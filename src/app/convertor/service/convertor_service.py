from convertor.service.transcription import Transcription


class ConvertorService:

    @classmethod
    def create_text(cls):
        # data_dir = "data"
        input_file_name = "./convertor/service/data/inputs/5846093734223028963.ogg"
        # output_file_name = "./data/outputs/5846093734223028963"
        model_id = "tiny"
        show_text = True
        text_preview_size = 10

        transcription = Transcription(
            model_id=model_id,
            input_file_name=input_file_name,
            show_text=show_text,
            text_preview_size=text_preview_size,
        )

        return transcription.get_transcription()
