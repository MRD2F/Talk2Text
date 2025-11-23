from flask import Flask, request
from convertor.service.convertor_service import ConvertorService

app = Flask(__name__)
@app.route("/")
def hello_world():
    name = request.args.get('name')
    text = ConvertorService.create_text(name)
    return f"<h1>{text}</h1>"