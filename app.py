from flask import Flask, request

app = Flask(__name__)

@app.route('/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get("message")
    print(f"Received message: {message}")
    return "Message received", 200

@app.route('/')
def home():
    return "Cloud is running!", 200
