FROM ubuntu:latest

MAINTAINER Amit Ghadge (amitg.b14@gmail.com)

# Install
RUN \
	apt-get update && \
	apt-get -y upgrade && \
	apt-get install -y mosquitto mosquitto-clients && \
	apt-get install -y python python-dev python-pip python-virtualenv && \
	apt-get install -y net-tools && \
	apt-get install -y vim


ENTRYPOINT service mosquitto start && /bin/bash

