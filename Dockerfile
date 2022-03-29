FROM python

# install teem-unu
RUN apt-get update && \
	apt-get -y install teem-apps

# install paraview
RUN	apt-get install -y paraview && \
	apt-get install -y python3-paraview

COPY hello.py /tmp/hello.py
