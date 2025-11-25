from flask import Flask, request
from convertor.service.convertor_service import ConvertorService

app = Flask(__name__)
@app.route("/")
def hello_world():
    text = ConvertorService.create_text()
    return f"<h1>{text}</h1>"