"""TTS synthesis helpers using gTTS and pydub.

Functions:
 - synthesize_sentence(text, output_path) -> wav_path
 - synthesize_batch(sentences, output_dir) -> list[wav_path]

Handles short/empty text and simple retry logic for network errors.
"""
import os
import time
import tempfile
from typing import List

from gtts import gTTS
from pydub import AudioSegment


def synthesize_sentence(text: str, output_path: str) -> str:
    """Synthesize `text` to WAV at `output_path`. Returns WAV path.

    - Saves intermediate MP3 then converts to WAV using pydub.
    - Handles empty/very-short text by generating a short silent WAV.
    - Retries gTTS up to 2 times on network errors with 1s delay.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Edge cases: empty or extremely short input
    if text.strip() == "" or len(text.strip()) < 3:
        silence = AudioSegment.silent(duration=600)
        silence.export(output_path, format="wav")
        return output_path

    mp3_fd, mp3_path = tempfile.mkstemp(suffix=".mp3")
    os.close(mp3_fd)
    try:
        attempts = 0
        last_exc = None
        while attempts < 3:
            try:
                tts = gTTS(text)
                tts.save(mp3_path)
                break
            except Exception as e:
                last_exc = e
                attempts += 1
                if attempts >= 3:
                    raise
                time.sleep(1)

        # Convert mp3 to wav using pydub
        audio = AudioSegment.from_file(mp3_path, format="mp3")
        audio.export(output_path, format="wav")
        return output_path
    finally:
        try:
            if os.path.exists(mp3_path):
                os.remove(mp3_path)
        except Exception:
            pass


def synthesize_batch(sentences: List[str], output_dir: str) -> List[str]:
    """Synthesize a list of sentences to WAV files in `output_dir`.

    Returns ordered list of WAV file paths.
    Creates `output_dir` if missing.
    """
    os.makedirs(output_dir, exist_ok=True)
    wav_paths: List[str] = []
    for idx, s in enumerate(sentences, start=1):
        out_wav = os.path.join(output_dir, f"sentence_{idx:03d}.wav")
        synthesize_sentence(s, out_wav)
        wav_paths.append(out_wav)

    return wav_paths


if __name__ == "__main__":
    # quick manual test
    out = synthesize_batch(["Hello world.", "I am so happy!", "This is sad."], output_dir="./temp_tts")
    print(out)
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
