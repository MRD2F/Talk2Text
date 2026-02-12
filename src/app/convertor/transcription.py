import os
import tempfile

import whisper


class Transcription:
    whisper_allowed_extensions = [
        "flac",
        "m4a",
        "mp3",
        "mp4",
        "mpeg",
        "mpga",
        "oga",
        "ogg",
        "wav",
        "webm",
    ]

    whisper_model_ids = ["tiny", "base", "small", "medium", "large", "turbo"]

    def __init__(
        self,
        file_storage,
        model_id="tiny",
        show_text=False,
        language="english",
        test_mode=False,
        text_preview_size=None,
        output_file_name="",
    ):
        self.file_storage = file_storage
        self.model_id = model_id
        self.show_text = show_text
        self.language = language
        self.test_mode = test_mode
        self.text_preview_size = text_preview_size
        self.output_file_name = output_file_name
        self._check_file_extension()
        self._check_whisper_model_id()

    def _check_file_extension(self):
        filename = self.file_storage.filename
        ext = filename.rsplit(".", 1)[-1].lower()

        if ext not in self.whisper_allowed_extensions:
            raise ValueError(f"Invalid file format: .{ext}")

    def _check_whisper_model_id(self):
        if self.model_id not in self.whisper_model_ids:
            raise ValueError(f"Invalid model ID selection: {self.model_id}")

    def _get_model(self):
        return whisper.load_model(self.model_id)

    def _save_transcription(self, text, output_file_name=""):
        file_name = self.output_file_name if not output_file_name else output_file_name
        with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
            f.write(text)

    def get_transcription(self):
        model = self._get_model()

        # Salvataggio temporaneo
        with tempfile.NamedTemporaryFile(delete=False, suffix=".tmp") as tmp:
            self.file_storage.save(tmp.name)
            temp_path = tmp.name

        try:
            result = model.transcribe(temp_path, fp16=False)

            if self.show_text:
                if self.text_preview_size:
                    print(result["text"][: self.text_preview_size])
                else:
                    print(result["text"])
            if self.test_mode:
                self._save_transcription(result["text"])

            return result["text"]

        finally:
            os.remove(temp_path)
