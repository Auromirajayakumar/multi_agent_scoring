from sqlalchemy import Column, Integer, String, Float
from models.database import Base

class Evaluation(Base):
    __tablename__ = "evaluations"

    id = Column(Integer, primary_key=True, index=True)
    transcript = Column(String)
    score = Column(Float)
    feedback = Column(String)
    reasoning = Column(String)