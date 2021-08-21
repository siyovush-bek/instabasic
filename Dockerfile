# pull official base image
FROM python:3.8.11-slim-buster

# set working dir
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean

# install dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system

COPY . .

