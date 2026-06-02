from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
@app.route('/explain', methods=['POST'])
def explain():

    return jsonify({
        "explanation": "Railway backend reached successfully"
    })