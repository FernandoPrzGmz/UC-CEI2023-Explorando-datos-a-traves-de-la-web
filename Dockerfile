FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive
ARG PYTHON_VERSION=3.8

RUN apt update -y
RUN apt upgrade -y

RUN apt install -y \
        git \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
        tree \
        nano \
        nginx \
        redis-server

# Configurar Redis
RUN sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf
RUN service redis-server restart

# Instalar python 
RUN curl https://pyenv.run | bash

ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN set -ex \
    && pyenv update \
    && pyenv install ${PYTHON_VERSION} \
    && pyenv global ${PYTHON_VERSION} \
    && pyenv rehash

# Configurar e instalar dependencias del proyecto
RUN mkdir -p /app/hello-world

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

EXPOSE 8000
EXPOSE 6655

CMD ["tail", "-f", "/dev/null"]
