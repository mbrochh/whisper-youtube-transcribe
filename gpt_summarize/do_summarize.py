import os

import openai
import spacy
import tiktoken

from .local_settings import OPENAI_API_KEY

PROMPT = """
Create a bullet point summary of the text that will follow after the heading `TEXT:`. 

Do not just list the general topic, but the actual facts that were shared.

For example, if a speaker claims that "a dosage of X increases Y", do not
just write "the speaker disusses the effects of X", instead write "a dosage 
of X increases Y".

Use '- ' for bullet points:

After you have made all bullet points, add one last bullet point that 
summarizes the main message of the content, like so:

- Main message: [MAIN MESSAGE HERE]

---

TEXT TITLE: {title}

TEXT:
{chunk}
"""

# MODEL = "gpt-3.5-turbo-16k"
# ENCODING = "cl100k_base"
# MODEL_MAX_TOKENS = 16384
# COST_PER_1K_INPUT_TOKENS_USD = 0.003
# COST_PER_1K_OUTPUT_TOKENS_USD = 0.004
# RESPONSE_TOKENS = 4000

MODEL = "gpt-4-1106-preview"
ENCODING = "cl100k_base"
MODEL_MAX_TOKENS = 128000
COST_PER_1K_INPUT_TOKENS_USD = 0.01
COST_PER_1K_OUTPUT_TOKENS_USD = 0.03
RESPONSE_TOKENS = 4000



def count_tokens(text):
    """Count tokens in a text string using tiktoken."""
    enc = tiktoken.encoding_for_model(MODEL)
    tokens = enc.encode(text)
    token_count = len(tokens)
    return token_count


def split_text(text_path=None, title=None):
    """
    Split text into chunks of no more than max_tokens, using spaCy, so that
    full sentences are never broken up.

    """
    prompt_tokens = count_tokens(PROMPT.format(chunk="", title=title))
    max_tokens = MODEL_MAX_TOKENS - prompt_tokens - RESPONSE_TOKENS

    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("sentencizer")

    with open(text_path, "r") as f:
        text = f.read()

    doc = nlp(
        text, disable=["tagger", "parser", "ner", "lemmatizer", "textcat"]
    )
    chunks = []
    current_chunk = []

    for sent in doc.sents:
        sent_text = sent.text.strip()  # this is one sentence
        sent_tokens = count_tokens(sent_text)

        if (
            sum([count_tokens(chunk) for chunk in current_chunk]) + sent_tokens
            > max_tokens
        ):
            # the sentence would make the chunk too big, so start a new chunk
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent_text]
        else:
            # the sentence still fits into the current chunk
            current_chunk.append(sent_text)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    total_token_count = sum([count_tokens(chunk) for chunk in chunks])
    return chunks, total_token_count


def summarize(chunk=None, title=None):
    """
    Calls OpenAI API to summarize a chunk of text.

    """
    client = openai.Client(api_key=OPENAI_API_KEY)
    prompt = PROMPT.format(chunk=chunk, title=title)
    print("Sending prompt to OpenAI API...")
    result = client.chat.completions.create( model=MODEL, messages=[{"role": "user", "content": prompt}], max_tokens=RESPONSE_TOKENS, temperature=0, n=1, stream=False,)
    return result


def summarize_in_parallel(chunks, num_threads=4):
    """
    Calls OpenAI API to summarize each chunk of text.

    """
    summaries = []
    for chunk in chunks:
        result = summarize(chunk)
        summaries.append(result)

    # OpenAI now rate limits when using multiple threads...
    # with ThreadPoolExecutor(max_workers=num_threads) as executor:
    #     results = executor.map(summarize, chunks)
    #     for result in results:
    #         summaries.append(result)
    return summaries


def save_summaries(summaries, filename_only, output_dir="files/summaries"):
    """
    Saves summaries to a text file, and returns the path to the file.

    Also calculates the total number of tokens used, and the cost of the
    API calls.

    """
    total_input_tokens_used = 0
    total_output_tokens_used = 0
    summary_path = os.path.join(output_dir, f"{filename_only}.txt")
    with open(summary_path, "w") as f:
        for summary in summaries:
            f.write(summary.choices[0].message.content)
            f.write("\n\n")
            total_input_tokens_used += summary.usage.prompt_tokens
            total_output_tokens_used += summary.usage.completion_tokens
    total_input_cost = (
        total_input_tokens_used * COST_PER_1K_INPUT_TOKENS_USD / 1000
    )
    total_output_cost = (
        total_output_tokens_used * COST_PER_1K_OUTPUT_TOKENS_USD / 1000
    )
    total_tokens_used = total_input_tokens_used + total_output_tokens_used
    total_cost = total_input_cost + total_output_cost
    return summary_path, total_tokens_used, total_cost
