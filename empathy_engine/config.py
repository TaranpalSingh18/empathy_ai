"""Emotion to voice parameter mappings for GoEmotions labels.

Each emotion maps to three intensity levels: `low`, `medium`, `high`.
Parameters:
 - `speed`: float (0.7 - 1.4)
 - `pitch_semitones`: int (-5 - +5)
 - `volume_db`: float (-6 - +6)

Mappings are designed so `high` intensity uses more extreme parameter values,
`low` is more subtle, and `medium` is in-between.
"""

from typing import Dict


# GoEmotions label set (subset from the dataset + neutral)
EMOTIONS = [
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


EMOTION_VOICE_MAP: Dict[str, Dict[str, Dict]] = {
    # Positive / Warm
    "admiration": {
        "high": {"speed": 1.25, "pitch_semitones": 3, "volume_db": 2.5},
        "medium": {"speed": 1.12, "pitch_semitones": 2, "volume_db": 1.0},
        "low": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 0.5},
    },
    "amusement": {
        "high": {"speed": 1.30, "pitch_semitones": 3, "volume_db": 3.0},
        "medium": {"speed": 1.18, "pitch_semitones": 2, "volume_db": 1.5},
        "low": {"speed": 1.12, "pitch_semitones": 1, "volume_db": 0.6},
    },
    "approval": {
        "high": {"speed": 1.22, "pitch_semitones": 2, "volume_db": 2.0},
        "medium": {"speed": 1.10, "pitch_semitones": 1, "volume_db": 1.0},
        "low": {"speed": 1.03, "pitch_semitones": 0, "volume_db": 0.4},
    },
    "caring": {
        "high": {"speed": 1.05, "pitch_semitones": 2, "volume_db": 1.0},
        "medium": {"speed": 1.00, "pitch_semitones": 1, "volume_db": 0.5},
        "low": {"speed": 0.95, "pitch_semitones": 0, "volume_db": 0.0},
    },
    "desire": {
        "high": {"speed": 1.30, "pitch_semitones": 2, "volume_db": 2.0},
        "medium": {"speed": 1.15, "pitch_semitones": 1, "volume_db": 1.0},
        "low": {"speed": 1.05, "pitch_semitones": 0, "volume_db": 0.5},
    },
    "excitement": {
        "high": {"speed": 1.35, "pitch_semitones": 4, "volume_db": 4.0},
        "medium": {"speed": 1.22, "pitch_semitones": 3, "volume_db": 2.0},
        "low": {"speed": 1.12, "pitch_semitones": 2, "volume_db": 1.0},
    },
    "gratitude": {
        "high": {"speed": 1.12, "pitch_semitones": 2, "volume_db": 2.0},
        "medium": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 1.0},
        "low": {"speed": 1.00, "pitch_semitones": 0, "volume_db": 0.5},
    },
    "joy": {
        "high": {"speed": 1.30, "pitch_semitones": 4, "volume_db": 3.0},
        "medium": {"speed": 1.18, "pitch_semitones": 2, "volume_db": 1.5},
        "low": {"speed": 1.08, "pitch_semitones": 1, "volume_db": 1.0},
    },
    "love": {
        "high": {"speed": 1.20, "pitch_semitones": 3, "volume_db": 2.0},
        "medium": {"speed": 1.08, "pitch_semitones": 2, "volume_db": 1.0},
        "low": {"speed": 1.00, "pitch_semitones": 1, "volume_db": 0.5},
    },
    "optimism": {
        "high": {"speed": 1.25, "pitch_semitones": 3, "volume_db": 2.0},
        "medium": {"speed": 1.12, "pitch_semitones": 2, "volume_db": 1.0},
        "low": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 0.5},
    },
    "pride": {
        "high": {"speed": 1.20, "pitch_semitones": 2, "volume_db": 2.5},
        "medium": {"speed": 1.10, "pitch_semitones": 1, "volume_db": 1.0},
        "low": {"speed": 1.00, "pitch_semitones": 1, "volume_db": 0.5},
    },
    "relief": {
        "high": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 1.0},
        "medium": {"speed": 1.00, "pitch_semitones": 0, "volume_db": 0.5},
        "low": {"speed": 0.95, "pitch_semitones": 0, "volume_db": -0.2},
    },

    # Negative / Tense
    "anger": {
        "high": {"speed": 1.35, "pitch_semitones": 2, "volume_db": 4.5},
        "medium": {"speed": 1.20, "pitch_semitones": 1, "volume_db": 2.0},
        "low": {"speed": 1.05, "pitch_semitones": 0, "volume_db": 1.0},
    },
    "annoyance": {
        "high": {"speed": 1.22, "pitch_semitones": 1, "volume_db": 2.0},
        "medium": {"speed": 1.12, "pitch_semitones": 0, "volume_db": 1.0},
        "low": {"speed": 1.02, "pitch_semitones": 0, "volume_db": 0.2},
    },
    "disappointment": {
        "high": {"speed": 0.82, "pitch_semitones": -2, "volume_db": -2.5},
        "medium": {"speed": 0.90, "pitch_semitones": -1, "volume_db": -1.2},
        "low": {"speed": 0.95, "pitch_semitones": -1, "volume_db": -0.6},
    },
    "disapproval": {
        "high": {"speed": 0.88, "pitch_semitones": -2, "volume_db": -1.8},
        "medium": {"speed": 0.95, "pitch_semitones": -1, "volume_db": -1.0},
        "low": {"speed": 0.98, "pitch_semitones": 0, "volume_db": -0.3},
    },
    "disgust": {
        "high": {"speed": 0.90, "pitch_semitones": -2, "volume_db": -2.5},
        "medium": {"speed": 0.95, "pitch_semitones": -1, "volume_db": -1.0},
        "low": {"speed": 1.00, "pitch_semitones": 0, "volume_db": -0.3},
    },
    "embarrassment": {
        "high": {"speed": 0.85, "pitch_semitones": -3, "volume_db": -3.0},
        "medium": {"speed": 0.90, "pitch_semitones": -2, "volume_db": -2.0},
        "low": {"speed": 0.95, "pitch_semitones": -1, "volume_db": -1.0},
    },
    "fear": {
        "high": {"speed": 1.25, "pitch_semitones": 3, "volume_db": -1.0},
        "medium": {"speed": 1.12, "pitch_semitones": 2, "volume_db": -0.5},
        "low": {"speed": 1.00, "pitch_semitones": 1, "volume_db": 0.0},
    },
    "grief": {
        "high": {"speed": 0.75, "pitch_semitones": -4, "volume_db": -4.0},
        "medium": {"speed": 0.82, "pitch_semitones": -3, "volume_db": -2.0},
        "low": {"speed": 0.90, "pitch_semitones": -2, "volume_db": -1.0},
    },
    "nervousness": {
        "high": {"speed": 1.28, "pitch_semitones": 3, "volume_db": -0.5},
        "medium": {"speed": 1.15, "pitch_semitones": 2, "volume_db": -0.2},
        "low": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 0.0},
    },
    "remorse": {
        "high": {"speed": 0.85, "pitch_semitones": -2, "volume_db": -2.5},
        "medium": {"speed": 0.92, "pitch_semitones": -1, "volume_db": -1.2},
        "low": {"speed": 0.98, "pitch_semitones": -1, "volume_db": -0.5},
    },
    "sadness": {
        "high": {"speed": 0.78, "pitch_semitones": -3, "volume_db": -3.0},
        "medium": {"speed": 0.85, "pitch_semitones": -2, "volume_db": -1.5},
        "low": {"speed": 0.95, "pitch_semitones": -1, "volume_db": -0.6},
    },

    # Cognitive / Reactive
    "confusion": {
        "high": {"speed": 1.05, "pitch_semitones": 1, "volume_db": -0.5},
        "medium": {"speed": 0.98, "pitch_semitones": 0, "volume_db": 0.0},
        "low": {"speed": 0.95, "pitch_semitones": 0, "volume_db": 0.0},
    },
    "curiosity": {
        "high": {"speed": 1.20, "pitch_semitones": 2, "volume_db": 1.5},
        "medium": {"speed": 1.12, "pitch_semitones": 1, "volume_db": 0.5},
        "low": {"speed": 1.05, "pitch_semitones": 1, "volume_db": 0.2},
    },
    "realization": {
        "high": {"speed": 1.18, "pitch_semitones": 2, "volume_db": 1.0},
        "medium": {"speed": 1.08, "pitch_semitones": 1, "volume_db": 0.5},
        "low": {"speed": 1.00, "pitch_semitones": 0, "volume_db": 0.0},
    },
    "surprise": {
        "high": {"speed": 1.40, "pitch_semitones": 5, "volume_db": 5.5},
        "medium": {"speed": 1.25, "pitch_semitones": 3, "volume_db": 2.5},
        "low": {"speed": 1.12, "pitch_semitones": 2, "volume_db": 1.0},
    },

    # Neutral
    "neutral": {
        "high": {"speed": 1.00, "pitch_semitones": 0, "volume_db": 0.0},
        "medium": {"speed": 0.98, "pitch_semitones": 0, "volume_db": 0.0},
        "low": {"speed": 0.95, "pitch_semitones": 0, "volume_db": -0.5},
    },
}


