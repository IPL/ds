FROM python:3.9-alpine
RUN apk add build-base

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /srv
