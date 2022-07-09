FROM python:3.10.5-alpine3.16
MAINTAINER Ignacio Van Droogenbroeck
WORKDIR /ezcompose
ADD $PWD/ezcompose.py /ezcompose/
CMD ["/ezcompose/ezcompose.py"]
ENTRYPOINT ["python"]
