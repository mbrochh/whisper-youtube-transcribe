import os
import sys
import timeit

import whisper


def transcribe(audio_file, whisper_model="small.en"):
    """
    Transcribes the given audio file using the given model. Returns a tuple
    containing the transcription result and the elapsed time in seconds.

    """
    model = whisper.load_model(whisper_model)
    start_time = timeit.default_timer()
    result = model.transcribe(audio_file, verbose=True)
    end_time = timeit.default_timer()
    elapsed_time = int(end_time - start_time)
    return result, elapsed_time


def save_transcript(
    text, filename_without_filetype, output_path="files/transcripts"
):
    """
    Saves the given text to a file with the given filename in the given
    output_path.

    Returns the path to the saved file.

    """
    text_path = os.path.join(output_path, f"{filename_without_filetype}.txt")
    with open(text_path, "w") as f:
        f.write(text)
    return text_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        result, elapsed_time = transcribe(audio_path)
        save_transcript(result["text"], audio_path)
        print(f"Audio has been transcribed in {elapsed_time} seconds")
    else:
        print(
            "Usage: python -m whisper_transcribe.whisper_transcribe.py"
            " <audio_path>"
        )
