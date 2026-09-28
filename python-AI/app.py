from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello!!!! Python application is running.",
        "version": os.getenv("APP_VERSION", "local"),
        "environment": os.getenv("ENVIRONMENT", "development")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/info")
def info():
    return jsonify({
        "application": "python-AI-DEMO-CI",
        "version": os.getenv("APP_VERSION", "local"),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "hostname": os.getenv("HOSTNAME", "local")
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", 9090))

    app.run(
        host="0.0.0.0",
        port=port
    )