from pydantic import BaseModel


class QuestionRequest(BaseModel):
    question: str

class SummaryRequest(BaseModel):
    text: str
