FROM ubuntu:18.04

RUN apt-get update && apt-get install -y wget sudo curl vim
RUN wget https://github.com/EOSIO/eosio.cdt/releases/download/v1.6.1/eosio.cdt_1.6.1-1_amd64.deb
RUN apt-get update && sudo apt install -y ./eosio.cdt_1.6.1-1_amd64.deb
RUN wget https://github.com/eosio/eos/releases/download/v2.0.2/eosio_2.0.2-1-ubuntu-18.04_amd64.deb
RUN apt-get update && sudo apt install -y ./eosio_2.0.2-1-ubuntu-18.04_amd64.deb

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
  pip3 install "numpy<1.17" && \
  pip3 install pickle-mixin && \
  pip3 install pycrypto && \
  pip3 install timeloop


# Install Bittensor protos
RUN pip3 install -i https://test.pypi.org/simple/ bittensor-proto==0.0.4

# Copy source to this image.
RUN mkdir bittensor
COPY . bittensor/
WORKDIR /bittensor
