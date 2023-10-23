import os
import sys

from newspaper import Article

from .source_youtube import slugify


def download_website(url, title, output_path="files/website/"):
    """
    Downloads the text from a website and saves it to the given output path.

    """
    article = Article(url)
    article.download()
    article.parse()
    title_slug = slugify(title)
    if not title_slug:
        raise Exception(f"Could not slugify title: {title}")
    filename = f"{title_slug}.txt"
    file_path = os.path.join(output_path, filename)
    with open(file_path, "w") as f:
        f.write(article.text)
    return file_path, article.text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        title = sys.argv[1]
        file_path, text = download_website(url, title)
        print(f"Downloaded website to {file_path} ({len(text)} characters)")
    else:
        print("Usage: python -m gpt_summarize.source_website.py <url>")
