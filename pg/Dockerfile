FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN mkdir /pg

WORKDIR /pg

RUN apt-get update\
    && apt install -y python3-dev \
        build-essential \
        python3-pip

RUN pip install django djangorestframework

COPY . /pg/
