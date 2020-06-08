FROM ubuntu:18.04

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        curl \
        python \
        python3-dev \
        python3-setuptools \
        python3-pip \
        nginx \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
  pip3 install argparse && \
  pip3 install grpcio && \
  pip3 install grpcio-tools && \
  pip3 install libeospy && \
  pip3 install loguru && \
  pip3 install matplotlib && \
  pip3 install "numpy<1.17" && \
  pip3 install pebble && \
  pip3 install pickle-mixin && \
  pip3 install pycrypto && \
  pip3 install --upgrade setuptools && \
  pip3 install timeloop && \
  pip3 install zipfile36

RUN pip3 uninstall -y tensorboard tensorflow tensorflow-estimator
RUN pip3 install "tensorflow==1.15.2"

# Add specific installs here
#...

# Copy across the local files.
COPY . bittensor/*
