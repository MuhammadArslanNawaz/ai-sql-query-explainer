from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/explain', methods=['POST'])
def explain():

    return jsonify({
        "explanation": "Backend deployment successful!"
    })
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)