import os
import sys

import openai
import spacy
import tiktoken

from .local_settings import OPENAI_API_KEY

PROMPT = """Create a bullet point summary of the following text. 
Make sure that all major talking points are part of the summary. 
Use '- ' for bullet points:

{chunk}
"""

MODEL = "text-davinci-003"
ENCODING = "cl100k_base"
MODEL_MAX_TOKENS = 4096
COST_PER_1K_TOKENS_USD = 0.02
RESPONSE_TOKENS = 1000


def count_tokens(text):
    enc = tiktoken.encoding_for_model(MODEL)
    tokens = enc.encode(text)
    token_count = len(tokens)
    return token_count


def get_sentences(text_path):
    with open(text_path, "r") as f:
        text = f.read()
    nlp = spacy.load("en_core_web_sm")
    spacy_docs = nlp(text)
    sentences = [sentence.text.strip() for sentence in spacy_docs.sents]
    return sentences


def get_chunks(sentences):
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # Check if adding the sentence to the current chunk would exceed the token limit
        new_chunk = f"{current_chunk} {sentence}"
        new_chunk_token_count = (
            count_tokens(PROMPT.format(chunk=new_chunk)) + RESPONSE_TOKENS
        )

        if new_chunk_token_count <= MODEL_MAX_TOKENS:
            # If not, add the sentence to the current chunk
            current_chunk = new_chunk.strip()
        else:
            # If yes, start a new chunk with the sentence
            chunks.append(current_chunk)
            current_chunk = sentence.strip()

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def summarize(chunks, filename):
    openai.api_key = OPENAI_API_KEY
    summaries = []
    for chunk in chunks:
        prompt = PROMPT.format(chunk=chunk)
        prompt_tokens = count_tokens(prompt)
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=MODEL_MAX_TOKENS - prompt_tokens,
            temperature=0,
            n=1,
        )
        summaries.append(result)

    summary_path = os.path.join("files/summaries", f"{filename}.txt")
    with open(summary_path, "w") as f:
        for summary in summaries:
            f.write(summary["choices"][0].text)
            f.write("\n\n")
    return summary_path


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_path = sys.argv[1]
        sentences = get_sentences(text_path)
        chunks = get_chunks(sentences)
        filename = os.path.splitext(os.path.basename(text_path))[0]
        summary_path = summarize(chunks, filename)
        print(f"Summary saved to {summary_path}.")
    else:
        print(
            "Usage: python -m gpt_summarize.do_summarize.py <transcript_path>"
        )
