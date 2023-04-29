import os
import re
import sys

import yt_dlp
from moviepy.editor import AudioFileClip


def slugify(value):
    """
    Converts a file path to a slugified version. Only changes the filename at
    the end of the path, not the path itself. For example, if the input path is
    "files/audio/My Video.mp4", the output path will be
    "files/audio/my_video.mp4".

    """
    value = re.sub(r"[^\w\s-]", "", value).strip().lower()
    value = re.sub(r"[-\s]+", "_", value)
    return re.sub(r"[^\x00-\x7f]", "", value)


def download_audio(url, output_path="files/audio/"):
    """
    Downloads the audio from a YouTube video and saves it to the given output
    path. Returns the path to the downloaded file.

    """
    output_filename_result = {}

    def get_output_filename(info_dict, output_filename_result):
        file_path = info_dict["filename"]
        path, filename = os.path.split(file_path)
        file_base, file_ext = os.path.splitext(filename)
        file_extension = file_ext
        filename_without_filetype = slugify(file_base)
        output_filename = os.path.join(
            output_path, filename_without_filetype + file_extension
        )
        output_filename_result[
            "filename_without_filetype"
        ] = filename_without_filetype
        output_filename_result["file_extension"] = file_extension
        output_filename_result["output_filename"] = output_filename
        return output_filename

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "progress_hooks": [
            lambda d: os.rename(
                d["filename"], get_output_filename(d, output_filename_result)
            )
            if d["status"] == "finished"
            else None
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    filename_without_filetype = output_filename_result[
        "filename_without_filetype"
    ]
    output_filename = output_filename_result["output_filename"]
    return output_filename, filename_without_filetype


def convert_to_mp3(path, output_path="files/audio/"):
    """
    Converts a mp4 file to a mp3 file. Returns the path to the mp3 file.

    """
    dir_path, filename = os.path.split(path)
    file_base, file_ext = os.path.splitext(filename)
    mp3_path = path.replace(file_ext, ".mp3")
    AudioFileClip(path).write_audiofile(mp3_path)
    os.remove(path)
    return mp3_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        movie_path = download_audio(url)
        convert_to_mp3(movie_path)
    else:
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
