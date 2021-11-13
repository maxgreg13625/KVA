# Windows env
# docker build --build-arg home_dir=rendy -t kva-test . --no-cache
# winpty docker run -it --volume //d/workspace/kva:/home/rendy/workspace/kva kva-test

# Ubuntu env
# sudo docker build --build-arg home_dir=rendy -t kva-test . --no-cache
# sudo docker run -it --volume /home/rendy/workspace/kva:/home/rendy/workspace/kva kva-test

FROM ubuntu:xenial-20210804
ARG home_dir=kva
COPY requirements.txt /tmp/requirements.txt

RUN mkdir -p /home/${home_dir}/workspace/kva &&\
    apt update --yes &&\
    apt upgrade --yes &&\
    apt-get install wget --yes &&\
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/${home_dir}/miniconda.sh &&\
    bash /home/${home_dir}/miniconda.sh -b -p /home/${home_dir}/miniconda &&\
    rm -rf /home/${home_dir}/miniconda.sh &&\
	mkdir /home/${home_dir}/env &&\
    /home/${home_dir}/miniconda/bin/conda create --p /home/${home_dir}/env/kva python=3.8 &&\
    /home/${home_dir}/env/kva/bin/pip install -r /tmp/requirements.txt

ENV PATH=$PATH:/home/${home_dir}/env/kva/bin
