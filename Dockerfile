FROM debian:12.1

RUN apt-get update && \
    apt-get install -y git ffmpeg make bash wget g++ vim python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /whisper

RUN git clone https://github.com/ggerganov/whisper.cpp.git

WORKDIR /whisper/whisper.cpp

RUN bash ./models/download-ggml-model.sh base.en

RUN make CFLAGS='-O2 -Wall -march=armv8-a+simd'

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 install pip --upgrade --break-system-packages

RUN pip3 install -r requirements.txt --break-system-packages

RUN python3 -m spacy download en_core_web_sm --break-system-packages

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]