# ============================================================
# 🚀 Flask Frontend for Gemini AI Workspace
# ============================================================

from flask import Flask, render_template, request
import requests

# ============================================================
# Flask App
# ============================================================

app = Flask(__name__)

# ============================================================
# FastAPI Backend URLs
# ============================================================

ASK_URL = "http://127.0.0.1:8000/ask"
SUMMARY_URL = "http://127.0.0.1:8000/summarize"

# ============================================================
# Single Page Route
# ============================================================

@app.route("/", methods=["GET", "POST"])
def home():

    response_text = None
    mode = "chat"

    if request.method == "POST":

        mode = request.form.get("mode")

        # ====================================================
        # ASK AI
        # ====================================================

        if mode == "chat":

            question = request.form.get("question")

            try:

                response = requests.post(
                    ASK_URL,
                    json={
                        "question": question
                    }
                )

                data = response.json()

                response_text = data.get(
                    "answer",
                    "No response generated."
                )

            except Exception as e:

                response_text = f"Error: {str(e)}"

        # ====================================================
        # AI SUMMARY
        # ====================================================

        elif mode == "summary":

            article = request.form.get("article")

            try:

                response = requests.post(
                    SUMMARY_URL,
                    json={
                        "text": article
                    }
                )

                data = response.json()

                response_text = data.get(
                    "summary",
                    "No summary generated."
                )

            except Exception as e:

                response_text = f"Error: {str(e)}"

    return render_template(
        "index.html",
        response=response_text,
        mode=mode
    )

# ============================================================
# Run Flask App
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )