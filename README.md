# EZCompose ![visitors](https://visitor-badge.glitch.me/badge?page_id=ezcompose)
EZCompose es un programa en Python que mediante un asistente te ayuda a generar un archivo docker-compose.yml. En este video, pueden ver [cómo funciona EZCompose](https://youtu.be/nCqUx_3D7mQ?t=100).

## Preguntas Frecuentes

### Como ejecuto EZCompose

Para ejecutar EZCompose, si estás en Linux, descargas el ejecutable que encontrarás en [releases](https://github.com/xe-nvdk/ezcompose/releases), si no quieres ejecutarlo desde el ejecutable y quieres lanzar el script de Python, usa el que esta especificado en el release, ya que el de repositorio se esta tocando todo el tiempo y puede no funcionar. 

Si usas código fuente descargado desde el release, necesitas instalar Python3 en tu sistema, Si no lo tienes, ejecutas:

```
$ sudo apt-get install python3
```
Si estás en Windows, te recomiendo que lo bajes desde la [página oficial](https://www.python.org/downloads/).

Una vez que instalaste, descargas la última versión de EZCompose y ejecutas lo siguiente:
```
python3 ezcompose.py
```
A partir de ahí, deberías ver la pantalla de bienvenida

```
##############################################################
################ Bienvenides a EZCompose #####################
##############################################################

Este programa te ayudará a crear un archivo docker-compose.yml

Escribe el nombre del servicio:
```
### Le faltan opciones a EZCompose

Si, eso es correcto, a la fecha que estoy escribiendo esto, (Noviembre 2020) EZCompose es capaz de generar un archivo docker-compose.yml totalmente funcional, pero es bastante limitado, solo podés agregar un solo juego de puertos, un solo volumen, una sola label, etc. La idea es que a medida que siga aprendiendo Python, tenga más funcionalidades y alcance un grado "Production Ready".

### Che, me gustaría contribuir

Si te copa el proyecto y te gustaría contribuir, ningún problema, todas las contribuciones son bienvenidas. Simplemente hace un Fork de este repo y cuando tengas esa modificación hecha, hace un Pull Request.
