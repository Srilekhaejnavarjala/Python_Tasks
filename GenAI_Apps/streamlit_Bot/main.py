from fastapi import FastAPI, HTTPException
from schemas import QuestionRequest, SummaryRequest
from gemini_service import ask_gemini, summarize_text

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(
    title="Gemini AI Assistant",
    description="AI Chat + Text Summarizer using FastAPI and Gemini",
    version="1.0"
)

# ============================================================
# Home Route
# ============================================================

@app.get("/", tags=["Home"])
def home():

    return {
        "status": "success",
        "message": "Gemini FastAPI App Running"
    }

# ============================================================
# Ask Route
# ============================================================

@app.post("/ask", tags=["AI Chat"])
def ask_question(data: QuestionRequest):

    try:

        answer = ask_gemini(data.question)

        return {
            "status": "success",
            "question": data.question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Error generating AI response: {str(e)}"
        )

# ============================================================
# Summarize Route
# ============================================================

@app.post("/summarize", tags=["Text Summarizer"])
def summarize(data: SummaryRequest):

    try:

        summary = summarize_text(data.text)

        return {
            "status": "success",
            "summary": summary
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Error generating summary: {str(e)}"
        )