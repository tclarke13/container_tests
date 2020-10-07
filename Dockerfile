# https://github.com/tiangolo/uvicorn-gunicorn-docker
# The base image contains a set of defaults and "auto tuning" to get high performance
FROM python:3.8.6-slim-buster

WORKDIR /app

COPY ./app /app/