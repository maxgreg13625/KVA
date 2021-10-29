FROM ubuntu:xenial-20210804

RUN mkdir /home/kva &&\
    apt update --yes &&\
    apt upgrade --yes &&\
    apt-get install wget --yes &&\
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/kva/miniconda.sh &&\
    bash /home/kva/miniconda.sh -b -p /home/kva/miniconda

RUN mkdir /home/kva/env &&\
    /home/kva/miniconda/bin/conda create --p /home/kva/env/kva python=3.8 