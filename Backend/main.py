from pathlib import Path
import sys
import os
import nltk
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Ensure the project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

# 1. LIFESPAN: This handles heavy tasks AFTER the port is bound
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This prevents Render's "Port Scan Timeout"
    print("Starting up: Downloading NLTK data...")
    try:
        nltk.download("punkt")
        nltk.download("punkt_tab") # Fixes the 500 error for NLTK 3.9+
        print("NLTK data downloaded successfully.")
        
        # Pre-initialize the AI model so the first request is fast
        from empathy_engine.emotion_detector import _init_detector
        _init_detector()
        print("Emotion detector model loaded.")
    except Exception as e:
        print(f"Startup warning: {e}")
    
    yield
    # Shutdown logic goes here if needed

# 2. APP INITIALIZATION
app = FastAPI(title="Empathy AI Backend", version="0.1", lifespan=lifespan)

try:
    from empathy_engine.pipeline import run_pipeline
except Exception as e:
    raise RuntimeError(f"Failed to import empathy_engine.pipeline: {e}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "https://empathy-ai-3iiy.onrender.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-speech")
async def generate_speech(request: Request):
    payload = await request.json()
    text = payload.get("text") if isinstance(payload, dict) else None
    
    if not text or not isinstance(text, str) or not text.strip():
        raise HTTPException(status_code=400, detail="'text' must be a non-empty string")

    try:
        # Now run_pipeline won't crash because NLTK is already there
        result = run_pipeline(text)
    except Exception as e:
        # Logs the actual error to Render console for you to see
        print(f"Error in pipeline: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate speech: {e}")

    out_path = result.get("output_audio_path")
    if not out_path or not os.path.exists(out_path):
        raise HTTPException(status_code=500, detail="Audio file was not created")

    return FileResponse(path=out_path, media_type="audio/wav", filename=Path(out_path).name)

if __name__ == "__main__":
    import uvicorn
    import os

    # 1. Get the port from Railway's environment variable
    # 2. Default to 8000 ONLY if we are running locally
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(app, host="0.0.0.0", port=port)