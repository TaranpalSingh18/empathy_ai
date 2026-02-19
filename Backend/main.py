from pathlib import Path
import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from fastapi.responses import FileResponse

# Ensure the project root is on sys.path so we can import empathy_engine
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from empathy_engine.pipeline import run_pipeline
except Exception as e:
    # Provide a clearer error if imports fail
    raise RuntimeError(f"Failed to import empathy_engine.pipeline: {e}")

app = FastAPI(title="Empathy AI Backend", version="0.1")

# Allow the frontend running on localhost:3000 to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/generate-speech")
async def generate_speech(request: Request):
    """Accepts JSON {"text": "..."} and returns the generated WAV file.

    The call is synchronous: it will wait for the model to generate the file
    and then return the WAV as a FileResponse.
    """
    payload = await request.json()
    text = payload.get("text") if isinstance(payload, dict) else None
    if not text or not isinstance(text, str) or not text.strip():
        raise HTTPException(status_code=400, detail="'text' must be a non-empty string")

    # Run the existing empathy_engine pipeline; it returns a dict including output_audio_path
    try:
        result = run_pipeline(text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate speech: {e}")

    out_path = result.get("output_audio_path")
    if not out_path or not os.path.exists(out_path):
        raise HTTPException(status_code=500, detail="Audio file was not created")

    # Return the file directly to the client
    return FileResponse(path=out_path, media_type="audio/wav", filename=Path(out_path).name)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
