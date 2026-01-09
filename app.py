from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load dataset
with open("dataset.txt", "r", encoding="utf-8") as f:
    data = [line.strip().lower() for line in f if line.strip()]

@app.route("/")
def home():
    return "AI Knowledge Base Backend is Running"

@app.route("/ask", methods=["POST"])
def ask():
    q = request.json.get("question", "").lower()

    for line in data:
        if any(word in line for word in q.split()):
            return jsonify({"answer": line})

    return jsonify({"answer": "Answer not available in the dataset."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
