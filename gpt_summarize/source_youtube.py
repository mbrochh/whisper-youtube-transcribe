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
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_")
    outtmpl = os.path.join(output_path, date_str + '%(title)s.%(ext)s')

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        output_file_path = ydl.prepare_filename(info_dict)
    
    original_path, original_filename = os.path.split(output_file_path)
    original_file_base, file_ext = os.path.splitext(original_filename)
    slugified_base = slugify(original_filename)
    new_file_path = os.path.join(
        output_path, f"{slugified_base}{file_ext.lower()}"
    )
    os.rename(output_file_path, new_file_path)
    return new_file_path


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
