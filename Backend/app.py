from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to FinRelief AI Backend",
        "status": "Running Successfully"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "backend": "Flask",
        "project": "FinRelief AI"
    })

if __name__ == "__main__":
    app.run(debug=True)