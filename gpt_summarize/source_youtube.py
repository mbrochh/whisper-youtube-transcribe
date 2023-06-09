import datetime
import os
import sys

import yt_dlp

from .local_settings import FFMPEG_PATH
from .utils import slugify

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


def convert_to_mp3(path, output_path="files/audio/"):
    """
    Converts a mp4 file to a mp3 file. Returns the path to the mp3 file.

    """
    from moviepy.editor import AudioFileClip

    dir_path, filename = os.path.split(path)
    file_base, file_ext = os.path.splitext(filename)
    mp3_path = path.replace(file_ext, ".mp3")
    AudioFileClip(path).write_audiofile(mp3_path)
    os.remove(path)
    return mp3_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        movie_path = download_video(url)
        convert_to_mp3(movie_path)
    else:
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
