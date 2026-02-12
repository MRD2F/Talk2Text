from convertor.routes import upload_bp
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return "Talk2Text"


# Registrazione dei Blueprint
app.register_blueprint(upload_bp)
