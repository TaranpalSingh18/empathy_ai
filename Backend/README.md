# Empathy AI — Backend

This folder contains a small FastAPI server that exposes a single endpoint to generate speech using the `empathy_engine` pipeline.

Endpoints
- `GET /health` — basic health check
- `POST /generate-speech` — Accepts JSON `{ "text": "..." }` and returns the generated WAV file as `audio/wav`.

How it works
1. The endpoint calls `empathy_engine.pipeline.run_pipeline(text)` which synthesizes audio and returns a result dict containing `output_audio_path`.
2. The backend returns the generated WAV file as a `FileResponse`.

Run locally

1. Create a Python environment and install dependencies. You must have the dependencies needed by `empathy_engine` installed as well (transformers, torch, gtts, pydub, etc.).

```bash
python -m venv .venv
.\.venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -r ../empathy_engine/requirements.txt
```

2. Start the server

```bash
uvicorn Backend.main:app --reload --port 8000
```

3. The frontend at `http://localhost:3000` can POST to `http://localhost:8000/generate-speech` with JSON `{ "text": "..." }` and will receive the WAV file in response.
