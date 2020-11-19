import os
os.system("clear")

# v0.1.4

# What's New

# Added capacity to specify multiples bind volumes
# Added posibility to add multiple networks

global VOLUMES_BIND

print("######################################################################")
print("###################### Welcome to EZCompose ##########################")
print("######################################################################\n")

print("This software is going to help you to build a docker-compose.yml file\n")

TEXT_FILE = open("docker-compose.yml", "w")

VERSION = ('version: "3.3"\n\n')
TEXT_FILE.write(VERSION)

services = ("services:\n")
TEXT_FILE.write(services)

cont = "y"
while cont == "y":

# Defining Service Name

    SERVICE_NAME = str(input("Name of the service: "))
    TEXT_FILE.write("\n\n   " + str(SERVICE_NAME) + ":")

# Name of the container

    container_name = str(input("Do you want to name your container? [y/n]: "))
    if container_name == str("y"):
        container_name = str(input("Specify a name: "))
        TEXT_FILE.write("\n    " + str("container_name: ") + str(container_name))

    else:
        pass

# Image to download

    image = str(input("What's the image?: "))
    TEXT_FILE.write(str("\n    ") + str("image: ") + str(image))

# Ports Definition

    ports = str(input("¿Do you want to publish ports? [y/n]: "))
    if ports == ("y"):
        TEXT_FILE.write("\n    " + str("ports:"))

    cont = "y"
    while cont == "y":

        if ports == str("y"):
            port_published = int(input("Define external port: "))
            port_container = int(input("Define container port: "))
            TEXT_FILE.write("\n     - " + str(port_published) + ":" + str(port_container))

            cont = str(input("\nDo you want to add more ports? [y/n]: "))

        else:
            break

    else:
        pass

# Networks Definition

    NETWORKS = str(input("Do you want to define a network? [y/n]: "))

    if NETWORKS == ("y"):
        TEXT_FILE.write("\n    networks: ")
        NETWORK_NAME = str(input("Define the networks, comma separated: "))
        NETWORK_NAME = NETWORK_NAME.split(", ")
        for item in NETWORK_NAME:
            TEXT_FILE.write("\n     - %s" % item)

    else:
        pass

# Bind Volumes Definition

    BIND_VOLUMES = str(input("¿Do you want to add Bind Volumes? [y/n]: "))
    if BIND_VOLUMES == str("y"):
        TEXT_FILE.write("\n    volumes: ")

    cont = "y"
    while cont == "y":

        if BIND_VOLUMES == str("y"):
            LOCAL_PATH = str(input("Define the local path: "))
            CONTAINER_PATH = str(input("Define the path in container: "))
            PERMISSIONS = str(input("Define permissions [rw/ro]: "))
            TEXT_FILE.write(str("\n     - " + str(LOCAL_PATH) + str(":") + str(CONTAINER_PATH) + str(":") + str(PERMISSIONS)))

            cont = str(input("\nDo you want to add more Bind Volumes? [y/n]: "))

        else:
            break

    else:
        pass

# Managed Volumes Definition

    MANAGED_VOLUMES = str(input("¿Do you want to add Manage Volumes? [y/n]: "))
    if BIND_VOLUMES == str("n") and MANAGED_VOLUMES == ("y"):
        TEXT_FILE.write("\n    volumes:")


    if MANAGED_VOLUMES == str("y"):
        VOLUME_NAME = str(input("Define a Managed Volume name: "))
        CONTAINER_PATH = str(input("Define the path in container: "))
        TEXT_FILE.write(str("\n     - " + str(VOLUME_NAME) + ":" + str(CONTAINER_PATH)))

    else:
        pass

# Command definition

    command = str(input("Do you want to define a command? [y/n]: "))

    if command == str("y"):
        command_name = str(input("Type the command: "))
        TEXT_FILE.write("\n    " + str("command:\n     - ") + str(command_name))

    else:
        pass

# Label Definition

    LABELS = str(input("Do you want to add a Label? [y/n]: "))
    if LABELS == ("y"):
        TEXT_FILE.write("\n    " + str("labels:"))

    cont = "y"
    while cont == "y":

        if LABELS == str("y"):
            LABEL_NAME = str(input("Name of the Label: "))
            LABEL_VALUE = str(input("Value of the Label: "))
            TEXT_FILE.write("\n     - " + str(LABEL_NAME) + "=" + str(LABEL_VALUE))

            cont = str(input("\nDo you want to add more labels? [y/n]: "))

        else:
            break

    else:
        pass

    cont = str(input("\nDo you want to add a new container? [y/n]: "))

# Definiendo redes y volumenes

    if NETWORKS == str("y"):
        TEXT_FILE.write("\n\n" + str("networks:"))
        for item in NETWORK_NAME:
            TEXT_FILE.write("\n  %s:" % item)

    if MANAGED_VOLUMES == str("y"):
        TEXT_FILE.write("\n\nvolumes:")
        TEXT_FILE.write(str("\n  ") + str(VOLUME_NAME) + str(":"))

TEXT_FILE.close()

print("\nTu archivo esta listo, lo encontraras en el mismo directorio desde donde ejecutaste este programa")
print("\nGracias por usar EZCompose")
print("\n")

# Horas dedicadas a este proyecto:
# 14/11/2020: 10.5
# 15/11/2020: 2
# 19/11/2020: 5.5

# Contributors:
# * Ignacio Van Droogenbroeck