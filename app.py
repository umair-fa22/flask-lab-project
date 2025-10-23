from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/health')
def health():
    return "OK"

@app.route('/data', methods=['POST'])
def data():
    return jsonify({"message": "Data received"}), 200