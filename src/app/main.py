from flask import Flask, render_template

from app.convertor.routes import upload_bp

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


# Registrazione dei Blueprint
app.register_blueprint(upload_bp)