def get_voice_params(emotion: str, intensity: str) -> Dict:
    """Return voice parameters for a given emotion and intensity.

    Falls back to `neutral`/`medium` for unknown values.
    """
    e = (emotion or "").lower()
    i = (intensity or "").lower()
    if e not in EMOTION_VOICE_MAP:
        e = "neutral"
    if i not in ("low", "medium", "high"):
        i = "medium"
    return EMOTION_VOICE_MAP[e][i]


# ============================================================================
# Emotional Prosody Modeling: Valence & Pitch Bias
# ============================================================================
#
# Maps each emotion to a psychological valence score in [-1, 1].
# This drives corpus-level prosody adjustments (subtle pitch bias).
#
# Scale rationale:
#   [+0.8, +1.0]:  Ecstatic, pure positivity (joy, love, elation)
#   [+0.5, +0.8):  Positive, warm emotions (happiness, admiration, care)
#   [+0.2, +0.5):  Mildly positive (curiosity, approval, excitement onset)
#   [-0.2, +0.2):  Neutral or ambiguous (neutral, confusion, realization)
#   [-0.5, -0.2):  Mildly negative (concern, mild disappointment)
#   [-0.8, -0.5):  Negative, tense (anger, fear, disgust)
#   [-1.0, -0.8]:  Deep negative (grief, despair, extreme remorse)
#


