from transcription import Transctiption

class TransctiptionService:
    data_dir = "data"
    input_file_name = f"{data_dir}/inputs/5846093734223028963.ogg"
    output_file_name = f"{data_dir}/outputs/5846093734223028963"
    model_id = "tiny"
    show_text = True
    text_preview_size = 10

    transctiption = Transctiption(model_id=model_id, input_file_name=input_file_name, 
                                  show_text=show_text, output_file_name=output_file_name,
                                  text_preview_size=text_preview_size)

    #transctiption.get_transcription()



