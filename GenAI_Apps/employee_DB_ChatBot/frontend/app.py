from flask import Flask, render_template, request
import requests

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000/chat"

chat_history = []


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        question = request.form["question"]

        response = requests.post(
            FASTAPI_URL,
            json={"question": question}
        )

        data = response.json()

        answer = data.get("answer", "No answer generated.")
        sql = data.get("sql", "")

        chat_history.append(
            {
                "question": question,
                "answer": answer,
                "sql": sql
            }
        )

    return render_template(
        "chat.html",
        chat_history=chat_history
    )


if __name__ == "__main__":
    app.run(debug=True)