from fastapi import FastAPI
from pydantic import BaseModel

from backend.database import get_connection
from backend.sql_generator import generate_sql
from backend.answer_generator import generate_answer

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    question = request.question

    sql = generate_sql(question)

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    try:

        cursor.execute(sql)

        result = cursor.fetchall()

        answer = generate_answer(
            question,
            result
        )

        # Save history
        history_cursor = conn.cursor()

        history_cursor.execute(
            """
            INSERT INTO query_history
            (
                question,
                generated_sql,
                answer,
                execution_status
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                question,
                sql,
                answer,
                "SUCCESS"
            )
        )

        conn.commit()

        history_cursor.close()

        return {
            "answer": answer
        }

    except Exception as e:

        error_message = str(e)

        # Save failed queries
        history_cursor = conn.cursor()

        history_cursor.execute(
            """
            INSERT INTO query_history
            (
                question,
                generated_sql,
                answer,
                execution_status
            )
            VALUES (%s,%s,%s,%s)
            """,
            (
                question,
                sql,
                error_message,
                "FAILED"
            )
        )

        conn.commit()

        history_cursor.close()

        return {
            "error": error_message
        }

    finally:

        cursor.close()
        conn.close()