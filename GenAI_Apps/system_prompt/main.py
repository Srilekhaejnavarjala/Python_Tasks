# ============================================================
# Gemini Learning Assistant Backend
# ============================================================

import os
from google import genai
from dotenv import load_dotenv

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Gemini Client
# ============================================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ============================================================
# Check Question Relevance
# ============================================================

def is_python_related(question: str) -> bool:

    prompt = f"""
    You are a strict classifier.

    Return ONLY YES or NO.

    Return YES only if the question is clearly related to:
    - Python
    - Python Programming
    - FastAPI
    - Flask
    - AI
    - Machine Learning
    - Deep Learning
    - Data Science

    Return NO for:
    - Greetings
    - Random text
    - Gibberish
    - Personal conversation
    - Non-technical topics

    Question:
    {question}

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "temperature": 0
        }
    )

    answer = response.text.strip().upper()

    return answer == "YES"

# ============================================================
# Generate Response
# ============================================================

def generate_answer(question: str):

    if not is_python_related(question):
        return (
            "⚠️ I'm currently designed to provide responses only for "
            "Python, FastAPI, Flask, AI/ML, Data Science, and related "
            "technical learning queries."
        )

    system_prompt = """
    You are an AI Learning Assistant.

    Your purpose is to help users learn:

    - Python
    - FastAPI
    - Flask
    - APIs
    - Machine Learning
    - Deep Learning
    - Data Science
    - Software Development

    Rules:

    - Be beginner friendly.
    - Explain concepts clearly.
    - Use examples whenever helpful.
    - Keep answers structured.
    - Do not answer unrelated questions.
    """

    full_prompt = f"""
    {system_prompt}

    User Question:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=full_prompt
    )

    return response.text