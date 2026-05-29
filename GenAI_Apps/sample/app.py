# ============================================================
# Install Required Packages
# ============================================================
# pip install google-genai python-dotenv

import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# ============================================================
# Function to Generate Response
# ============================================================
def generate(question):

    # Create Gemini Client
    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # Model Name
    model = "gemini-2.5-flash"

    # Generate Streaming Response
    response = client.models.generate_content_stream(
        model=model,
        contents=question
    )

    # Print streamed output
    for chunk in response:
        if chunk.text:
            print(chunk.text, end="")


# ============================================================
# Main Function
# ============================================================
if __name__ == "__main__":

    question = "What is Postman? I want to know about it in detail."

    generate(question)