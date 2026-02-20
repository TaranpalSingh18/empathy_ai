"""Emotion detection using a local Hugging Face model.

Model: SamLowe/roberta-base-go_emotions (GoEmotions)

Provides `detect_emotion(text: str) -> dict` returning:
    {"emotion": str, "confidence": float, "all_scores": {label: score}, "intensity": str}

This model predicts a fine-grained set of 27 emotions plus `neutral` (GoEmotions).

Corpus analysis includes emotional valence and prosody modeling for subtle
global pitch adjustment based on text sentiment and emotional stability.
"""
from typing import Dict
import nltk
import json
from contextlib import asynccontextmanager

try:
    from .config import compute_valence_score, compute_base_pitch, apply_base_pitch_to_params, get_voice_params
except ImportError:
    # Fallback for __main__ execution
    from config import compute_valence_score, compute_base_pitch, apply_base_pitch_to_params, get_voice_params

try:
    from transformers import pipeline
except Exception as e:  # pragma: no cover - helpful error when deps missing
    raise ImportError(
        "transformers is required to use emotion_detector. Install dependencies: pip install -r requirements.txt"
    ) from e


_detector = None


def _init_detector():
    global _detector
    if _detector is None:
        # return_all_scores=True gives scores for all labels
        _detector = pipeline(
            "text-classification",
            model="SamLowe/roberta-base-go_emotions",
            return_all_scores=True,
        )


# GoEmotions label set (informational)
GOEMOTIONS_LABELS = [
    "admiration",
    "amusement",
    "approval",
    "caring",
    "desire",
    "excitement",
    "gratitude",
    "joy",
    "love",
    "optimism",
    "pride",
    "relief",
    "anger",
    "annoyance",
    "disappointment",
    "disapproval",
    "disgust",
    "embarrassment",
    "fear",
    "grief",
    "nervousness",
    "remorse",
    "sadness",
    "confusion",
    "curiosity",
    "realization",
    "surprise",
    "neutral",
]


def _intensity_from_score(score: float) -> str:
    if score > 0.85:
        return "high"
    elif score >= 0.60:
        return "medium"
    else:
        return "low"


def detect_emotion(text: str) -> Dict:
    """Detect the predominant emotion in `text`.

    Returns a dict with keys:
      - emotion: one of joy, sadness, anger, fear, disgust, surprise, neutral
      - confidence: float between 0 and 1
      - all_scores: dict mapping each label -> score
      - intensity: 'high'|'medium'|'low' based on confidence thresholds
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text.strip() == "":
        return {"emotion": "neutral", "confidence": 0.0, "all_scores": {}, "intensity": "low"}

    _init_detector()

    # pipeline output can vary across HF versions and model wrappers.
    raw = _detector(text)

    # Normalize into a mapping label->score
    all_scores = {}

    # Handle common shapes robustly
    if isinstance(raw, dict):
        # mapping label->score
        for k, v in raw.items():
            try:
                all_scores[str(k).lower()] = float(v)
            except Exception:
                continue
    elif isinstance(raw, list):
        # batch outputs: take first item
        first = raw[0] if raw else []
        # first may be a list of dicts, a dict, or a list/tuple of pairs
        if isinstance(first, list):
            iterable = first
        else:
            iterable = [first]

        for entry in iterable:
            if isinstance(entry, dict):
                # dict may be {'label': 'joy', 'score': 0.9} or { 'joy': 0.9 }
                if "label" in entry and "score" in entry:
                    all_scores[str(entry["label"]).lower()] = float(entry["score"])
                else:
                    for k, v in entry.items():
                        try:
                            all_scores[str(k).lower()] = float(v)
                        except Exception:
                            continue
            elif isinstance(entry, (list, tuple)) and len(entry) >= 2:
                try:
                    all_scores[str(entry[0]).lower()] = float(entry[1])
                except Exception:
                    continue
            elif isinstance(entry, str):
                # label with unknown score
                all_scores[entry.lower()] = all_scores.get(entry.lower(), 0.0)
            # otherwise ignore unknown entry types
    else:
        raise RuntimeError("unexpected model output type: %r" % (type(raw),))

    # If we couldn't build scores, fallback to neutral
    if not all_scores:
        return {"emotion": "neutral", "confidence": 0.0, "all_scores": {}, "intensity": "low"}

    # Pick top prediction
    emotion, confidence = max(all_scores.items(), key=lambda kv: kv[1])
    emotion = str(emotion).lower()
    confidence = float(confidence)

    # Intensity scaling
    if confidence > 0.85:
        intensity = "high"
    elif confidence >= 0.60:
        intensity = "medium"
    else:
        intensity = "low"

    return {"emotion": emotion, "confidence": confidence, "all_scores": all_scores, "intensity": intensity}


def get_dominant_emotion(timeline: list) -> str:
    """Count frequency of top emotion per sentence and return the most frequent label."""
    from collections import Counter

    tops = []
    for item in timeline:
        emotions = item.get("emotions", [])
        if emotions:
            tops.append(emotions[0]["label"])
    if not tops:
        return "neutral"
    return Counter(tops).most_common(1)[0][0]


def get_weighted_emotion(timeline: list) -> str:
    """Sum scores per emotion across all sentences and return the highest-weighted emotion."""
    totals = {}
    for item in timeline:
        for e in item.get("emotions", []):
            lbl = e["label"]
            totals[lbl] = totals.get(lbl, 0.0) + float(e.get("confidence", 0.0))
    if not totals:
        return "neutral"
    return max(totals.items(), key=lambda kv: kv[1])[0]


def _intensity_from_score(score: float) -> str:
    if score > 0.85:
        return "high"
    elif score >= 0.60:
        return "medium"
    else:
        return "low"


def compute_emotional_volatility(timeline: list) -> float:
    """Compute volatility as proportion of sentence-to-sentence changes in the top emotion.

    Returns a float between 0 and 1.
    """
    tops = []
    for item in timeline:
        emotions = item.get("emotions", [])
        if emotions:
            tops.append(emotions[0]["label"])
    if len(tops) < 2:
        return 0.0
    changes = 0
    for a, b in zip(tops, tops[1:]):
        if a != b:
            changes += 1
    return changes / (len(tops) - 1)


def analyze_corpus(text: str) -> Dict:
    """Analyze a long text corpus and return timeline, dominant, weighted, and volatility.

    Timeline format:

    [
        {"sentence": "...", "emotions": [{"label": "joy", "score": 0.82}, ...]},
        ...
    ]
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # # Ensure punkt is available
    # try:
    #     nltk.data.find("tokenizers/punkt")
    # except Exception:
    #     try:
    #         nltk.download("punkt")
    #         nltk.download('punkt_tab')
    #     except Exception:
    #         pass

    sentences = nltk.sent_tokenize(text)
    timeline = []
    for s in sentences:
        det = detect_emotion(s)
        # convert all_scores dict to sorted list of tuples
        all_scores = det.get("all_scores", {})
        emotions_list = [
            {"label": lbl, "confidence": float(score), "intensity": _intensity_from_score(float(score))}
            for lbl, score in sorted(all_scores.items(), key=lambda kv: kv[1], reverse=True)
        ]
        timeline.append({"sentence": s, "emotions": emotions_list})

    dominant = get_dominant_emotion(timeline)
    weighted = get_weighted_emotion(timeline)
    volatility = compute_emotional_volatility(timeline)

    # Compute corpus-level emotional valence and prosody
    valence = compute_valence_score(timeline)
    base_pitch = compute_base_pitch(valence, volatility)

    return {
        "timeline": timeline,
        "dominant_emotion": dominant,
        "weighted_emotion": weighted,
        "volatility_score": float(volatility),
        "valence_score": float(valence),
        "base_pitch": float(base_pitch),
    }


