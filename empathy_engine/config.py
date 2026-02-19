"""Emotion to voice parameter mappings for GoEmotions labels.

Each emotion maps to three intensity levels: `low`, `medium`, `high`.
Parameters:
 - `speed`: float (0.7 - 1.4)
 - `pitch_semitones`: int/float (-5 - +5)
 - `volume_db`: float (-6 - +6)

Design philosophy (revised):
  - Minimal perturbation: the speaker's voice identity must be preserved.
  - Speed changes are subtle (max ±0.06 from 1.0 baseline).
  - Pitch shifts are gentle; high-intensity caps at ±2.5 semitones.
  - Volume is used sparingly; large swings feel artificial in TTS.
  - Low intensity values hover near neutral so blended outputs stay natural.
  - Bug fix: sadness medium/low pitch corrected to negative (was erroneously positive).
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

    # ── Positive / Warm ──────────────────────────────────────────────────────

    # Warm, slightly elevated; restrained rise so it sounds genuine, not giddy
    "admiration": {
        "high":   {"speed": 1.03, "pitch_semitones":  1.5, "volume_db":  1.0},
        "medium": {"speed": 1.02, "pitch_semitones":  0.8, "volume_db":  0.5},
        "low":    {"speed": 1.00, "pitch_semitones":  0.3, "volume_db":  0.2},
    },

    # Light, a touch faster; playful without sounding manic
    "amusement": {
        "high":   {"speed": 1.05, "pitch_semitones":  1.8, "volume_db":  1.2},
        "medium": {"speed": 1.03, "pitch_semitones":  1.0, "volume_db":  0.6},
        "low":    {"speed": 1.01, "pitch_semitones":  0.5, "volume_db":  0.3},
    },

    # Calm positivity; small upward nudge conveys affirmation
    "approval": {
        "high":   {"speed": 1.02, "pitch_semitones":  1.2, "volume_db":  0.8},
        "medium": {"speed": 1.01, "pitch_semitones":  0.6, "volume_db":  0.4},
        "low":    {"speed": 1.00, "pitch_semitones":  0.2, "volume_db":  0.1},
    },

    # Soft and warm; slightly slower, gentle pitch lift
    "caring": {
        "high":   {"speed": 0.98, "pitch_semitones":  1.0, "volume_db":  0.6},
        "medium": {"speed": 0.99, "pitch_semitones":  0.5, "volume_db":  0.3},
        "low":    {"speed": 1.00, "pitch_semitones":  0.2, "volume_db":  0.1},
    },

    # Slightly slower, breathy feel; pitch up conveys longing
    "desire": {
        "high":   {"speed": 0.99, "pitch_semitones":  1.5, "volume_db":  0.8},
        "medium": {"speed": 1.00, "pitch_semitones":  0.8, "volume_db":  0.4},
        "low":    {"speed": 1.00, "pitch_semitones":  0.3, "volume_db":  0.1},
    },

    # Noticeably faster and brighter; high energy but not shrill
    "excitement": {
        "high":   {"speed": 1.06, "pitch_semitones":  2.0, "volume_db":  1.5},
        "medium": {"speed": 1.04, "pitch_semitones":  1.2, "volume_db":  0.8},
        "low":    {"speed": 1.02, "pitch_semitones":  0.5, "volume_db":  0.3},
    },

    # Warm and sincere; modest speed + pitch rise
    "gratitude": {
        "high":   {"speed": 1.02, "pitch_semitones":  1.5, "volume_db":  0.8},
        "medium": {"speed": 1.01, "pitch_semitones":  0.8, "volume_db":  0.4},
        "low":    {"speed": 1.00, "pitch_semitones":  0.3, "volume_db":  0.2},
    },

    # Bright and upbeat; the most clearly positive prosody cluster
    "joy": {
        "high":   {"speed": 1.06, "pitch_semitones":  2.0, "volume_db":  1.5},
        "medium": {"speed": 1.04, "pitch_semitones":  1.2, "volume_db":  0.8},
        "low":    {"speed": 1.02, "pitch_semitones":  0.6, "volume_db":  0.4},
    },

    # Warm, slightly rounded; pitch lift without speed surge
    "love": {
        "high":   {"speed": 1.01, "pitch_semitones":  1.8, "volume_db":  0.8},
        "medium": {"speed": 1.00, "pitch_semitones":  1.0, "volume_db":  0.4},
        "low":    {"speed": 1.00, "pitch_semitones":  0.4, "volume_db":  0.2},
    },

    # Forward-looking; slight speed and pitch rise
    "optimism": {
        "high":   {"speed": 1.04, "pitch_semitones":  1.8, "volume_db":  1.0},
        "medium": {"speed": 1.02, "pitch_semitones":  1.0, "volume_db":  0.5},
        "low":    {"speed": 1.01, "pitch_semitones":  0.4, "volume_db":  0.2},
    },

    # Confident and measured; fuller volume, slight pitch rise
    "pride": {
        "high":   {"speed": 1.02, "pitch_semitones":  1.5, "volume_db":  1.2},
        "medium": {"speed": 1.01, "pitch_semitones":  0.8, "volume_db":  0.6},
        "low":    {"speed": 1.00, "pitch_semitones":  0.3, "volume_db":  0.2},
    },

    # Sigh of relief: pace eases slightly, neutral to mildly positive pitch
    "relief": {
        "high":   {"speed": 0.97, "pitch_semitones":  0.5, "volume_db":  0.5},
        "medium": {"speed": 0.98, "pitch_semitones":  0.2, "volume_db":  0.2},
        "low":    {"speed": 1.00, "pitch_semitones":  0.0, "volume_db":  0.0},
    },

    # ── Negative / Tense ─────────────────────────────────────────────────────

    # Tense and louder; pitch rises with intensity (not falls — anger is sharp)
    "anger": {
        "high":   {"speed": 1.05, "pitch_semitones":  1.5, "volume_db":  2.0},
        "medium": {"speed": 1.03, "pitch_semitones":  1.0, "volume_db":  1.2},
        "low":    {"speed": 1.01, "pitch_semitones":  0.5, "volume_db":  0.4},
    },

    # Clipped and slightly raised pitch; mild volume bump
    "annoyance": {
        "high":   {"speed": 1.03, "pitch_semitones":  1.0, "volume_db":  0.8},
        "medium": {"speed": 1.01, "pitch_semitones":  0.5, "volume_db":  0.4},
        "low":    {"speed": 1.00, "pitch_semitones":  0.2, "volume_db":  0.1},
    },

    # Slower, flatter; subdued volume — deflated energy
    "disappointment": {
        "high":   {"speed": 0.96, "pitch_semitones": -1.0, "volume_db": -1.0},
        "medium": {"speed": 0.97, "pitch_semitones": -0.5, "volume_db": -0.5},
        "low":    {"speed": 0.99, "pitch_semitones": -0.2, "volume_db": -0.2},
    },

    # Measured, slightly lower pitch; firm but not aggressive
    "disapproval": {
        "high":   {"speed": 0.97, "pitch_semitones": -1.2, "volume_db": -0.6},
        "medium": {"speed": 0.98, "pitch_semitones": -0.6, "volume_db": -0.3},
        "low":    {"speed": 0.99, "pitch_semitones": -0.2, "volume_db": -0.1},
    },

    # Slow, low, flat — revulsion drops pitch and drains energy
    "disgust": {
        "high":   {"speed": 0.96, "pitch_semitones": -1.8, "volume_db": -0.8},
        "medium": {"speed": 0.97, "pitch_semitones": -1.0, "volume_db": -0.4},
        "low":    {"speed": 0.99, "pitch_semitones": -0.4, "volume_db": -0.1},
    },

    # Quiet, subdued, slightly slower; withdrawn quality
    "embarrassment": {
        "high":   {"speed": 0.96, "pitch_semitones": -1.5, "volume_db": -1.5},
        "medium": {"speed": 0.97, "pitch_semitones": -0.8, "volume_db": -0.8},
        "low":    {"speed": 0.98, "pitch_semitones": -0.3, "volume_db": -0.3},
    },

    # Slightly faster (urgency) + pitch rise; quieter (caught throat feeling)
    "fear": {
        "high":   {"speed": 1.05, "pitch_semitones":  1.5, "volume_db": -0.5},
        "medium": {"speed": 1.03, "pitch_semitones":  0.8, "volume_db": -0.2},
        "low":    {"speed": 1.01, "pitch_semitones":  0.3, "volume_db":  0.0},
    },

    # Very slow, very quiet, low pitch — the most subdued prosody cluster
    "grief": {
        "high":   {"speed": 0.92, "pitch_semitones": -2.5, "volume_db": -1.8},
        "medium": {"speed": 0.95, "pitch_semitones": -1.5, "volume_db": -1.0},
        "low":    {"speed": 0.97, "pitch_semitones": -0.6, "volume_db": -0.5},
    },

    # Faster, slightly higher pitch; volume neutral (anxious restraint)
    "nervousness": {
        "high":   {"speed": 1.05, "pitch_semitones":  1.2, "volume_db":  0.0},
        "medium": {"speed": 1.03, "pitch_semitones":  0.6, "volume_db": -0.1},
        "low":    {"speed": 1.01, "pitch_semitones":  0.2, "volume_db":  0.0},
    },

    # Quiet, lower, slightly slower; genuine contrition
    "remorse": {
        "high":   {"speed": 0.96, "pitch_semitones": -1.5, "volume_db": -1.2},
        "medium": {"speed": 0.97, "pitch_semitones": -0.8, "volume_db": -0.6},
        "low":    {"speed": 0.99, "pitch_semitones": -0.3, "volume_db": -0.2},
    },

    # Slow, quiet, low — heavy and withdrawn
    # BUG FIX: medium/low pitch was erroneously +1 in original (should be ≤0)
    "sadness": {
        "high":   {"speed": 0.94, "pitch_semitones": -2.0, "volume_db": -1.5},
        "medium": {"speed": 0.96, "pitch_semitones": -1.0, "volume_db": -0.8},
        "low":    {"speed": 0.98, "pitch_semitones": -0.4, "volume_db": -0.3},
    },

    # ── Cognitive / Reactive ─────────────────────────────────────────────────

    # Slightly halting; mild speed dip, near-neutral pitch — "lost" feeling
    "confusion": {
        "high":   {"speed": 0.99, "pitch_semitones": -0.3, "volume_db": -0.3},
        "medium": {"speed": 1.00, "pitch_semitones": -0.1, "volume_db": -0.1},
        "low":    {"speed": 1.00, "pitch_semitones":  0.0, "volume_db":  0.0},
    },

    # Slightly faster, mild pitch rise — leaning in, engaged
    "curiosity": {
        "high":   {"speed": 1.03, "pitch_semitones":  1.0, "volume_db":  0.5},
        "medium": {"speed": 1.02, "pitch_semitones":  0.6, "volume_db":  0.3},
        "low":    {"speed": 1.01, "pitch_semitones":  0.2, "volume_db":  0.1},
    },

    # Small upward inflection, slight speed bump — "aha" quality
    "realization": {
        "high":   {"speed": 1.03, "pitch_semitones":  1.2, "volume_db":  0.5},
        "medium": {"speed": 1.02, "pitch_semitones":  0.6, "volume_db":  0.2},
        "low":    {"speed": 1.00, "pitch_semitones":  0.2, "volume_db":  0.1},
    },

    # Faster, brighter — reflexive jolt; positive valence default
    "surprise": {
        "high":   {"speed": 1.05, "pitch_semitones":  2.0, "volume_db":  1.2},
        "medium": {"speed": 1.03, "pitch_semitones":  1.2, "volume_db":  0.6},
        "low":    {"speed": 1.01, "pitch_semitones":  0.5, "volume_db":  0.2},
    },

    # ── Neutral ──────────────────────────────────────────────────────────────

    "neutral": {
        "high":   {"speed": 1.00, "pitch_semitones":  0.0, "volume_db":  0.0},
        "medium": {"speed": 1.00, "pitch_semitones":  0.0, "volume_db":  0.0},
        "low":    {"speed": 1.00, "pitch_semitones":  0.0, "volume_db":  0.0},
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
# This drives corpus-level prosody adjustments (very subtle pitch bias).
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
    "joy":          0.90,
    "love":         0.95,
    "excitement":   0.85,
    "amusement":    0.88,
    "gratitude":    0.80,
    "admiration":   0.80,
    "pride":        0.82,
    "optimism":     0.78,
    "caring":       0.70,
    "desire":       0.72,
    "approval":     0.75,
    "relief":       0.65,

    # Moderate positivity (0.3–0.5): interest, curiosity, realization, surprise
    "curiosity":    0.35,
    "realization":  0.40,
    "surprise":     0.50,   # Mild positive bias; surprise can go either way

    # Neutral (0.0)
    "neutral":      0.0,

    # Mild negativity (-0.15 to -0.60)
    "confusion":        -0.15,
    "nervousness":      -0.50,
    "annoyance":        -0.45,
    "disappointment":   -0.60,
    "disapproval":      -0.55,

    # Strong negativity (-0.65 to -0.85)
    "embarrassment":    -0.65,
    "anger":            -0.80,
    "fear":             -0.70,
    "disgust":          -0.85,
    "remorse":          -0.70,

    # Extreme negativity (-0.75 to -0.95)
    "sadness":          -0.75,
    "grief":            -0.95,
}


def compute_valence_score(timeline: list) -> float:
    """Compute weighted corpus-level emotional valence from timeline.

    Args:
        timeline: list of dicts with "emotions" key, each emotion has
                  "label" and "confidence"

    Returns:
        float in [-1.0, 1.0]; 0.0 if no emotions found
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
            valence = EMOTION_VALENCE.get(label, 0.0)
            weighted_sum += valence * confidence
            total_weight += confidence

    if total_weight == 0.0:
        return 0.0

    result = weighted_sum / total_weight
    return max(-1.0, min(1.0, result))


