"""Pipeline to run full Empathy Engine: detection -> TTS -> modulation -> mixdown"""
import os
import shutil
import uuid
from typing import Dict, List

from pydub import AudioSegment

try:
    from .emotion_detector import analyze_corpus
    from .tts_engine import synthesize_sentence
    from .voice_modulator import modulate
    from .config import get_voice_params
except ImportError:
    # Fallback for direct execution
    from emotion_detector import analyze_corpus
    from tts_engine import synthesize_sentence
    from voice_modulator import modulate
    from config import get_voice_params


def run_pipeline(text: str, output_dir: str = "static/audio") -> Dict:
    """Run the full pipeline and produce a concatenated WAV.

    Returns a dict with analysis and file paths.
    """
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, "temp")
    os.makedirs(temp_dir, exist_ok=True)

    result = analyze_corpus(text)

    # Enrich timeline if voice_params missing (safety)
    timeline = result.get("timeline", [])

    sentence_audio_paths: List[str] = []
    modulated_paths: List[str] = []

    try:
        # Step 2: synthesize raw audio for each sentence
        for idx, item in enumerate(timeline, start=1):
            sentence = item.get("sentence", "")
            # Raw TTS path
            raw_wav = os.path.join(temp_dir, f"raw_{idx:03d}.wav")
            synthesize_sentence(sentence, raw_wav)
            sentence_audio_paths.append(raw_wav)

        # Step 3: apply modulation per sentence
        for idx, item in enumerate(timeline, start=1):
            voice_params = item.get("voice_params")
            if not voice_params:
                # Fallback to top emotion if voice_params absent
                emotions = item.get("emotions", [])
                if emotions:
                    top = emotions[0]
                    voice_params = get_voice_params(top.get("label", "neutral"), top.get("intensity", "medium"))
                else:
                    voice_params = get_voice_params("neutral", "medium")

            raw_path = sentence_audio_paths[idx - 1]
            mod_path = os.path.join(temp_dir, f"mod_{idx:03d}.wav")
            modulate(raw_path, voice_params, mod_path)
            modulated_paths.append(mod_path)

        # Step 4: concatenate with 300ms silence gaps
        gap = AudioSegment.silent(duration=300)
        final = AudioSegment.silent(duration=0)
        for i, p in enumerate(modulated_paths):
            seg = AudioSegment.from_wav(p)
            final += seg
            if i < len(modulated_paths) - 1:
                final += gap

        out_name = f"empathy_output_{uuid.uuid4().hex[:8]}.wav"
        out_path = os.path.join(output_dir, out_name)
        final.export(out_path, format="wav")

        # Populate return structure
        return {
            "dominant_emotion": result.get("dominant_emotion"),
            "weighted_emotion": result.get("weighted_emotion"),
            "volatility_score": result.get("volatility_score"),
            "valence_score": result.get("valence_score"),
            "base_pitch": result.get("base_pitch"),
            "timeline": timeline,
            "output_audio_path": out_path,
            "sentence_audio_paths": modulated_paths,
        }
    finally:
        # Clean up intermediate files
        try:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
        except Exception:
            pass


if __name__ == "__main__":
    sample = (
        "I’m furious at you for not showing up yesterday. I waited for hours and felt completely ignored. But at the same time, I know you’ve been struggling, and I can’t stop caring about you. That’s what makes this hurt even more."
    )
    out = run_pipeline(sample, output_dir="static/audio")
    # Print succinct result (exclude long timeline and paths for brevity)
    summary = {k: out[k] for k in ("dominant_emotion", "weighted_emotion", "volatility_score", "valence_score", "base_pitch")}
    print(summary)
