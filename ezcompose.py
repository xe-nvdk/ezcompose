import os
#os.system("clear")

print("##############################################################")
print("################ Bienvenides a EZCompose #####################")
print("##############################################################\n")

print("Este programa te ayudará a crear un archivo docker-compose.yml\n")

text_file = open("docker-compose.yml", "w")

version = ('version: "3.3"\n\n')
text_file.write(version)

services = ("services:\n")
text_file.write(services)  

cont = "y"
while cont == "y":

    service_name = str(input("Escribe el nombre del servicio: "))
    text_file.write("\n\n   " + str(service_name) + ":")

    container_name = str(input("¿Quieres especificar un nombre al contenedor? [y/n]: "))
    if container_name == str("y"):
        container_name = str(input("Dame un nombre para tu contenedor: "))
        text_file.write("\n    " + str("container_name: ") + str(container_name))

    else: 
        pass

    image = str(input("Define la imágen a descargar: "))
    text_file.write(str('\n    ') + str('image: ') + str(image))

    ports = str(input("¿Quieres publicar uno o mas puertos? [y/n]: "))
    text_file.write("\n    " + str("ports:"))

    cont = "y"
    while cont == "y":
        
        if ports == str("y"):
            port_published = int(input("Define el puerto a publicar hacia afuera: "))
            port_container = int(input("Define el puerto del contenedor: "))
            text_file.write("\n     - " + str(port_published) + ":" + str(port_container))

            cont = str(input("\nQueres agregar mas puertos? [y/n]: "))

        else:
            break

    else:
        pass

    volumes = str(input("¿Quieres montar volumenes? [y/n]: "))

    if volumes == str("y"):
        local_path = str(input("Especifica el directorio local: "))
        container_path = str(input("Especifica el directorio a resguardar en el contenedor: "))
        permissions = str(input("Define los permisos. Pueden ser rw o ro, si no especificas nada, sera rw: "))
        text_file.write("\n    " + str("volumes:\n     - ") + str(local_path) + ":" + str(container_path) + ":" + str(permissions))

    else:
        pass

    network = str(input("¿Quieres especificar una red? [y/n]: "))

    if network == str("y"):
        network_name = str(input("Especifica el nombre de la red: "))
        text_file.write("\n    " + str("networks:\n     - ") + str(network_name))

    else:
        pass

    command = str(input("¿Quieres especificar un comando? [y/n]: "))

    if command == str("y"):
        command_name = str(input("Especifica el comando: "))
        text_file.write("\n    " + str("command:\n     - ") + str(command_name))

    else:
        pass

    labels = str(input("¿Quieres especificar una label? [y/n]: "))
    text_file.write("\n    " + str("labels:"))

    cont = "y"
    while cont == "y":
        
        if labels == str("y"):
            label_name = str(input("Especifica el nombre de la label: "))
            label_value = str(input("Especifica el valor de la label: "))
            text_file.write("\n     - " + str(label_name) + "=" + str(label_value))

            cont = str(input("\nQueres agregar mas labels? [y/n]: "))

        else:
            break

    else:
        pass

    cont = str(input("\nQueres agregar un nuevo contenedor? [y/n]: "))
   
# Definiendo redes y volumenes

if network == str("y"):
    text_file.write("\n\n" + str("networks:\n  ") + str(network_name)+":" +"\n")


text_file.close()

print("\nTu archivo esta listo, lo encontraras en el mismo directorio desde donde ejecutaste este programa")
print("\nGracias por usar EZCompose")
print("\n")

# Horas dedicadas a este proyecto:
# 14/11/2020: 10.5
# 15/11/2020: 2

# Contributors:
# * Ignacio Van Droogenbroeck
