import os

from app.convertor.transcription import Transcription


class FileService:
    def __init__(self, allowed_extensions, max_size_mb, model, language):
        self.allowed_extensions = allowed_extensions
        self.max_size_mb = max_size_mb
        self.max_size_bytes = max_size_mb * 1024 * 1024
        self.model = model
        self.language = language

    def _allowed_extension(self, filename):
        ext = os.path.splitext(filename)[1].lower().replace(".", "")
        return ext in self.allowed_extensions

    def _allowed_size(self, file):
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0)
        return size <= self.max_size_bytes

    def validate(self, file):
        if not file:
            return {"error": "Missing file"}, 400

        # Controllo filename
        if not file.filename:
            return {"error": "Invalid filename"}, 400

        # Controllo estensione
        if not self._allowed_extension(file.filename):
            return {"error": "File extension not allowed"}, 400

        # Controllo MIME dichiarato
        if not file.mimetype.startswith("audio/"):
            return {"error": "File is not an audio type"}, 400

        # Controllo dimensione
        if not self._allowed_size(file):
            return {"error": f"File exceeds {self.max_size_mb} MB"}, 400

        return None

    def convert(self, file):
        error = self.validate(file)

        if error:
            return error

        try:
            transcription = Transcription(
                file_storage=file, model_id=self.model, language=self.language
            )
            text = transcription.get_transcription()
            return {
                "message": "File converted successfully",
                "transcription": text,
            }, 200

        except Exception as e:
            return {"error": str(e)}, 400
