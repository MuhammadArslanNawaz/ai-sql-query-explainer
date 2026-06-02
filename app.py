from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
@app.route('/explain', methods=['POST'])
def explain():

    try:

        data = request.get_json()
        sql_query = data.get("query", "")

        prompt = f"""
Explain this SQL query in a clean structured format.

Include:
1. What the query does
2. Tables used
3. Conditions applied
4. Beginner-friendly explanation

SQL Query:

{sql_query}
"""

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "microsoft/phi-3-mini-128k-instruct:free",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        result = response.json()

        explanation = result["choices"][0]["message"]["content"]

        return jsonify({
            "explanation": explanation
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5001))
    )