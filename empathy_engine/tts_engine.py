"""Scaffold for TTS engine.

Example function may use gTTS to synthesize speech to a file.
"""
from typing import Dict


def synthesize_text(text: str, output_path: str, voice_params: Dict = None) -> None:
    """Synthesize `text` to `output_path`.

    `voice_params` can be used to choose voice or affect synthesis.
    This is a scaffold showing expected signature.
    """
    raise NotImplementedError("TTS synthesize function not implemented yet")
