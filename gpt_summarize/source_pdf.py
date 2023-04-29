import os
import sys
import unicodedata

import PyPDF2
import requests

from .source_youtube import slugify


def remove_non_printable_chars(text):
    """
    Removes non-printable characters from the given text.

    """
    return "".join(c for c in text if unicodedata.category(c) != "Cc")


def extract_text_from_pdf(
    file_path, filename_without_filetype, output_path="files/pdf_text"
):
    """
    Extracts the text from the given PDF and saves it to the given output path.

    """
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            dirty_text = reader.pages[page_num].extract_text()
            cleaned_text = remove_non_printable_chars(dirty_text)
            text += cleaned_text

    filename = f"{filename_without_filetype}.txt"
    txt_path = os.path.join(output_path, filename)
    with open(txt_path, "w") as f:
        f.write(text)
    return txt_path


def download_pdf(url, title, output_path="files/pdf"):
    """
    Downloads the given PDF and saves it to the given output path.

    """
    response = requests.get(url)
    title_slug = slugify(title)
    filename_without_filetype = title_slug
    pdf_path = os.path.join(output_path, f"{title_slug}.pdf")
    with open(pdf_path, "wb") as file:
        file.write(response.content)
    return pdf_path, filename_without_filetype


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        title = sys.argv[2]
        file_path, filename_without_filetype = download_pdf(url, title)
        extract_text_from_pdf(file_path, filename_without_filetype)
        print(f"Downloaded pdf to {file_path}")
    else:
        print('Usage: python -m gpt_summarize.source_pdf.py <url> "<title>"')
        print('Usage: python -m gpt_summarize.source_pdf.py <url> "<title>"')
