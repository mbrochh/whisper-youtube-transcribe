import sys

from .do_summarize import save_summaries, split_text, summarize_in_parallel
from .do_transcribe import save_transcript, transcribe
from .source_pdf import download_pdf, extract_text_from_pdf
from .source_website import download_website
from .source_youtube import convert_to_mp3, download_video
from .utils import get_filename


def call_openai(text_path, filename_without_filetype):
    chunks, total_token_count = split_text(text_path)
    print(
        f"Found {len(chunks)} chunks, totalling {total_token_count} tokens."
        " Calling OpenAI API now..."
    )
    summaries = summarize_in_parallel(chunks)
    summary_path, total_tokens_used, total_cost = save_summaries(
        summaries, filename_without_filetype
    )
    print(
        f"ALL DONE! Summary saved at {summary_path}."
        f" Total tokens used: {total_tokens_used}. Cost: {total_cost} USD."
    )


def process_youtube(url):
    """
    Downloads the given YouTube video, transcribes it, splits it into chunks,
    summarizes each chunk, and saves the summaries to a file.

    """
    print(f"Downloading audio for {url}...")
    movie_path = download_video(url)

    audio_path = convert_to_mp3(movie_path)

    filename_without_filetype = get_filename(audio_path)

    print(f"Transcribing {audio_path} (this will take a while)...")
    transcript, elapsed_time = transcribe(audio_path)
    text_path = save_transcript(transcript["text"], filename_without_filetype)
    print(f"Audio has been transcribed in {int(elapsed_time)} seconds")

    call_openai(text_path, filename_without_filetype)


def process_website(url):
    """
    Downloads the given website, splits it into chunks, summarizes each chunk,
    and saves the summaries to a file.

    """
    print(f"Downloading website {url}...")
    file_path, text = download_website(url)
    filename_without_filetype = get_filename(file_path)

    call_openai(file_path, filename_without_filetype)


def process_pdf(url, title):
    """
    Downloads the given PDF, splits it into chunks, summarizes each chunk,
    and saves the summaries to a file.

    """
    print(f"Downloading PDF from {url}...")
    file_path = download_pdf(url, title)
    filename_without_filetype = get_filename(file_path)

    print("Extracting text from PDF...")
    text_path = extract_text_from_pdf(file_path, filename_without_filetype)

    call_openai(text_path, filename_without_filetype)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        title = None
        try:
            title = sys.argv[2]
        except IndexError:
            pass

        if "youtube.com" in url:
            process_youtube(url)
            sys.exit(1)
        if title:
            process_pdf(url, title)
        else:
            process_website(url)
    else:
        print("Usage: python -m gpt_summarize.gpt_summarize <youtube_url>")
