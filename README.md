# Introduction to ChatGPT, Copilot & Whisper

This is a talk that I presented for the Python User Group Singapore & National
Library Board in May 2023.

You can find the slides [here](https://mbrochh.github.io/whisper-youtube-transcribe/1)

You can find a video of the talk [here](https://www.youtube.com/watch?v=t5eVAtavoQ8)

This is part two of a three part series

1. [Introduction to ChatGPT, Copilot & Whisper](https://mbrochh.github.io/whisper-youtube-transcribe/1)
2. [Summarising books with ChatGPT, Python and Logseq](https://mbrochh.github.io/kindle-scrape-summarise/1)
3. [Talk to your notes with Logseq and ChatGPT](https://mbrochh.github.io/logseq-faiss-chatgpt/1)

## Usage with Docker

I don't recommend using this with Docker because it is much slower than using
it on a MacBook. But if you want to try it out, you can do this:

* close this repo and `cd` into the cloned folder
* `docker-compose build``
* `docker-compose run -rm python --source youtube --url YOUTUBE_URL --title "VIDEO_TITLE" --authors "VIDEO_AUTHORS"`

The output should appear in the `files/summaries` folder eventually.

## Usage on local machine

* First, follow the steps in the [Local Setup for MacOS](#local-setup-for-macos) section
* If you want to summarize a Youtube video, run this command:
  * `python -m gpt_summarize.gpt_summarize --source youtube --url YOUTUBE_URL --title "VIDEO_TITLE" --authors "VIDEO_AUTHORS"`
* If you want to summarize a PDF, run this command:
  * `python -m gpt_summarize.gpt_summarize --source pdf --url PDF_URL --title "PDF_TITLE" --authors "PDF_AUTHORS"` 
* If you want to summarize a website, run this command:
  * `python -m gpt_summarize.gpt_summarize --source website --url WEBSITE_URL --title "WEBSITE_TITLE" --authors "WEBSITE_AUTHORS"`

Note: PDF and Website is not very well tested and there are tons of edge cases
that will make these commands crash.

Youtube videos work very well. The only thing that I found is that sometimes,
for very long videos, Whisper spasms out and while it does transcribe everything
correctly, it stops adding punctuation. Without full stops, the `do_summarize`
module cannot create proper chunks with spacy (based on full sentences), and
then the chunk gets too big and the API call to OpenAI fails.

## Local Setup for MacOS

If you would like to use this tool on your own machine, you can do this:

NOTE: This should work fine even on Windows, you probably just need to 
figure out how to install `ffmpeg` over there. I'm not sure if `whisper.cpp`
works on windows.

First, setup the faster whisper.cpp:

* `mkdir ~/Repos && cd ~/Repos`
* `git clone https://github.com/ggerganov/whisper.cpp.git`
* `cd whisper.cpp`
* `bash ./models/download-ggml-model.sh base.en`
* `make`

Now prepare this repo:

* Clone this repo & `cd` into it
* Make sure you have `pyenv` installed with the `virtualenv` plugin
* Make sure you have `homebrew` installed
* Create a virtual environment: `pyenv virtualenv chatgpt-copilot-whisper`
* Activate the virtual environment: `pyenv activate chatgpt-copilot-whisper`
* Upgrade pip: `pip install pip --upgrade`
* Install all dependencies: `pip install -r requirements.txt`
* Install ffmpeg: `brew install ffmpeg`
* Download spacy model: `python -m spacy download en_core_web_sm`
* Create your `local_settings.py` file:
  * `cd gpt_summarize`
  * `cp local_settings.py.example local_settings.py`
  * Edit the `local_settings.py` file and add your OpenAI API key and change
    the FFMPEG_PATH if needed (try `which ffmpeg` in your terminal to find out 
    where it is) and change REPO_PATH (this repo) and WHISPER_REPO_PATH (
      the whisper.cpp repo)

Also, create the following folder structure inside this repo:

```bash
├── files
│   ├── audio
│   ├── book
│   ├── logseq
│   ├── summaries
│   ├── website
│   └── transcripts
```

You can do so via:

```bash
mkdir -p files/audio
mkdir -p files/book
mkdir -p files/logseq
mkdir -p files/summaries
mkdir -p files/transcripts
mkdir -p files/website
```

If setup worked, you should be able to summarize a video like so:

* `cd` into the git repo
* `python -m gpt_summarize.gpt_summarize --source youtube --url YOUTUBE_URL --title "SOME_TITLE" --authors "SOME AUTHORS"`

## Running the tests

There are a few pytest tests in this repo. You can run them like so:

* `pytest -vs --cov=. --cov-report term-missing --cov-report html`

## Structure of this repo

* `gpt_summarize.py` is your main entry point. Based on the command line
  arguments that you pass, it will decide which module to run.
* If you want to summarize a video, the logic is in `source_youtube.py`
  * `source_youtube.py` makes use of `do_transcribe.py`. The other two
    obviously don't need that.
* If you want to summarize a PDF, the logic is in `source_pdf.py`
* If you want to summarize a website, the logic is in `source_website.py`
* All three `source_XXX.py` modules make use of `do_summarize.py`

In theory, you can call each part of the pipeline individually like so:

```bash
# Download a video:
python -m gpt_summarize.source_youtube <some youtube URL>

# Then transcribe it:
python -m gpt_summarize.do_transcribe <path to mp3>

# Then summarize it:
python -m gpt_summarize.do_summarize <path to transcript>
```

## Running the slids

* `git checkout slides`
* Learn more about how to run and build the slides in the README.md in the slides branch