from fastapi import FastAPI, UploadFile, File
from typing import Optional, List
from models.schemas import EvaluationOutput, EvaluationRecord
from models.database import Base, engine, SessionLocal
from models.tables import Evaluation
from agents.orchestrator import orchestrate
from utils.audio_utils import transcribe_audio
from utils.document_utils import extract_document_text

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/evaluate", response_model=EvaluationOutput)
async def evaluate(text: Optional[str] = None, audio: Optional[UploadFile] = File(None)):
    if audio:
        audio_path = f"temp_{audio.filename}"
        with open(audio_path, "wb") as f:
            f.write(await audio.read())
        transcript = transcribe_audio(audio_path)
    else:
        transcript = text

    result = orchestrate(transcript)

    db = SessionLocal()
    record = Evaluation(
        transcript=transcript,
        score=result["score"],
        feedback=result["feedback"],
        reasoning=result["reasoning"]
    )
    db.add(record)
    db.commit()
    db.close()

    return EvaluationOutput(**result)

@app.post("/evaluate-doc", response_model=EvaluationOutput)
async def evaluate_document(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())

    transcript = extract_document_text(file_path)
    result = orchestrate(transcript)

    db = SessionLocal()
    record = Evaluation(
        transcript=transcript,
        score=result["score"],
        feedback=result["feedback"],
        reasoning=result["reasoning"]
    )
    db.add(record)
    db.commit()
    db.close()

    return EvaluationOutput(**result)

@app.get("/history", response_model=List[EvaluationRecord])
def get_history():
    db = SessionLocal()
    records = db.query(Evaluation).order_by(Evaluation.id.desc()).limit(20).all()
    db.close()
    return records