import datetime
import os
import subprocess
import sys

import yt_dlp

from .local_settings import FFMPEG_PATH, REPO_PATH
from .utils import get_filename, slugify

os.environ["IMAGEIO_FFMPEG_EXE"] = FFMPEG_PATH


def download_video(url, output_path="files/audio/"):
    """
    Downloads a YouTube video and saves it to the given output
    path. Returns the path to the downloaded file and the filename without the
    file extension.

    """
    output_filename_result = {}

    def rename_file(info_dict, output_filename_result):
        """
        Renames the downloaded file to a slugified version of the original.

        """
        if info_dict["status"] != "finished":
            return None

        original_file_path = info_dict["filename"]
        original_path, original_filename = os.path.split(original_file_path)
        original_file_base, file_ext = os.path.splitext(original_filename)

        new_filename = slugify(original_filename)
        date_str = datetime.datetime.now().strftime("%Y-%m-%d_")
        new_filename = date_str + new_filename

        new_file_path = os.path.join(
            output_path, f"{new_filename}{file_ext.lower()}"
        )

        output_filename_result["file_path"] = new_file_path
        os.rename(original_file_path, new_file_path)

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "progress_hooks": [lambda d: rename_file(d, output_filename_result)],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    output_file_path = output_filename_result["file_path"]
    return output_file_path


def convert_to_wav(movie_path, output_path="files/audio/"):
    """
    Converts a mp4 file to a wav file. Returns the path to the mp3 file.

    """
    filename = get_filename(movie_path)
    audio_path = os.path.join(REPO_PATH, movie_path)
    wav_path = os.path.join(REPO_PATH, output_path, f"{filename}.wav")
    cmd = (
        f'ffmpeg -y -i "{audio_path}" -ar 16000 -ac 1'
        f' -c:a pcm_s16le "{wav_path}"'
    )
    print("Converting to wav with command: ", cmd)
    return_code = subprocess.call(cmd, shell=True)
    print("ffmpeg return code: ", return_code)
    os.remove(audio_path)
    return wav_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        movie_path = download_video(url)
        wav_path = convert_to_wav(movie_path)
        print("Audio downloaded to: ", wav_path)
    else:
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