def compute_base_pitch(valence_score: float, volatility_score: float) -> float:
    """Compute global pitch bias from valence and volatility.

    Intentionally conservative: max corpus-level pitch shift is ±0.4 semitones
    (reduced from 0.7) so the baseline speaker identity is always preserved.
    High volatility dampens the shift toward neutral.

    Args:
        valence_score:    float in [-1, 1] from compute_valence_score()
        volatility_score: float in [0, 1] (fraction of emotion changes)

    Returns:
        float in semitones (typically [-0.4, +0.4] after damping)
    """
    # Reduced multiplier: 0.4 instead of 0.7 — gentler global pitch nudge
    base_pitch = valence_score * 0.4

    # Dampen if emotions shift frequently (keep pitch neutral in volatile text)
    volatility_damp = 1.0 - min(volatility_score, 1.0)
    base_pitch *= volatility_damp

    return float(base_pitch)


def apply_base_pitch_to_params(sentence_params: Dict, base_pitch: float) -> Dict:
    """Apply global pitch bias to sentence-level voice parameters.

    Args:
        sentence_params: dict from get_voice_params() with "pitch_semitones" key
        base_pitch:      float from compute_base_pitch()

    Returns:
        New dict with adjusted pitch_semitones clamped to [-5, +5]; original
        dict is not mutated.
    """
    result = dict(sentence_params)
    current_pitch = result.get("pitch_semitones", 0)
    result["pitch_semitones"] = max(-5.0, min(5.0, current_pitch + base_pitch))
    return result