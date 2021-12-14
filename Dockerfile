FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
RUN apk --update add bash nano
RUN apk add gcc
RUN apk add musl-dev
RUN apk add build-base
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
COPY . /cloud
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt
