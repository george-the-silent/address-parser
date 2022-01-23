FROM python:3.9.10

EXPOSE 5000

# prepare python virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy sources
RUN mkdir /address_parser
ADD . /address_parser
WORKDIR /address_parser

RUN pip install pipx
# install torch (machine learning framework required by deepparse)
RUN pip3 install torch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1
RUN pipx install .
RUN pipx ensurepath

# download model for deepparse
RUN mkdir -p /root/.cache/bpemb/multi
RUN wget https://nlp.h-its.org/bpemb/multi/multi.wiki.bpe.vs100000.model -P /root/.cache/bpemb/multi/
RUN curl -s -L https://nlp.h-its.org/bpemb/multi/multi.wiki.bpe.vs100000.d300.w2v.bin.tar.gz | tar xz -C /root/.cache/bpemb/multi/

ENTRYPOINT ["/root/.local/pipx/venvs/address-parser/bin/address_parser"]