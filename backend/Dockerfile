# syntax=docker/dockerfile:1
# FROM python:3.9-alpine

# WORKDIR /app

# COPY py.requirements py.requirements/
# RUN pip3 install -r py.requirements/all.txt

# COPY . .

# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# FROM ubuntu:16.04

# MAINTAINER Your Name "dangeloagustinariel@gmail.com"

# RUN apt-get update -y && \
#     apt-get install -y python-pip python-dev

# # We copy just the requirements.txt first to leverage Docker cache
# COPY py.requirements /app/py.requirements/

# WORKDIR /app

# RUN pip install --upgrade pip

# RUN pip install -r py.requirements/all.txt

# COPY . .

# ENTRYPOINT [ "python" ]

# CMD [ "app.py" ]

FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
