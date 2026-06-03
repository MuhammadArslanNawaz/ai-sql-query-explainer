from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/explain', methods=['POST'])
def explain():

    try:

        data = request.get_json()
        sql_query = data.get("query", "")

        prompt = f"""
Explain this SQL query in simple language.

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
                "model": "google/gemma-3-4b-it:free",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        result = response.json()

        print(result)

        if "choices" not in result:
            return jsonify({
                "explanation": str(result)
            })

        return jsonify({
            "explanation": result["choices"][0]["message"]["content"]
        })

    except Exception as e:

        return jsonify({
            "explanation": f"Error: {str(e)}"
        })