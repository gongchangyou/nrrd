FROM ubuntu:14.04.4

RUN apt-get update && \
	apt-get -y install teem-apps
