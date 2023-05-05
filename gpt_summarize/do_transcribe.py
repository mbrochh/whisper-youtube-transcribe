import os
import sys

import whisper


def transcribe(audio_path):
    model = whisper.load_model("small.en")
    result = model.transcribe(audio_path, verbose=True)
    transcript = str(result["text"])

    filename = os.path.splitext(os.path.basename(audio_path))[0]
    text_path = os.path.join("files/transcripts", f"{filename}.txt")
    with open(text_path, "w") as f:
        f.write(transcript)

    return text_path, transcript


if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        text_path, transcript = transcribe(audio_path)
        print(f"Transcript saved to: {text_path}.")
    else:
        print("Usage: python -m gpt_summarize.do_transcribe.py <audio_path>")
