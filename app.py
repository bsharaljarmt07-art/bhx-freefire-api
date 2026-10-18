
from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "name": "BHX API",
        "status": "online",
        "version": "1.0"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/info")
def player_info():
    uid = request.args.get("uid", "").strip()

    if not re.fullmatch(r"[0-9]{5,20}", uid):
        return jsonify({
            "status": "error",
            "message": "Invalid UID"
        }), 400

    return jsonify({
        "status": "pending",
        "uid": uid,
        "message": "Player data source is not configured"
    }), 503

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
