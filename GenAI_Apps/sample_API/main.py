from fastapi import FastAPI
from schemas import QuestionRequest, SummaryRequest
from gemini_services import ask_gemini,summarize_text

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Gemini FastAPI App Running"
    }


@app.post("/ask")
def ask_question(data: QuestionRequest):

    answer = ask_gemini(data.question)

    return {
        "question": data.question,
        "answer": answer
    }

@app.post("/summarize")
def summarize(data: SummaryRequest):
    summary = summarize_text(data.text)

    return {
        "summary": summary
    }
