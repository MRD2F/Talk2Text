def test_imports():
    import whisper
    assert True

def test_imports_modules():
    from src.app.convertor.service.transcription import Transctiption
    assert True

def test_transcription_text():
    from src.app.convertor.service.transcription import Transctiption
    data_dir = "data"
    input_file_name = f"{data_dir}/inputs/5846093734223028963.ogg"
    output_file_name = f"{data_dir}/outputs/5846093734223028963"
    model_id = "tiny"
    show_text = True
    text_preview_size = 10

    transcription_service = Transctiption(model_id=model_id, input_file_name=input_file_name, 
                                          show_text=show_text, output_file_name=output_file_name,
                                          text_preview_size=text_preview_size)

    assert transcription_service._get_model() is not None
    assert transcription_service._check_file_extension() is True
    assert transcription_service._check_whisper_model_id() is True


def test_load_file_success():
    import tempfile
    from src.app.convertor.service.transcription import Transctiption

    with tempfile.NamedTemporaryFile(suffix=".ogg") as tmp:
        transcription_service = Transctiption(input_file_name=tmp.name)
        assert transcription_service.load_file(tmp.name) == tmp.name
    
# def test_validate_extension_allowed():
#     from src.app.convertor.service.transcription import Transctiption

#     data_dir = "data"
#     model_id = "tiny"
#     input_file_name = f"{data_dir}/inputs/5846093734223028963.ogg"
#     transcription_service = Transctiption(model_id=model_id, input_file_name=input_file_name, 
#                                           show_text="", output_file_name="",
#                                           text_preview_size="")

#     assert transcription_service._check_file_extension() is True
