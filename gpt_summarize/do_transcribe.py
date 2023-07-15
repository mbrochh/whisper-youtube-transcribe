import os
import sys
import timeit

import whisper

from .local_settings import REPO_PATH, WHISPER_REPO_PATH
from .utils import get_filename


def transcribe(audio_file, output_path="files/transcripts"):
    """
    Transcribes the given audio file using the given model. Returns a tuple
    containing the transcription result and the elapsed time in seconds.

    """
    filename_only = get_filename(audio_file)
    audio_path = os.path.join(REPO_PATH, audio_file)
    model_path = os.path.join(WHISPER_REPO_PATH, "models/ggml-base.en.bin")

    # model = whisper.load_model(whisper_model)
    start_time = timeit.default_timer()
    cmd = (
        f"{WHISPER_REPO_PATH}/main"
        f' -f "{audio_path}"'
        f' --model "{model_path}"'
        f' --prompt "Hello."'
        f" --output-txt"
    )
    print("Transcribing with command: ", cmd)
    os.system(cmd)

    text_path = f"{output_path}/{filename_only}.txt"
    cmd = f'mv "{audio_path}.txt" "{text_path}"'
    print("Moving transcript with command: ", cmd)
    os.system(cmd)

    # result = model.transcribe(audio_file, verbose=True)
    end_time = timeit.default_timer()
    elapsed_time = int(end_time - start_time)
    return elapsed_time, text_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        elapsed_time, transcript_path = transcribe(audio_path)
        print(
            f"Audio has been transcribed in {elapsed_time} seconds. Path: {transcript_path}"
        )
    else:
        print(
            "Usage: python -m whisper_transcribe.whisper_transcribe.py"
            " <audio_path>"
        )
