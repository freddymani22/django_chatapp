FROM python:3.10-slim-buster
ENV PYTHONUNBUFFERED =1
WORKDIR /django_chat
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt