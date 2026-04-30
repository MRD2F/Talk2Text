from flask import Flask, render_template

from app.convertor.routes import upload_bp

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024  # 500MB
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
app.config["MAX_CONTENT_PATH"] = None


@app.route("/")
def main():
    return render_template("main.html")


# Registrazione dei Blueprint
app.register_blueprint(upload_bp)
