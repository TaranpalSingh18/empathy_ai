# Empathy Engine

Empathy Engine detects emotion from text and modulates TTS voice output accordingly.

Structure:

- `app.py` — Flask scaffold
- `emotion_detector.py` — implemented emotion detector using local HF model
- `voice_modulator.py` — scaffold for audio modulation
- `tts_engine.py` — scaffold for TTS logic
- `config.py` — mapping from emotion+intensity to voice parameters
- `templates/index.html` — basic UI scaffold
- `static/audio/` — output audio files
- `requirements.txt` — needed Python packages

Run the detector tests:

```bash
python empathy_engine/emotion_detector.py
```

Install dependencies first:

```bash
pip install -r empathy_engine/requirements.txt
```
