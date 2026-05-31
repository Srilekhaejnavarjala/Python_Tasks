import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_sql(question):

    prompt = f"""
You are an expert SQL developer.

Database Schema:

employees(
id,
name,
age,
email,
phone,
designation,
department_id
)

departments(
id,
name,
location
)

attendance(
id,
employee_id,
date,
status
)

salaries(
id,
employee_id,
salary,
bonus
)

Generate ONLY SQL query.

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")

    return sql.strip()