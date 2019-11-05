# docker build -t awscli -f AWScli.dockerfile .

FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update && apt-get -y install  --no-install-recommends apt-utils
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
# RUN apt-get -y upgrade
# RUN apt-get -y --fix-missing install build-essential
RUN apt-get -y install python-pip
RUN apt-get install -y  less groff jq vim
RUN pip install awscli
