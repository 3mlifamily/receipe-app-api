FROM python:3.7-alpine
MAINTAINER 3mfamily

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D 3mfamily
USER 3mfamily