EMOTION_VALENCE: Dict[str, float] = {
    # High positivity (0.65–1.0): warm, joyful, loving, proud
    "joy": 0.90,
    "love": 0.95,
    "excitement": 0.85,
    "amusement": 0.88,
    "gratitude": 0.80,
    "admiration": 0.80,
    "pride": 0.82,
    "optimism": 0.78,
    "caring": 0.70,
    "desire": 0.72,
    "approval": 0.75,
    "relief": 0.65,

    # Moderate positivity (0.3–0.5): interest, curiosity, realization, surprise
    "curiosity": 0.35,
    "realization": 0.40,
    "surprise": 0.50,  # Mild positive bias; surprise can be either

    # Neutral (0.0)
    "neutral": 0.0,

    # Mild negativity (-0.3 to -0.6): confusion, nervousness, annoyance, disappointment
    "confusion": -0.15,
    "nervousness": -0.50,
    "annoyance": -0.45,
    "disappointment": -0.60,
    "disapproval": -0.55,

    # Strong negativity (-0.65 to -0.85): embarrassment, anger, fear, disgust, remorse
    "embarrassment": -0.65,
    "anger": -0.80,
    "fear": -0.70,
    "disgust": -0.85,
    "remorse": -0.70,

    # Extreme negativity (-1.0 to -0.75): sadness, grief (existential sorrow)
    "sadness": -0.75,
    "grief": -0.95,
}


