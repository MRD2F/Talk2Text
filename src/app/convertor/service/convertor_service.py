#import whisper

class ConvertorService:
    quality = "tiny"

    # # Load the Whisper model (choose: tiny, base, small, medium, large)
    # model = whisper.load_model(quality)    


    # print("Transcribing... this may take a few minutes for a 1h file.")

    # result = model.transcribe(audio_path)

    # # Print text
    # print(result["text"])

    # # Save transcript to file
    # with open(f"{output_file_name}.txt", "w", encoding="utf-8") as f:
    #     f.write(result["text"])
    @classmethod
    def create_text(cls, nome):
        pippo = "Ciao" + cls.quality

        return f"{pippo} {nome}"
