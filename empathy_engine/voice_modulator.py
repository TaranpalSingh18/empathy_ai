"""Audio manipulation and voice modulation utilities.

Implements speed, pitch, and volume modulation on pydub AudioSegment
objects. Uses pydub natively; pitch shifting uses speed + resampling
to avoid heavy JIT compilation (librosa/numba issues on Windows).
"""
from typing import Dict
import os
import tempfile

from pydub import AudioSegment


def _clamp(v, lo, hi):
    return max(lo, min(hi, v))


def apply_speed(audio: AudioSegment, speed: float) -> AudioSegment:
    """Change playback speed by adjusting frame rate and resetting to original.

    Clamps `speed` to [0.7, 1.4] before applying.
    """
    speed = _clamp(speed, 0.7, 1.4)
    new_frame_rate = int(audio.frame_rate * speed)
    altered = audio._spawn(audio.raw_data, overrides={"frame_rate": new_frame_rate})
    return altered.set_frame_rate(audio.frame_rate)


def apply_pitch(audio: AudioSegment, semitones: float) -> AudioSegment:
    """Shift pitch by `semitones` using frame rate manipulation.

    This is a simple pitch shift that avoids heavy JIT compilation (librosa/numba).
    Pitch shift is implemented via speed change + resampling.
    Semitones is clamped to [-5, 5].
    """
    semitones = _clamp(semitones, -5.0, 5.0)

    if semitones == 0:
        return audio

    # Convert semitones to frequency ratio: 2^(semitones/12)
    ratio = 2.0 ** (semitones / 12.0)

    # Speed up the audio (this raises pitch)
    new_rate = int(audio.frame_rate * ratio)
    pitched = audio._spawn(audio.raw_data, overrides={"frame_rate": new_rate})

    # Resample back to original frame rate to adjust duration
    return pitched.set_frame_rate(audio.frame_rate)


def apply_volume(audio: AudioSegment, volume_db: float) -> AudioSegment:
    """Adjust volume in dB; clamp to [-6, +6]."""
    volume_db = _clamp(volume_db, -6.0, 6.0)
    return audio.apply_gain(volume_db)


def modulate(input_path: str, voice_params: Dict, output_path: str) -> str:
    """Apply speed -> pitch -> volume to `input_path` and save to `output_path`.

    `voice_params` should contain keys: `speed`, `pitch_semitones`, `volume_db`.
    Returns `output_path`.
    """
    audio = AudioSegment.from_file(input_path)

    speed = float(voice_params.get("speed", 1.0))
    pitch = float(voice_params.get("pitch_semitones", 0.0))
    volume = float(voice_params.get("volume_db", 0.0))

    # Apply in order: speed -> pitch -> volume
    audio = apply_speed(audio, speed)
    audio = apply_pitch(audio, pitch)
    audio = apply_volume(audio, volume)

    # Export final wav
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    audio.export(output_path, format="wav")
    return output_path
