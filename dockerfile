FROM python:3.9.10

# prepare python virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy sources
RUN mkdir /address_parser
ADD . /address_parser
WORKDIR /address_parser

RUN pip install pipx

# install dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pipx ensurepath

# download model for deepparse
RUN mkdir -p /root/.cache/bpemb/multi
RUN wget https://nlp.h-its.org/bpemb/multi/multi.wiki.bpe.vs100000.model -P /root/.cache/bpemb/multi/
RUN curl -s -L https://nlp.h-its.org/bpemb/multi/multi.wiki.bpe.vs100000.d300.w2v.bin.tar.gz | tar xz -C /root/.cache/bpemb/multi/
RUN wget https://graal.ift.ulaval.ca/public/deepparse/bpemb.ckpt -P /root/.cache/deepparse/
RUN wget https://graal.ift.ulaval.ca/public/deepparse/bpemb.version -P /root/.cache/deepparse/

EXPOSE 5000
ENTRYPOINT ["gunicorn" , "-b", "0.0.0.0:5000", "-t", "300", "wsgi:app"]#