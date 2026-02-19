# 1. Use an official Python runtime as a parent image
FROM python:3.11-slim

# 2. Install system dependencies (FFmpeg is required for pydub)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# 3. Set the working directory in the container
WORKDIR /app

# 4. Copy requirements first to leverage Docker cache
COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Set PYTHONPATH so Python can see the 'empathy_engine' folder
ENV PYTHONPATH=/app

# 7. Start the application using the dynamic PORT provided by Railway
# We use 'sh -c' so that the $PORT variable is correctly expanded
CMD ["sh", "-c", "uvicorn Backend.main:app --host 0.0.0.0 --port ${PORT}"]