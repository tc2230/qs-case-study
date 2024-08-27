FROM python:3.11.9-slim

RUN mkdir /deploy
COPY ./ /deploy/
WORKDIR /deploy

RUN apt-get update && apt-get install -y nano git curl
RUN pip install -r requirements.txt