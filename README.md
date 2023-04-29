# Introduction to ChatGPT, Copilot & Whisper

This is a talk that I presented for the Python User Group Singapore & National
Library Board in May 2023.

## Running the slides

* Clone this repo & `cd` into it and then `cd` into the `slidev` folder
* `npm install`
* `npm run dev`
* Browse to `http://localhost:3030/`

## Local Setup for MacOS

* Clone this repo & `cd` into it
* Make sure you have pyenv installed with the virtualenv plugin
* Make sure you have homebrew installed
* `pyenv virtualenv chatgpt-copilot-whisper`
* `pyenv activate chatgpt-copilot-whisper`
* `pip install pip --upgrade`
* `pip install -r requirements.txt`
* `brew install ffmpeg`
* `python -m spacy download en_core_web_sm`

Also, create the following folder structure inside this repo:

```
- files/
---- audio/
---- summaries/
---- transcripts/
```

If setup worked, you should be able to summarize a video like so:

* `cd` into the git repo
* `python -m gpt_summarize.gpt_summarize <some youtube URL>`