FROM python:3.9-buster

WORKDIR /opt/app

RUN apt-get update && apt-get install -y python-psycopg2 wget cron unzip curl

ENV DOCKER_ENV True

ADD requirements.txt /opt/app

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install uwsgi

RUN mkdir logs
RUN mkdir static
RUN mkdir static/css
RUN mkdir static/javascript
RUN mkdir static/images
RUN mkdir media
RUN mkdir private-media
RUN mkdir socket

# install dependencies
ADD . /opt/app
RUN chmod +x .docker/entrypoint.sh

EXPOSE 8000
ENTRYPOINT [".docker/entrypoint.sh"]