def apply_prosody_to_timeline(corpus_result: Dict) -> Dict:
    """Apply corpus-level prosody bias to each sentence's voice parameters.

    Takes the output of analyze_corpus and enriches each timeline entry with
    final voice parameters (speed, pitch, volume) that include the base_pitch
    global adjustment combined with sentence-level emotional modulation.

    Args:
        corpus_result: dict from analyze_corpus() with "timeline", "base_pitch", etc.

    Returns:
        New dict with same structure, plus "sentence_voice_params" list in timeline items
    """
    if not corpus_result:
        return corpus_result

    timeline = corpus_result.get("timeline", [])
    base_pitch = corpus_result.get("base_pitch", 0.0)

    enhanced_timeline = []
    for item in timeline:
        sentence = item.get("sentence", "")
        emotions = item.get("emotions", [])

        # Get the top emotion and its intensity to select voice parameters
        voice_params = None
        if emotions:
            top_emotion = emotions[0]
            emotion_label = top_emotion.get("label", "neutral")
            intensity = top_emotion.get("intensity", "medium")
            voice_params = get_voice_params(emotion_label, intensity)
            # Apply base_pitch modulation
            voice_params = apply_base_pitch_to_params(voice_params, base_pitch)

        enhanced_entry = {
            "sentence": sentence,
            "emotions": emotions,
            "voice_params": voice_params,
        }
        enhanced_timeline.append(enhanced_entry)

    result = dict(corpus_result)
    result["timeline"] = enhanced_timeline
    return result


if __name__ == "__main__":
    import json

    # Mixed-emotion corpus: multiple sentences to analyze as a corpus
    corpus = (
      "Today felt like a strange blend of everything at once. I woke up feeling hopeful and motivated, ready to take on the day, but somewhere between deadlines and expectations, a quiet anxiety started creeping in. There were moments of genuine happiness — a small compliment, a message from a friend — that made me smile unexpectedly."
    )

    result = analyze_corpus(corpus)

    # Print timeline in requested format
    print("=== EMOTIONAL TIMELINE ===\n")
    print(json.dumps(result["timeline"], indent=2))

    # Print prosody and overall tone summary
    print("\n=== EMOTIONAL PROSODY & TONE ===\n")
    print(json.dumps({
        "dominant_emotion": result["dominant_emotion"],
        "weighted_emotion": result["weighted_emotion"],
        "volatility_score": result["volatility_score"],
        "valence_score": result["valence_score"],
        "base_pitch_adjustment_semitones": result["base_pitch"],
    }, indent=2))

    # Show enhanced timeline with voice parameters
    print("\n=== VOICE PARAMETERS (With Prosody Bias) ===\n")
    enhanced = apply_prosody_to_timeline(result)
    for i, entry in enumerate(enhanced["timeline"], 1):
        print(f"{i}. {entry['sentence']}")
        if entry.get("voice_params"):
            print(f"   Voice params: speed={entry['voice_params'].get('speed'):.2f}, "
                  f"pitch={entry['voice_params'].get('pitch_semitones'):.1f} st, "
                  f"volume={entry['voice_params'].get('volume_db'):.1f} dB")
        print()
