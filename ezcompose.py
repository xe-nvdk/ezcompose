import os
os.system("clear")

# v0.1.6

# What's New

# Added Restart condition
# Added Environment variables
# Added depends_on

print("######################################################################")
print("###################### Welcome to EZCompose ##########################")
print("######################################################################\n")

print("This software is going to help you to build a docker-compose.yml file.\n")

TEXT_FILE = open("docker-compose.yml", "w")

VERSION = ('version: "3.8"\n\n')
TEXT_FILE.write(VERSION)

SERVICES = ("services:\n")
TEXT_FILE.write(SERVICES)

CONT = "y"
while CONT == "y":

# Defining Service Name

    SERVICE_NAME = str(input("Name of the service: "))
    TEXT_FILE.write("\n\n   " + str(SERVICE_NAME) + ":")

# Name of the container

    CONTAINER_NAME = str(input("Do you want to name your container? [y/n]: "))
    if CONTAINER_NAME == str("y"):
        CONTAINER_NAME = str(input("Specify a name: "))
        TEXT_FILE.write("\n    " + str("container_name: ") + str(CONTAINER_NAME))

    else:
        pass

# Image to download

    IMAGE = str(input("What's the image?: "))
    TEXT_FILE.write(str("\n    ") + str("image: ") + str(IMAGE))

# Restart Condition

    RESTART = str(input("Do you want to define a restart policy? [y/n]: "))
    if RESTART == ("y"):
        print("In what condition you container should restart?:")
        print("\n1: None \n2: Always \n3: On-Failure \n4: Unless-Stopped\n")
        CONDITION = int(input("\nEnter your selection: "))

        if CONDITION == int(1):
            TEXT_FILE.write("\n    " + str("restart: no"))

        elif CONDITION == int(2):
            TEXT_FILE.write("\n    " + str("restart: always"))

        elif CONDITION == int(3):
            TEXT_FILE.write("\n    " + str("restart: on-failure"))

        elif CONDITION == int(4):
            TEXT_FILE.write("\n    " + str("restart: unless-stopped"))

        else:
            print("The option entered is not valid")

    else:
        pass

# Ports Definition

    PORTS = str(input("¿Do you want to publish ports? [y/n]: "))
    if PORTS == ("y"):
        TEXT_FILE.write("\n    " + str("ports:"))

    CONT = "y"
    while CONT == "y":

        if PORTS == str("y"):
            PORT_PUBLISHED = int(input("Define external port: "))
            PORT_CONTAINER = int(input("Define container port: "))
            TEXT_FILE.write("\n     - " + str(PORT_PUBLISHED) + ":" + str(PORT_CONTAINER))

            CONT = str(input("\nDo you want to add more ports? [y/n]: "))

        else:
            break

    else:
        pass

# depends_on definition

    DEP = str(input("Do you want to define a dependency? [y/n]: "))

    if DEP == ("y"):
        TEXT_FILE.write("\n    depends_on: ")
        DEP_NAME = str(input("Define the service you want to wait, comma separated: "))
        DEP_NAME = DEP_NAME.split(", ")
        for item in DEP_NAME:
            TEXT_FILE.write("\n     - %s" % item)

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

# Env definition

    ENV = str(input("Do you want to define a environment variables? [y/n]: "))

    if ENV == ("y"):
        TEXT_FILE.write("\n    environment: ")
        ENV_NAME = str(input("Define the environment variables with values, comma separated: "))
        ENV_NAME = ENV_NAME.split(", ")
        for item in ENV_NAME:
            TEXT_FILE.write("\n     - %s" % item)

    else:
        pass

# Bind Volumes Definition

    BIND_VOLUMES = str(input("¿Do you want to add a bind volume? [y/n]: "))
    if BIND_VOLUMES == str("y"):
        TEXT_FILE.write("\n    volumes: ")

    CONT = "y"
    while CONT == "y":

        if BIND_VOLUMES == str("y"):
            LOCAL_PATH = str(input("Define the local path: "))
            CONTAINER_PATH = str(input("Define the path in container: "))
            PERMISSIONS = str(input("Define permissions [rw/ro]: "))
            TEXT_FILE.write(str("\n     - " + str(LOCAL_PATH) + str(":") + str(CONTAINER_PATH)))
            TEXT_FILE.write(":" + str(PERMISSIONS))

            CONT = str(input("\nDo you want to add another bind volume? [y/n]: "))

        else:
            break

    else:
        pass

# Managed Volumes Definition

    MANAGED_VOLUMES = str(input("¿Do you want to add a managed volume? [y/n]: "))
    if BIND_VOLUMES == str("n") and MANAGED_VOLUMES == ("y"):
        TEXT_FILE.write("\n    volumes:")


    if MANAGED_VOLUMES == str("y"):
        VOLUME_NAME = str(input("Define a Managed Volume name: "))
        CONTAINER_PATH = str(input("Define the path in container: "))
        TEXT_FILE.write(str("\n     - " + str(VOLUME_NAME) + ":" + str(CONTAINER_PATH)))

    else:
        pass

# Command definition

    COMMAND = str(input("Do you want to define a command? [y/n]: "))
    if COMMAND == str("y"):
        TEXT_FILE.write("\n    " + str("command: "))

    CONT = "y"
    while CONT == "y":

        if COMMAND == str("y"):
            COMMAND_NAME = str(input("Type the command: "))
            TEXT_FILE.write(str('\n     - ') + str(COMMAND_NAME))

            CONT = str(input("\nDo you want to add another command? [y/n]: "))

        else:
            break

    else:
        pass

# Label Definition

    LABELS = str(input("Do you want to add a label? [y/n]: "))
    if LABELS == ("y"):
        TEXT_FILE.write("\n    " + str("labels:"))

    CONT = "y"
    while CONT == "y":

        if LABELS == str("y"):
            LABEL_NAME = str(input("Name of the label: "))
            LABEL_VALUE = str(input("Value of the label: "))
            TEXT_FILE.write(str('\n     - "') + str(LABEL_NAME))
            TEXT_FILE.write(str('=') + str(LABEL_VALUE) + str('"'))

            CONT = str(input("\nDo you want to add another label? [y/n]: "))

        else:
            break

    else:
        pass

    CONT = str(input("\nDo you want to add a new container? [y/n]: "))

# Definiendo redes y volumenes

if NETWORKS == str("y"):
    TEXT_FILE.write("\n\n" + str("networks:"))

    for item in NETWORK_NAME:
        TEXT_FILE.write("\n  %s:" % item)

if MANAGED_VOLUMES == str("y"):
    TEXT_FILE.write("\n\nvolumes:")
    TEXT_FILE.write(str("\n  ") + str(VOLUME_NAME) + str(":"))

TEXT_FILE.close()

print("\nFile building is done. You'll find it in this folder:")
print("\n"+os.getcwd())
print("######################################################################")
print("#################### Thank you for using EZCompose ###################")
print("######################################################################")

# Horas dedicadas a este proyecto:
# 14/11/2020: 10.5
# 15/11/2020: 2
# 19/11/2020: 8
# 20/11/2020: 1
# 21/11/2020: 3
# 22/11/2020: 1:30
# 29/11/2020: 11:00

# Contributors:
# * Ignacio Van Droogenbroeck
