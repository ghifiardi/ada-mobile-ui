"""
Simplified Mock API Server for ADA Media Integrity Mobile UI Testing
This server provides the required endpoints for testing the mobile UI without full ML dependencies.
"""

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uuid
import time
import random

app = FastAPI(title="ADA Media Integrity Mock API", version="2.0")

# Enable CORS for mobile UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session storage
sessions = {}

class RealtimeStartRequest(BaseModel):
    mode: str = "realtime_balanced"
    stream_type: str = "video_audio"

class RealtimeStopRequest(BaseModel):
    session_id: str

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "ADA Media Integrity Mock API", "version": "2.0"}

@app.post("/analyze/realtime/start")
async def start_realtime(request: RealtimeStartRequest):
    """Start real-time analysis session"""
    session_id = str(uuid.uuid4())
    sessions[session_id] = {
        "mode": request.mode,
        "stream_type": request.stream_type,
        "start_time": time.time(),
        "frame_count": 0
    }

    return {
        "session_id": session_id,
        "status": "started",
        "mode": request.mode,
        "stream_type": request.stream_type
    }

@app.post("/analyze/realtime/chunk")
async def process_realtime_chunk(
    chunk: UploadFile = File(...),
    session_id: str = Form(...)
):
    """Process real-time video/audio chunk"""

    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")

    session = sessions[session_id]
    session["frame_count"] += 1

    # Mock analysis results
    is_authentic = random.random() > 0.3  # 70% chance of authentic
    confidence = random.uniform(0.75, 0.95) if is_authentic else random.uniform(0.60, 0.85)
    risk_score = random.uniform(5, 25) if is_authentic else random.uniform(40, 75)

    verdict = "authentic" if is_authentic else "suspicious" if risk_score < 60 else "synthetic"

    return {
        "session_id": session_id,
        "final_verdict": verdict,
        "confidence": confidence,
        "risk_score": risk_score,
        "timestamp": time.strftime("%H:%M:%S"),
        "deepfake_result": {
            "is_fake": not is_authentic,
            "risk_score": risk_score * 0.6,
            "confidence": confidence
        },
        "voice_result": {
            "is_clone": not is_authentic and random.random() > 0.5,
            "risk_score": risk_score * 0.4,
            "confidence": confidence
        }
    }

@app.post("/analyze/realtime/stop")
async def stop_realtime(request: RealtimeStopRequest):
    """Stop real-time analysis session"""

    if request.session_id in sessions:
        session = sessions.pop(request.session_id)
        duration = time.time() - session["start_time"]

        return {
            "session_id": request.session_id,
            "status": "stopped",
            "duration": duration,
            "frames_processed": session["frame_count"]
        }

    return {"session_id": request.session_id, "status": "not_found"}

@app.post("/analyze/upload/hybrid")
async def analyze_upload(
    file: UploadFile = File(...),
    mode: str = Form("hybrid")
):
    """Analyze uploaded media file"""

    # Simulate processing time
    await file.read()
    processing_time = random.uniform(2, 5)
    time.sleep(min(processing_time, 2))  # Cap at 2 seconds for demo

    # Mock analysis results
    is_authentic = random.random() > 0.4  # 60% chance of authentic
    confidence = random.uniform(0.75, 0.95) if is_authentic else random.uniform(0.65, 0.85)
    risk_score = random.uniform(5, 25) if is_authentic else random.uniform(45, 80)

    verdict = "authentic" if is_authentic else "suspicious" if risk_score < 60 else "synthetic"

    return {
        "final_verdict": verdict,
        "is_authentic": is_authentic,
        "confidence": confidence,
        "risk_score": risk_score,
        "processing_time": processing_time,
        "liveness_result": {
            "is_live": is_authentic,
            "pass_rate": random.uniform(0.7, 0.95) if is_authentic else random.uniform(0.3, 0.6),
            "challenges_passed": random.randint(4, 6) if is_authentic else random.randint(1, 3),
            "total_challenges": 6
        },
        "deepfake_result": {
            "is_fake": not is_authentic,
            "risk_score": risk_score * 0.6,
            "frames_analyzed": random.randint(30, 120),
            "suspicious_frames": 0 if is_authentic else random.randint(10, 50)
        },
        "voice_result": {
            "is_clone": not is_authentic and random.random() > 0.5,
            "risk_score": risk_score * 0.4,
            "confidence": confidence
        },
        "reasons": [
            f"Video quality: {'Good' if is_authentic else 'Suspicious artifacts detected'}",
            f"Liveness: {'Passed multiple challenges' if is_authentic else 'Failed liveness verification'}",
            f"Audio: {'Natural voice patterns' if is_authentic else 'Synthetic indicators found'}",
            f"Overall risk assessment: {verdict.upper()}"
        ],
        "mode": mode,
        "file_name": file.filename,
        "file_size": file.size if hasattr(file, 'size') else 0
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting ADA Media Integrity Mock API Server")
    print("📍 API URL: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("✨ This is a mock server for testing the mobile UI")
    print("")
    uvicorn.run(app, host="0.0.0.0", port=8000)
