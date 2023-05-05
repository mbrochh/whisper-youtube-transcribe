import os
import sys

import yt_dlp


def download_video(url):
    """
    Downloads a YouTube video and saves it to files/audio.

    Returns the path to the downloaded file.

    """
    output_filename_result = {}

    def get_filename(info_dict):
        """
        Gets the filename of the downloaded file.

        """
        if info_dict["status"] != "finished":
            return None

        filename = info_dict["filename"]
        filename, ext = os.path.splitext(filename)
        output_filename_result["file_path"] = filename + ".mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "files/audio/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "progress_hooks": [get_filename],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    output_file_path = output_filename_result["file_path"]
    return output_file_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        audio_path = download_video(url)
        print(f"Download complete: {audio_path}")
    else:
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
        print("Usage: python -m gpt_summarize.source_youtube.py <youtube_url>")
