FROM python:3.9-alpine

RUN apk add --no-cache libstdc++ libgcc g++ \
    # For django-hamlpy
    # gcc musl-dev \
    # For development and debug
    bash vim \
    # for updating python module
    && pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r requirements.txt

ENV DASH_DEBUG_MODE True