def compute_valence_score(timeline: list) -> float:
    """Compute weighted corpus-level emotional valence from timeline.

    Valence represents the overall positivity/negativity of the text,
    accounting for both emotion type and confidence.

    Args:
        timeline: list of dicts with "emotions" key, each emotion has "label" and "confidence"

    Returns:
        float in [-1.0, 1.0]; 0.0 if no emotions found or no weighted sum

    Algorithm:
        For each emotion in each sentence:
            weighted_sum += EMOTION_VALENCE[label] * confidence
            total_weight += confidence
        valence = weighted_sum / total_weight (if total_weight > 0)
        Return clamped to [-1, 1]
    """
    if not timeline:
        return 0.0

    weighted_sum = 0.0
    total_weight = 0.0

    for item in timeline:
        emotions = item.get("emotions", [])
        for emotion in emotions:
            label = emotion.get("label", "neutral").lower()
            confidence = float(emotion.get("confidence", 0.0))

            # Lookup valence; default to 0.0 (neutral) if unknown emotion
            valence = EMOTION_VALENCE.get(label, 0.0)
            weighted_sum += valence * confidence
            total_weight += confidence

    if total_weight == 0.0:
        return 0.0

    result = weighted_sum / total_weight
    # Clamp to [-1, 1]
    return max(-1.0, min(1.0, result))


def compute_base_pitch(valence_score: float, volatility_score: float) -> float:
    """Compute global pitch bias from valence and volatility.

    Creates a subtle, corpus-level prosodic adjustment that:
      - Raises pitch for positive texts (happy, uplifting)
      - Lowers pitch for negative texts (sad, angry, tense)
      - Reduces the bias if emotional sentiment shifts frequently (high volatility)

    This ensures the overall "tone" of the speech reflects the text's emotional
    character without overwhelming the sentence-level emotion modulation.

    Args:
        valence_score: float in [-1, 1] from compute_valence_score()
        volatility_score: float in [0, 1] from analyze_corpus() (fraction of emotion changes)

    Returns:
        float in semitones (typically [-0.7, +0.7] due to modulation)

    Algorithm:
        base_pitch = valence_score * 0.7       # Scale to subtle semitone range
        volatility_damp = 1 - min(volatility_score, 1.0)
        base_pitch *= volatility_damp          # Reduce if emotionally unstable
        Return base_pitch
    """
    # Scale valence to a subtle pitch adjustment (max ±0.7 semitones)
    base_pitch = valence_score * 0.7

    # Dampen the effect if the text has high emotional volatility
    # High volatility means emotions shift frequently → keep pitch more neutral
    volatility_damp = 1.0 - min(volatility_score, 1.0)
    base_pitch *= volatility_damp

    return float(base_pitch)


def apply_base_pitch_to_params(sentence_params: Dict, base_pitch: float) -> Dict:
    """Apply global pitch bias to sentence-level voice parameters.

    Modulates the sentence's pitch_semitones by the corpus-level base_pitch,
    preserving the original sentence-level emotion contrast while adding
    a subtle global harmonic shift.

    Args:
        sentence_params: dict from get_voice_params() with "pitch_semitones" key
        base_pitch: float from compute_base_pitch() (typically in [-0.7, +0.7])

    Returns:
        New dict with adjusted pitch_semitones; original is not mutated
    """
    result = dict(sentence_params)  # Shallow copy to avoid mutation
    current_pitch = result.get("pitch_semitones", 0)
    result["pitch_semitones"] = current_pitch + base_pitch
    # Clamp to physically safe range [-5, +5]
    result["pitch_semitones"] = max(-5, min(5, result["pitch_semitones"]))
    return result
