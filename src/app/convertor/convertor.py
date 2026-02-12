from app.convertor.transcription import Transcription


class Convertor:
    def __init__(self, model_id, input_file_name, show_text, text_preview_size):
        self.model_id = model_id
        self.input_file_name = input_file_name
        self.show_text = show_text
        self.text_preview_size = text_preview_size

    def create_text(self):
        transcription = Transcription(
            model_id=self.model_id,
            input_file_name=self.input_file_name,
            show_text=self.show_text,
            text_preview_size=self.text_preview_size,
        )

        return transcription.get_transcription()


if __name__ == "__main__":
    convertor_service = ConvertorService(
        model_id="tiny",
        input_file_name="./src/app/convertor/service/data/inputs/5846093734223028963.ogg",
        show_text=True,
        text_preview_size=100,
    )

    text = convertor_service.create_text()
