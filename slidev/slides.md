---
# try also 'default' to start simple
theme: default
title: Introduction to ChatGPT, Whisper & Github Copilot for Python Development
background: images/cover.jpg
# apply any windi css classes to the current slide
class: 'text-center'
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
drawings:
  persist: true
# page transition
transition: fade-out
# use UnoCSS
css: unocss
---

<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<div class="text-left relative">
    <div class="z-90 text-lg">Introduction to ChatGPT, Whisper & Github Copilot for Python Development</div>
    <div class="text-sm mt-0">by <a href="https://twitter.com/mbrochh" target="_blank">Martin Brochhaus</a></div>
    <div class="text-sm mt-1">slides: <a href="https://bit.ly/pugs-whisper" target="_blank">https://bit.ly/pugs-whisper</a></div>
</div>

---
clicks: 3
---

# About PUGS

<ul>
    <li v-click="1">
        PUGS stands for <span class="text-red">Python User Group Singapore</span>
        <ul>
            <li>registered non-profit society, run by volunteers</li>
            <li>was created to organize <a class="text-red" href="https://pycon.sg" target="_blank">PyCon Singapore</a></li>
        </ul>
    </li>
    <li v-click="2">
        Visit <a class="text-red" href="https://pugs.org.sg/membership/" target="_blank">https://pugs.org.sg/membership/</a> to become a member
    </li>
    <li v-click="3">
        Monthly meetups at <a class="text-red" href="https://www.meetup.com/singapore-python-user-group/" target="_blank">https://www.meetup.com/singapore-python-user-group/</a>
    </li>
</ul>

<div class="grid grid-cols-3 gap-4 mt-4 max-h-[220px] overflow-hidden">
  <div v-click="1"><img src="/images/pycon.png" /></div>
  <div v-click="2"><img src="/images/membership.png" /></div>
  <div v-click="3"><img src="/images/meetup.png" /></div>
</div>

---

# About me

