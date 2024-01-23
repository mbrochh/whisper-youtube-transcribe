import argparse
import sys

from .do_summarize import save_summaries, split_text, summarize_in_parallel
from .do_transcribe import transcribe
from .source_pdf import download_pdf, extract_text_from_pdf
from .source_website import download_website
from .source_youtube import convert_to_wav, download_video
from .utils import get_filename


def create_logseq_note(
    summary_path=None, 
    source=None, 
    title=None, 
    authors=None, 
    total_tokens_used=None, 
    total_cost=None
):
    """
    Takes the bullet point summary and formats it so that it becomes a logseq
    note.

    """
    if not summary_path or not source or not title or not authors:
        raise ValueError(
            "Please provide summary_path, source, title and authors"
        )

    with open(summary_path, "r") as f:
        lines = f.readlines()

    formatted_lines = ["    " + line for line in lines]

    logseq_note_path = summary_path.replace("files/summaries", "files/logseq")

    with open(logseq_note_path, "w") as f:
        f.write(f"source:: {source}\n")
        f.write(f"authors:: {authors}\n")
        f.write(f"gpt_token_count:: {total_tokens_used}\n")
        f.write(f"summary_cost:: {total_cost}\n")
        f.write(f"- summarized [[{title}]]")
        f.write("\n- [[summary]]\n")
        f.writelines(formatted_lines)

    print(f"Logseq note saved at {logseq_note_path}")


def call_openai(text_path=None, source=None, title=None, authors=None):
    filename_only = get_filename(text_path)

    chunks, total_token_count = split_text(text_path=text_path, title=title)
    print(
        f"Found {len(chunks)} chunks, totalling {total_token_count} tokens."
        " Calling OpenAI API now..."
    )
    summaries = summarize_in_parallel(chunks)
    summary_path, total_tokens_used, total_cost = save_summaries(
        summaries, filename_only
    )
    print(
        f"Summary saved at {summary_path}."
        f" Total tokens used: {total_tokens_used}. Cost: {total_cost} USD."
    )
    return summary_path, total_tokens_used, total_cost


def process_youtube(url=None, title=None, authors=None):
    """
    Downloads the given YouTube video, transcribes it, splits it into chunks,
    summarizes each chunk, and saves the summaries to a file.

    :url: The URL of the YouTube video to be processed.
    :title: The title of the YouTube video.
    :authors: The authors of the YouTube video.

    """
    if not url or not title or not authors:
        raise ValueError("Please provide url, title and authors.")

    print(f"Downloading audio for {url}...")
    movie_path = download_video(url)
    print(f'Audio downloaded to: "{movie_path}"')
    audio_path = convert_to_wav(movie_path)
    print(f"Transcribing {audio_path} (this will take a while)...")
    elapsed_time, transcript_path = transcribe(audio_path)
    print(f"Audio has been transcribed in {int(elapsed_time)} seconds")
    summary_path, total_tokens_used, total_cost = call_openai(
        text_path=transcript_path, source=url, title=title, authors=authors
    )
    create_logseq_note(
        summary_path=summary_path, 
        source=url, 
        title=title, 
        authors=authors, 
        total_tokens_used=total_tokens_used, 
        total_cost=total_cost,
    )
    print("End of job for source: youtube")


def process_website(url=None, title=None, authors=None):
    """
    Downloads the given website, splits it into chunks, summarizes each chunk,
    and saves the summaries to a file.

    """
    if not url or not title or not authors:
        raise ValueError("Please provide url, title and authors.")

    print(f"Downloading website {url}...")
    file_path, text = download_website(url, title)
    summary_path, total_tokens_used, total_cost = call_openai(
        text_path=file_path, source=url, title=title, authors=authors
    )
    create_logseq_note(
        summary_path=summary_path, 
        source=url, 
        title=title, 
        authors=authors, 
        total_tokens_used=total_tokens_used, 
        total_cost=total_cost,
    )
    print("End of job for source: website")


def process_pdf(url, title):
    """
    Downloads the given PDF, splits it into chunks, summarizes each chunk,
    and saves the summaries to a file.

    """
    print(f"Downloading PDF from {url}...")
    file_path = download_pdf(url, title)

    print("Extracting text from PDF...")
    text_path = extract_text_from_pdf(file_path)
    call_openai(text_path)
    print("End of job for source: pdf")


def process_book(path):
    """
    Processes the given book, splits it into chunks, summarizes each chunk,
    and saves the summaries to a file.

    """
    print(f"Processing text file {path}...")
    text_path = path
    call_openai(text_path)
    print("End of job for source: book")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", type=str, help="Source type", required=True
    )
    parser.add_argument("--url", type=str, help="Source URL", required=True)
    parser.add_argument(
        "--title", type=str, help="Title of the source", required=True
    )
    parser.add_argument(
        "--authors", type=str, help="Authors of the source", required=True
    )
    args = parser.parse_args()

    source = args.source
    url = args.url
    title = args.title
    authors = args.authors

    if source == "youtube":
        process_youtube(url=url, title=title, authors=authors)
        sys.exit(1)
    if source == "book":
        process_book(url)
        sys.exit(1)
    if source == "pdf":
        process_pdf(url, title)
        sys.exit(1)
    if source == "website":
        process_website(url=url, title=title, authors=authors)
        sys.exit(1)

    print("ERROR: Unknown source.")
