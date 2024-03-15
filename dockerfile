FROM python:3.13.0a5-alpine3.19
MAINTAINER Ignacio Van Droogenbroeck
WORKDIR /ezcompose
ADD $PWD/ezcompose.py /ezcompose/
CMD ["/ezcompose/ezcompose.py"]
ENTRYPOINT ["python"]
