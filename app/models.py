from pydantic import BaseModel
from typing import List

class QuestionRequest(BaseModel):
    session_id: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    session_id: str

class HistoryResponse(BaseModel):
    session_id: str
    history: List[str]