# EZCompose ![visitors](https://visitor-badge.glitch.me/badge?page_id=ezcompose) ![Pylint](https://github.com/xe-nvdk/ezcompose/workflows/Pylint/badge.svg)
EZCompose is a docker-compose.yml builder. Define your images, networks, volumes, ports and more, easily. In this video (Spanish) you can see how [EZCompose works](https://youtu.be/nCqUx_3D7mQ?t=100).

## FAQ

### How should I run EZCompose?

In each release, you have a executable file to run EZCompose under Linux or MacOS. 
```
$ ./ezcompose
```
If you're a Windows user, you need to download the source code and run in the following way.

```
$ python3 ezcompose.py
```
If you don't have installed Python, you can download it from [[here](https://www.python.org/downloads/).

Since the v0.1.5, EZCompose can be run from a Docker Container, you only need to run...
```
$ docker run -it hectorivand/ezcompose:v0.1.6
```

### I want to contribute with EZCompose

If you like this project and you want to contribute, you're very welcome to do it, just fork it and make a pull request when you're ready. Here, you can see the the [To Do list](https://github.com/xe-nvdk/ezcompose/projects/1) and here the [Issues](https://github.com/xe-nvdk/ezcompose/issues).
