import os
from google import genai
from dotenv import load_dotenv

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Get Gemini API Key
# ============================================================

API_KEY = os.getenv("GEMINI_API_KEY")

# Debugging
print("Loaded API Key:", API_KEY)

# ============================================================
# Validate API Key
# ============================================================

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ============================================================
# Create Gemini Client
# ============================================================

client = genai.Client(
    api_key=API_KEY
)

# ============================================================
# Ask Gemini Function
# ============================================================

def ask_gemini(question: str):

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=question
        )

        return response.text

    except Exception as e:

        print("Error in ask_gemini():", e)

        return f"Error: {str(e)}"

# ============================================================
# Summarize Text Function
# ============================================================

def summarize_text(text: str):

    try:

        prompt = f"""
        Read the following article carefully.
        Analyze it properly and provide a short, clear summary.

        Article:
        {text}
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        print("Error in summarize_text():", e)

        return f"Error: {str(e)}"