from flask import Flask, jsonify, request
from main import chat_api
app = Flask(__name__)


@app.route("/")
def hello_world():
    return chat_api()