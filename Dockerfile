# Windows env
# docker build -t kva-test . --no-cache
# winpty docker run -it --volume //d/workspace/kva:/home/kva/workspace/kva kva-test

# Ubuntu env
# sudo docker build -t kva-test . --no-cache
# sudo docker run -it --volume /home/rendy/workspace/kva:/home/kva/workspace/kva kva-test

FROM ubuntu:xenial-20210804

COPY requirements.txt /tmp/requirements.txt

RUN mkdir -p /home/kva/workspace/kva &&\
    apt update --yes &&\
    apt upgrade --yes &&\
    apt-get install wget --yes &&\
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/kva/miniconda.sh &&\
    bash /home/kva/miniconda.sh -b -p /home/kva/miniconda &&\
    rm -rf /home/kva/miniconda.sh &&\
	mkdir /home/kva/env &&\
    /home/kva/miniconda/bin/conda create --p /home/kva/env/kva python=3.8 &&\
    /home/kva/env/kva/bin/pip install -r /tmp/requirements.txt

ENV PATH=$PATH:/home/kva/env/kva/bin
