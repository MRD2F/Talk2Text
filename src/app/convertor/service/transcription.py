import whisper

class Transctiption:
    def __init__(self, model_id, input_file_name="", show_text=False, 
                 output_file_name="", text_preview_size=None, 
                 language="english"):
        self.model_id = model_id
        self.input_file_name = input_file_name
        self.show_text = show_text
        self.output_file_name = output_file_name
        self.text_preview_size = text_preview_size
        self.language = language

        ########## Sanity checks for whisper model use #########
        self.whisper_allowed_extensions = ['flac', 'm4a', 'mp3', 'mp4', 'mpeg', 'mpga', 'oga', 'ogg', 'wav', 'webm']
        self.whisper_model_ids = ["tiny", "base", "small", "medium", "large", "turbo"]
    
        # The default setting (which selects the turbo model) works well for transcribing English. 
        # However, the turbo model is not trained for translation tasks. 
        # If you need to translate non-English speech into English, use one of the 
        # multilingual models (tiny, base, small, medium, large) instead of turbo.

        self.whisper_model_ids_english_only = ["tiny.en", "base.en", "small.en", "medium.en"]
        self._check_file_extension()
        self._check_whisper_model_id()

    def _check_file_extension(self):
        ext = self.input_file_name.rsplit(".", 1)[-1].lower()

        if ext not in self.whisper_allowed_extensions:
            allowed = ", ".join(self.whisper_allowed_extensions)
            raise ValueError(
                f"Invalid file format: .{ext}\n"
                f"Allowed formats are: {allowed}"
            )
        
    def _check_whisper_model_id(self):
        if self.model_id not in self.whisper_model_ids:
            allowed = ", ".join(self.whisper_model_ids)
            raise ValueError(
                f"Invalid model ID selection: {self.model_id}\n"
                f"Allowed formats are: {allowed}"
            )

    def _get_model(self):
        model = whisper.load_model(self.model_id)   
        return model 
    
    def save_transcription(self, text, output_file_name=""):
        file_name = self.output_file_name if not output_file_name else output_file_name
        with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
            f.write(text)

    
    def get_transcription(self):
        #, input_file_name = "", show_text=False, output_file_name=""):
        model = self._get_model()
        print(f"Using as requested model {self.model_id}.")

    
        print(f"Transcribing file {self.input_file_name}... this may take a few minutes depening of the file size.")
        # load audio and pad/trim it to fit 30 seconds
        # audio = whisper.load_audio("audio.mp3")
        # audio = whisper.pad_or_trim(audio)

        # detect the spoken language
        # _, probs = model.detect_language(mel)
        # print(f"Detected language: {max(probs, key=probs.get)}")


        result = model.transcribe(self.input_file_name, )

        if self.show_text | show_text:
            if self.text_preview_size:
                print(result['text'][:self.text_preview_size])
            else:
                print(result["text"])

        if (len(self.output_file_name) > 0) |(len(self.output_file_name) > 0):
            file_name = self.output_file_name if not output_file_name else output_file_name
            self.save_transcription(result["text"], file_name)
            print(f"Saved transcription as: {file_name}.")


if __name__ == "__main__":
    
    data_dir = "data"
    input_file_name = f"{data_dir}/inputs/5846093734223028963.ogg"
    output_file_name = f"{data_dir}/outputs/5846093734223028963"


    model_id = "tiny"
    show_text = True
    text_preview_size = 10

    transctiption_service = Transctiption(model_id=model_id, input_file_name=input_file_name, 
                                                 show_text=show_text, output_file_name=output_file_name,
                                                 text_preview_size=text_preview_size)

    transctiption_service.get_transcription()



