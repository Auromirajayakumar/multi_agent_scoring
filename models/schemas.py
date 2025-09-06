from pydantic import BaseModel
from typing import List
from datetime import datetime

class EvaluationOutput(BaseModel):
    score: float
    feedback: str
    reasoning: str

class EvaluationRecord(BaseModel):
    id: int
    transcript: str
    score: float
    feedback: str
    reasoning: str
    timestamp: datetime

    class Config:
        from_attributes = True