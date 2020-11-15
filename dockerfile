FROM python:3.9.0-alpine
MAINTAINER Ignacio Van Droogenbroeck
WORKDIR /ezcompose
ADD $PWD/ezcompose.py /ezcompose/
CMD ["/ezcompose/ezcompose.py"]
ENTRYPOINT ["python"]
