from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/explain', methods=['POST'])
def explain_sql():

    try:

        data = request.json

        sql_query = data.get('query')

        prompt = f"""
        Explain this SQL query in simple English:
        Include:
        1. What the query does
        2. Which table is used
        3. Conditions applied
        4. Simple explanation for beginners
        SQL Query:
        {sql_query}
        """

        response = ollama.chat(

            model='phi3',

            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        explanation = response['message']['content']

        return jsonify({
            "explanation": explanation
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)