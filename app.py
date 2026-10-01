from flask import Flask, request, jsonify

app = Flask(__name__)

latest_message = ""

@app.route("/")
def home():
    return "Flask message server is running!"

@app.route("/send", methods=["POST"])
def send():
    global latest_message

    data = request.get_json()
    latest_message = data.get("message", "")

    return jsonify({
        "ok": True,
        "message": latest_message
    })

@app.route("/latest", methods=["GET"])
def latest():
    return jsonify({
        "message": latest_message
    })
