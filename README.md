# Introduction to ChatGPT, Copilot & Whisper

This is a talk that I presented for the Python User Group Singapore & National
Library Board in May 2023.

You can find the slides [here](https://mbrochh.github.io/whisper-youtube-transcribe/1)

You can find a video of the talk [here](https://www.youtube.com/watch?v=t5eVAtavoQ8)

## Usage

* First, follow the steps in the [Local Setup for MacOS](#local-setup-for-macos) section
* If you want to summarize a Youtube video, run this command:
  * `python -m gpt_summarize.gpt_summarize <some youtube URL>`
* If you want to summarize a PDF, run this command:
  * `python -m gpt_summarize.gpt_summarize <some PDF file> "<some title>"` 
* If you want to summarize a website, run this command:
  * `python -m gpt_summarize.gpt_summarize <some website URL>`

Note: PDF and Website is not very well tested and there are tons of edge cases
that will make these commands crash.

Youtube videos work very well. The only thing that I found is that sometimes,
for very long videos, Whisper spams out and while it does transcribe everything
correctly, it stops adding punctuation. Without full stops, the `do_summarize`
module cannot create proper chunks with spacy (based on full sentences), and
then the chunk gets too big and the API call to OpenAI fails.

## Local Setup for MacOS

If you would like to use this tool on your own machine, you can do this:

* Clone this repo & `cd` into it
* Make sure you have `pyenv` installed with the `virtualenv` plugin
* Make sure you have `homebrew` installed
* Create a virtual environment: `pyenv virtualenv chatgpt-copilot-whisper`
* Activate the virtual environment: `pyenv activate chatgpt-copilot-whisper`
* Upgrade pip: `pip install pip --upgrade`
* Install all dependencies: `pip install -r requirements.txt`
* Install ffmpeg: `brew install ffmpeg`
* Download spacy model: `python -m spacy download en_core_web_sm`

Also, create the following folder structure inside this repo:

```
- files/
---- audio/
---- summaries/
---- transcripts/
```

You can do so via:

```bash
mkdir -p files/audio
mkdir -p files/summaries
mkdir -p files/transcripts
```

If setup worked, you should be able to summarize a video like so:

* `cd` into the git repo
* `python -m gpt_summarize.gpt_summarize <some youtube URL>`

## Running the tests

There are a few pytest tests in this repo. You can run them like so:

* `pytest -vs --cov=. --cov-report term-missing --cov-report html`

## Running the slids

* `git checkout slides`
* Learn more about how to run and build the slides in the README.md in the slides branch