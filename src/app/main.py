from flask import Flask, render_template, request
from app.convertor.service.convertor_service import ConvertorService


app = Flask(__name__)


@app.route("/")
def main():
    # text = ConvertorService.create_text()
    return render_template("main.html", person="enrico")


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    # Instantiate service
    convertor_service = ConvertorService(
        model_id="tiny",
        input_file_name=file.filename,  #  PATH to the saved file
        show_text=True,
        text_preview_size=100,
    )

    text = convertor_service.create_text()

    return f"<h1>{text}</h1>"

    # Leggi il contenuto del file in memoria
    # data = file.read()  # bytes
    # # oppure se è un testo: file_content = file.read().decode('utf-8')
    # return f"Dimensione del file: {len(data)} byte"