- Martin Brochhaus
- CTO of [theartling.com](https://theartling.com/en/)
- Committee member of PUGS
- Twitter: [@mbrochh](https://twitter.com/mbrochh)

<div class="grid grid-cols-2 gap-4 mt-4 max-h-[300px] overflow-hidden">
  <div><img src="/images/theartling.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/twitter.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Say Hi to GPT-4!

<v-clicks>

- GPT stands for **G**enerative **P**re-trained **T**ransformer
- It is a **multimodal** **L**arge **L**anguage **M**odel (LLM)
    - multimodal means it can take several "modalities" as input other than just text (ie images and audio)
- It has a **context window** of 8192 and 32768 tokens 
    - depending on how much you are willing to pay
- It was released on March 14, 2023
- Sam Altman said it has cost $100 million to train the model
- There are rumors that it has 1 trillion **parameters**

</v-clicks>

---

# Say Hi to GPT-4!

<div class="flex flex-col">
<img src="/images/gpt3data.png" class="w-full" />
<em class="text-xs text-center">Source: <a href="https://en.wikipedia.org/wiki/Generative_pre-trained_transformer" target="_blank">Wikipedia</a></em>
</div>

---

# The rise of ChatGPT

- It took ChatGPT only two months to reach 100 million monthly active users

<div class="flex flex-col mt-4">
<img src="/images/chatgpt_mau.png" class="max-h-[300px] mx-auto" />
<em class="text-xs text-center">Source: <a href="https://www.youtube.com/watch?v=bSvTVREwSNw" target="_blank">How ChatGPT Works Technically | ChatGPT Architecture</a></em>
</div>

---

# Attention Is All You Need

- 2017 Paper started it all: [https://arxiv.org/pdf/1706.03762.pdf](https://arxiv.org/pdf/1706.03762.pdf)

<div class="grid grid-cols-2 gap-4 mt-6">
<div>
<img src="/images/attention_paper.png" class="max-h-[300px] mx-auto" />
</div>
<div>
<img src="/images/attention_diagram.png" class="max-h-[300px] mx-auto" />
</div>
</div>

---

# 1 Trillion Parameters?

<v-clicks>

- The goal with any machine learning model is to create a function
- We want to throw some input `x` into the function
- The function shall return a predicted value `y` to us
- For language models, `x` might be a word or sentence
- As a first step, that text will get converted into numbers so that we can do math with it
- The function will then spit out another number, which stands for another word that is most likely to come next
- Our function might look something like this: `f(x) = ax + bx + cx + dx + ex + fx + gx`
- But: it doesn't stop at `g`, it has A LOT more unknown parameters
- GPT-3 had 175 billion parameters, GPT-4 is rumoured to have 1 trillion parameters

</v-clicks>

---
layout: two-cols
transition: none
---

# How does it train?

- First, we give it some text as input

::right::

<img src="/images/training_1.jpg" class="max-h-[550px] mt-[-30px]" />

---
layout: two-cols
transition: none
---

# How does it train?

- First, we give it some text as input
- It will then "predict" some random nonsense

::right::

<img src="/images/training_2.jpg" class="max-h-[550px] mt-[-30px]" />

---
layout: two-cols
transition: none
---

# How does it train?

- First, we give it some text as input
- It will then "predict" some random nonsense
- We then reveal the correct answer

::right::

<img src="/images/training_3.jpg" class="max-h-[550px] mt-[-30px]" />

---
layout: two-cols
transition: none
---

# How does it train?

- First, we give it some text as input
- It will then "predict" some random nonsense
- We then reveal the correct answer
- We calculate the error, or "loss" between the prediction and the correct answer

::right::

<img src="/images/training_4.jpg" class="max-h-[550px] mt-[-30px]" />

---
layout: two-cols
transition: none
---

# How does it train?

- First, we give it some text as input
- It will then "predict" some random nonsense
- We then reveal the correct answer
- We calculate the error, or "loss" between the prediction and the correct answer
- We use that loss value to update all the parameters in the model a tiny bit via a process called "backpropagation"
- We repeat that billions of times with billions of different inputs

::right::

<img src="/images/training_5.jpg" class="max-h-[550px] mt-[-30px]" />

---

# So what are "tokens"?

<div class="flex">
    <div class="flex-grow">
        <ul>
            <li>It would be inefficient to use all words of all languages as our vocabulary</li>
            <li>A so called <code>Byte Pair Encoding</code> (BPE) algorithm can create a new, smaller vocabulary</li>
            <li>GPT-4 can keep 8192 or 32768 tokens in mind</li>
        </ul>
        <div class="mt-6">
            <div>
            <ul>
                <li><span class="text-red">astro</span>logy</li>
                <li><span class="text-red">astro</span><span class="text-blue">no</span>mist</li>
                <li><span class="text-red">astro</span><span class="text-blue">no</span>my</li>
            </ul>
        </div>
    <div class="mt-4">
        <ul>
            <li>
                --> <span class="text-red">astro</span>, <span class="text-blue">no</span>, my, logy, mist
            </li>
            <li>
              You can play around with tokens on the <a href="https://platform.openai.com/tokenizer" target="_blank">
                OpenAI Tokenizer Playground
              </a>
            </li>
        </ul>
    </div>
</div>
</div>
</div>

---

# Converting tokens into vectors

<div class="flex">
    <div class="flex-grow">
        <ul>
            <li>Computers don't understand words, they need numbers</li>
            <li>During the process of training, the model comes up with a vector for every word in the vocabulary</li>
            <li>The <code>text-embedding-ada-002</code> model uses a vector with <a target="_blank" href="https://platform.openai.com/docs/guides/embeddings/second-generation-models">1536 dimensions</a></li>
        </ul>
        <img src="/images/vectors.png" class="max-w-[400px] mt-4" />
    </div>
</div>

---

# Vectors have meaning encoded into them

<div class="flex">
    <div class="flex-grow">
        <ul>
            <li>Let's zoom into one of those vectors</li>
            <li>At the beginning, all these numbers are just random</li>
            <li>But when the model trains, some kind of meaning will be encoded in these vectors</li>
            <li>We do not know what exactly each dimension means, the model is like a black box</li>
        </ul>
        <img src="/images/vectors_meaning.png" class="max-w-[400px] mt-4" />
    </div>
</div>

---

# Vectors allow for similarity search

<div class="flex">
    <div class="flex-grow">
        <ul>
            <li>If the meaning was encoded well, similar words should be near each other in the vector space</li>
        </ul>
        <img src="/images/vectors_1.png" class="max-w-[400px] mt-4" />
    </div>
</div>

---

# Vectors magically understand abstract concepts

<div class="flex">
    <div class="flex-grow">
        <ul>
            <li>Incredibly, we can do vector math and witness the meaning embedded in the vectors</li>
            <li>King - Man + Woman = Queen</li>
        </ul>
        <img src="/images/vectors_2.png" class="max-w-[400px] mt-4" />
    </div>
</div>

---

# How can I learn more?

## Videos

- [Neural Networks by 3Blue1Brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Transformers & NLP by Lucidate](https://www.youtube.com/watch?v=jo1NZ3vCS90&list=PLaJCKi8Nk1hwaMUYxJMiM3jTB2o58A6WY)
- [Visual Guide to Transformer Neural Networks by Hedy AI](https://www.youtube.com/watch?v=mMa2PmYJlCo&list=PL86uXYUJ7999zE8u2-97i4KG_2Zpufkfb&index=2)
- [Intuition Behind Self-Attention Mechanism in Transformer Networks by Ark](https://www.youtube.com/watch?v=g2BRIuln4uc&t=1398s)

## Articles

- [The Illustrated Transformer by Jay Almar](https://jalammar.github.io/illustrated-transformer/)
- [Transformers from Scratch by Brandon Rohrer](https://e2eml.school/transformers.html)

---
layout: image
image: ./images/handson.jpg
--- 

<style>
.text-black-shadow {
  text-shadow: 0 0 3px rgba(0, 0, 0, 1);
} 
</style>

<div class="flex justify-center items-center h-full">
<div class="text-4xl text-black-shadow text-white">Let's get coding!</div>
</div>

---

# Installing Github Copilot

- https://github.com/features/copilot
- https://marketplace.visualstudio.com/items?itemName=GitHub.copilot

<div class="grid grid-cols-2 gap-4 mt-6 max-h-[300px] overflow-hidden">
  <div><img src="/images/copilot.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/copilot_vscode.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Subscribing to OpenAI API

- https://platform.openai.com/overview
- https://platform.openai.com/account/api-keys
- https://platform.openai.com/account/usage

<div class="grid grid-cols-3 gap-4 mt-6 max-h-[300px] overflow-hidden">
  <div><img src="/images/openai.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/apikeys.png" class="max-h-[300px] mx-auto" /></div>
  <div><img src="/images/usage.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# Subscribing to ChatGPT Plus

- Same login as the OpenAI login: https://chat.openai.com/auth/login
- "Profile" --> "My Plan" -> Upgrade to ChatGPT Plus

<div class="grid grid-cols-1 mt-6 max-h-[300px] overflow-hidden">
  <div><img src="/images/chatgpt.png" class="max-h-[300px] mx-auto" /></div>
</div>

---

# What we will build today

<v-clicks depth="2">

- We will build a tool that can summarize Youtube videos
- The tool will perform the following steps:
    1. Download the audio of the video
    1. Transcribe the audio file to text using OpenAI's `Whisper` model
    1. Split the large text into many smaller chunks
    1. Summarize each chunk using OpenAI's `text-davinci-003` model

</v-clicks>

---

# Downloading the audio

- We will use the `yt-dlp` Python library to download the audio
- Our tool will be called via the command line like so:

```bash
python -m gpt_summarize.source_youtube https://www.youtube.com/watch?v=OXcJw5tW9RY
```

<br />

- The output will look like this:

<div class="grid grid-cols-1 mt-2 max-h-[300px] overflow-hidden">
  <div><img src="/images/audio.png" class="w-full" /></div>
</div>

---

# Transcribing the audio

- We will use OpenAI's `Whisper` model to transcribe the audio
- We will call another script via the command line:

```bash
python -m gpt_summarize.do_transcribe files/audio/filename.mp3
```

<br />

- The output will look like this:

<div class="grid grid-cols-1 mt-2 max-h-[300px] overflow-hidden">
  <div><img src="/images/transcribe.png" class="w-full" /></div>
</div>

---

# Summarizing the transcript

- We will use OpenAI's `text-davinci-003` model to summarize the transcript
- We will call another script via the command line:

```bash
python -m gpt_summarize.do_summarize files/transcripts/filename.txt
```

<br />

- The output will look like this:

<img src="/images/summarize.png" class="w-full mt-2" />
<img src="/images/summarize_file.png" class="w-full mt-4" />

---
transition: none
---

# Creating a project

```bash
# First, let's create a new project folder:
mkdir -p ~/Projects/gpt_summarize/gpt_summarize
```

- NOTE: the `mkdir` command stands for "make directory"

---
transition: none
---

# Creating a project

```bash {3,4}
mkdir -p ~/Projects/gpt_summarize/gpt_summarize

# Let's `cd` into the newly created folder
cd ~/Projects/gpt_summarize
```

- NOTE: the `cd` command stands for "change directory"

---
transition: none
---

# Creating a project

```bash {4,5,6,7,8,9,10,11}
mkdir -p ~/Projects/gpt_summarize/gpt_summarize
cd ~/Projects/gpt_summarize

# Now create a few files that we will need later:
touch .gitignore
touch requirements.txt
touch gpt_summarize/__init__.py
touch gpt_summarize/source_youtube.py
touch gpt_summarize/do_transcribe.py
touch gpt_summarize/do_summarize.py
touch gpt_summarize/local_settings.py
```

- NOTE: the `touch` command creates an empty file

---

# Creating a project

```bash {11-14}
mkdir -p ~/Projects/gpt_summarize/gpt_summarize
cd ~/Projects/gpt_summarize
touch .gitignore
touch requirements.txt
touch gpt_summarize/__init__.py
touch gpt_summarize/source_youtube.py
touch gpt_summarize/do_transcribe.py
touch gpt_summarize/do_summarize.py
touch gpt_summarize/local_settings.py

# We will also need a few folders for all the files that our tool will generate:
mkdir -p files/audio
mkdir -p files/transcripts
mkdir -p files/summaries
```

---

# Creating a project

- When you run `tree . -a`, your file structure should look like this:

```bash
.
├── .gitignore
├── files
│   ├── audio
│   ├── summaries
│   └── transcripts
├── gpt_summarize
│   ├── __init__.py
│   ├── do_summarize.py
│   ├── do_summarize.pytouch
│   ├── do_transcribe.py
│   ├── local_settings.py
│   └── source_youtube.py
└── requirements.txt


5 directories, 6 files
```

- NOTE: the `tree .` command shows the file structure of the current folder
    - the `-a` flag shows hidden files like the `.gitignore` file

---
transition: none
---

# The `.gitignore` file

- Put the following code into the `.gitignore` file:

```bash
local_settings.py
files/
__pycache__/
.DS_Store
```

---

# The `.gitignore` file

- Put the following code into the `.gitignore` file:
model on it.

```bash {1}
local_settings.py
files/
__pycache__/
.DS_Store
```

- The most important line is the first one, it makes sure that Github Copilot does never look into the `local_settings.py` file
- IMPORTANT: When working with Copilot you must be aware that VSCode will constantly send your code to Github's servers
    - Make sure that your code does not contain sensitive information
    - Make sure that your company allows you to use Copilot
    - If your company hosts code on Github anyways, there is no reason not to use Copilot

---

# The `local_settings.py` file

- Put the following code into the `local_settings.py` file:

```python
OPENAI_API_KEY = 'YOUR KEY HERE'
```

- You can get your API key [here](https://platform.openai.com/account/api-keys)
- This is considered secret information, which is why we have this file in `.gitignore`
- Never share this key with anyone or they can use your OpenAI credits
- Consider storing this key in a password manager because you won't be able to see it again once it has been created

---

# The `requirements.txt` file

- We will need a few Python libraries throughout these slides
- To make things easier, we will just install them all at once
- Put the following code into the `requirements.txt` file:

```bash
yt-dlp==2023.3.4
openai-whisper==20230314
setuptools-rust==1.5.2
openai==0.27.4
spacy==3.5.2
tiktoken==0.3.1
requests==2.28.2
```

- And then execute `pip install -r requirements.txt` in your terminal

---
transition: none
---

# The `__main__` block for `source_youtube.py`

- Put the following code into the `source_youtube.py` file:

```python
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        audio_path = download_audio(url)
        print(f"Download complete: {audio_path}")
    else:
        print("Usage: python -m gpt_summarize.source_youtube <youtube_url>")
```

---
transition: none
---

# The `__main__` block for `source_youtube.py`

- Put the following code into the `source_youtube.py` file:

```python {3}
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        audio_path = download_audio(url)
        print(f"Download complete: {audio_path}")
    else:
        print("Usage: python -m gpt_summarize.source_youtube <youtube_url>")
```

- The variable `__name__` is a special variable in Python 
- It will have the string value `"__main__"` if this file is executed directly
    - If we call this script from the command line, the value will be `"__main__"`
    - If we import any function or variable from this file into another file, the value will be `"gpt_summarize.source_youtube"`


---
transition: none
---

# The `__main__` block for `source_youtube.py`

- Put the following code into the `source_youtube.py` file:

```python {6}
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        audio_path = download_audio(url)
        print(f"Download complete: {audio_path}")
    else:
        print("Usage: python -m gpt_summarize.source_youtube <youtube_url>")
```

- NOTE: The code will not work, because we have not yet implemented the function `download_audio` 
   
---

# Adding some dummy functions

- Let's add a dummy function to `source_youtube.py`:
- Let's see if Copilot can help us a bit...

```python {3,4}
import sys, os

def download_audio(url):
    return "files/audio/test.webm"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        audio_path = download_audio(url)
        print(f"Download complete: {audio_path}")
    else:
        print("Usage: python -m gpt_summarize.source_youtube <youtube_url>")
```

- Now we can run the code and see if it works:

```bash
python -m gpt_summarize.source_youtube test`
```

---

- Let's ask ChatGPT to help us with the `download_audio` function:

<img src="/images/download_audio_question.png" class="rounded-xl shadow w-full mt-[10%]" />

---

<img src="/images/download_audio_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---

# The `download_audio` function

- Replace the `download_audio` function with the following code:
- Also add the import statement for `yt_dlp` at the top of the file

```python
import sys

import yt_dlp

def download_audio(url):
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
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
```

---

- Let's ask ChatGPT how to get the filename...

<img src="/images/retrieve_filename_question.png" class="rounded-xl shadow w-full mt-[10%]" />

---

<img src="/images/retrieve_filename_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---

# The `download_audio` function

- Replace the `download_audio` function with the following code:
- Also add the import statement for `os` at the top of the file

```python {2,7-15,27,33-34} {maxHeight:'350px'}
import sys
import os

import yt_dlp

def download_audio(url):
    output_filename_result = {}

    def get_filename(info_dict):
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
```

---

# Try it out!

- Now we can run the code and see if it works:

```bash
python -m gpt_summarize.source_youtube https://www.youtube.com/watch?v=OXcJw5tW9RY
```

---
transition: none
---

# The `__main__` block for `do_transcribe.py`

- Like before, we can add a `__main__` block to `do_transcribe.py`:
- This time, we will not provide a Youtube URL, but an audio file path as a command line argument

```python
import os, sys, whisper

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        text_path = transcribe(audio_path)
        print(f"Transcript saved to: {text_path}.")
    else:
        print("Usage: python -m gpt_summarize.do_transcribe <audio_path>")
```

---
transition: none
---

# The `__main__` block for `do_transcribe.py`

- Like before, we can add a `__main__` block to `do_transcribe.py`:
- This time, we will not provide a Youtube URL, but an audio file path as a command line argument

```python {6}
import os, sys, whisper

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        text_path = transcribe(audio_path)
        print(f"Transcript saved to: {text_path}.")
    else:
        print("Usage: python -m gpt_summarize.do_transcribe <audio_path>")
```

- NOTE: Once again, this code will crash because we have not implemented the `transcribe` function yet

---

# The `__main__` block for `do_transcribe.py`

- Let's add a dummy function to `do_transcribe.py`:
- Let's see if Copilot can help us a bit...

```python {2-3}

def transcribe(audio_path):
    return "files/transcripts/test.txt"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
        text_path = transcribe(audio_path)
        print(f"Transcript saved to: {text_path}.")
    else:
        print("Usage: python -m gpt_summarize.do_transcribe <audio_path>")
```

- Now we can run the code and see if it works:

```bash
python -m gpt_summarize.do_transcribe files/audio/test.mp3
```

---

# The `transcribe` function

- Check https://github.com/openai/whisper to learn how to use Whisper
- Replace the `transcribe` function with the following code:

```python
def transcribe(audio_path):
    model = whisper.load_model("small.en")
    result = model.transcribe(audio_path, verbose=True)
    transcript = str(result["text"])

    filename = os.path.splitext(os.path.basename(audio_path))[0]
    text_path = os.path.join("files/transcripts", f"{filename}.txt")
    with open(text_path, "w") as f:
        f.write(transcript)

    return text_path
```

- Run the code!

```bash
python -m gpt_summarize.do_transcribe "files/audio/Sundar Pichai： AI will have greater impact than electricity ｜ Forum Insight.mp3"
```

---

- Tip: ChatGPT can be your Python mentor!

<img src="/images/code_question.png" class="rounded-xl shadow w-full mt-[10%]" />

---

<img src="/images/code_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---
transition: none
---

# The `__main__` block for `do_summarize.py`

- Just like before, we can add a `__main__` block to `do_summarize.py`

```python
import os, sys, openai, spacy, tiktoken

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
            "Usage: python -m gpt_summarize.do_summarize <transcript_path>"
        )
```

---

# The `__main__` block for `do_summarize.py`

- Just like before, we can add a `__main__` block to `do_summarize.py`

```python {6,7,9}
import os, sys, openai, spacy, tiktoken

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
            "Usage: python -m gpt_summarize.do_summarize <transcript_path>"
        )
```

- NOTE: As usual, this code will crash because we have not implemented the `get_sentences` and `get_chunks` and `summarize` functions yet

---
layout: two-cols
---

# Some constants

<ul class="mr-2">
<li>At the top of <code>do_summarize.py</code>, after the imports, add the following code:</li>
<li>See <a href="https://platform.openai.com/docs/models" target="_blank">https://platform.openai.com/docs/models</a></li>
<li>See <a href="https://openai.com/pricing" target="_blank">https://openai.com/pricing</a></li>
</ul>


::right::

<h1>&nbsp;</h1>

```python
# other imports...

from .local_settings import OPENAI_API_KEY

PROMPT = """Create a bullet point summary of the following text. 
Make sure that all major talking points are part of the summary. 
Use '- ' for bullet points:

{chunk}
"""

MODEL = "text-davinci-002"
ENCODING = "cl99k_base"
MODEL_MAX_TOKENS = 4095
COST_PER_0K_TOKENS_USD = 0.02
RESPONSE_TOKENS = 999

# rest of the code...
```

---

# The `__main__` block for `do_summarize.py`

- Let's add dummy functions to `do_summarize.py`:
- Let's see if Copilot can help us a bit...

```python
# imports here...
# constants here...

def get_sentences(text_path):
    return ["This is a sentence."]

def get_chunks(sentences):
    return ["This is a chunk."]

def summarize(chunks, filename):
    return 'files/summaries/test.txt'

# __main__ block here...
```

- Run the code and see if it works:

```bash
python -m gpt_summarize.do_summarize files/transcripts/test.txt
```

---

# Working with tokens

- See [What are tokens and how to count them](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)

<img src="/images/tokens.png" class="max-h-[300px] mt-6 mx-auto shadow rounded-xl" />

---

# Working with tokens

- See [Tiktoken](https://github.com/openai/tiktoken)

<img src="/images/tiktoken.png" class="max-h-[300px] mt-6 mx-auto shadow rounded-xl" />

---

# Working with tokens

- See [https://platform.openai.com/docs/models/gpt-3-5](https://platform.openai.com/docs/models/gpt-3-5)
- The `text-davinci-003` model has a maximum token length of 4,097
- When we send a prompt to the API, we must make sure that the PROMPT + RESPONSE fits into the maximum token limit
    - Example: If our prompt is 4,000 tokens, then our response can only be 97 tokens

---

# Working with tokens

- Our prompt will look like this
- If the `chunk` variable is empty, this would equal 37 tokens:

```python
PROMPT = """Create a bullet point summary of the following text.
Make sure that all major talking points are part of the summary.
Use '- ' for bullet points:

{chunk}
"""
```

<br />

```
Prompt: 37 tokens
```

---

# Working with tokens

```python
PROMPT = """Create a bullet point summary of the following text.
Make sure that all major talking points are part of the summary.
Use '- ' for bullet points:

{chunk}
"""
```

<br />

- We want to leave room for 1000 tokens for ChatGPT to respond

<br />

```
Prompt:     37 tokens
Response: 1000 tokens
```

---

# Working with tokens

```python
PROMPT = """Create a bullet point summary of the following text.
Make sure that all major talking points are part of the summary.
Use '- ' for bullet points:

{chunk}
"""
```

<br />


- That means our chunks can have a maximum size of `4097 - 1037 = 3060` tokens

<br />

```
Prompt:     37 tokens
Chunk:    3060 tokens
Response: 1000 tokens
---------------------
Total:    4097 tokens
``` 

---

<img src="/images/spacy_question.png" class="rounded-xl shadow w-full mt-[10%]" />

- <em class="text-xs">NOTE: I happen to know that spaCy is a good way to split text into sentences</em>

---

<img src="/images/spacy_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---
transition: none
---

# The `get_sentences` function

- Replace the `get_sentences` function with the following code:

```python
def get_sentences(text_path):
    with open(text_path, "r") as f:
        text = f.read()
    nlp = spacy.load("en_core_web_sm")
    spacy_docs = nlp(text)
    sentences = [sentence.text.strip() for sentence in spacy_docs.sents]
    return sentences
```

---

# The `get_sentences` function

- Replace the `get_sentences` function with the following code:

```python {6}
def get_sentences(text_path):
    with open(text_path, "r") as f:
        text = f.read()
    nlp = spacy.load("en_core_web_sm")
    spacy_docs = nlp(text)
    sentences = [sentence.text.strip() for sentence in spacy_docs.sents]
    return sentences
```

- If you are new to Python, this line will probably be confusing!

---

<img src="/images/listcomp_question.png" class="rounded-xl shadow w-full mt-[10%]" />

---

<img src="/images/listcomp_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---

<img src="/images/thanks.png" class="mt-[10%] mx-auto shadow rounded-xl" />

---

# The `count_tokens` function

- Before we can implement the `get_chunks` function, we need a way to count the number of tokens in a chunk
- See [Tiktoken README](https://github.com/openai/tiktoken) 
- Add this `count_tokens` function above all other functions:

```python
def count_tokens(text):
    enc = tiktoken.encoding_for_model(MODEL)
    tokens = enc.encode(text)
    token_count = len(tokens)
    return token_count
```

---

<img src="/images/chunks_question.png" class="rounded-xl shadow max-h-[100%] mx-auto" />

---

<img src="/images/chunks_answer.png" class="max-h-[100%] mx-auto shadow rounded-xl" />

---

# The `get_chunks` function

- Replace the `get_chunks` function with the following code:

```python {all} {maxHeight: '400px'}
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
```

---

# The `summarize` function

- See [OpenAI API docs about completion](https://platform.openai.com/docs/api-reference/completions/create)
- Replace the `summarize` function with the following code:

```python {all} {maxHeight: '300px'}
def summarize(chunks, filename):
    openai.api_key = OPENAI_API_KEY
    summaries = []
    for chunk in chunks:
        prompt = PROMPT.format(chunk=chunk)
        prompt_tokens = count_tokens(prompt)
        result = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            # max_tokens refers to the max tokens of the RESPONSE!!!
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
```

---

# Demo

- Our program should be fully functional now!
- Let's give it a try:

```bash
python -m gpt_summarize.source_youtube https://www.youtube.com/watch?v=OXcJw5tW9RY 
python -m gpt_summarize.do_transcribe "files/audio/Sundar Pichai： AI will have greater impact than electricity ｜ Forum Insight.mp3"
python -m gpt_summarize.do_summarize "files/transcripts/Sundar Pichai： AI will have greater impact than electricity ｜ Forum Insight.txt"
```

<img src="/images/result.png" class="mt-6 w-full shadow rounded-xl" />

---

# Thank you for your attention!

- Join the Python User Group: [https://pugs.org.sg/membership](https://pugs.org.sg/membership)
- Follow me on Twitter: [https://twitter.com/@mbrochh](https://twitter.com/mbrochh)
- Find the slides at [https://bit.ly/pugs-whisper](https://bit.ly/pugs-whisper)

---
layout: end
---
