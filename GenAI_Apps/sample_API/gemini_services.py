import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(question: str):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    return response.text

def summarize_text(text: str):
    prompt = f"""
    Read the following article carefully. Analyze it properly
    and provide a short and clear summary.and

    Article:
    {text}
    """
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )

    return response.text