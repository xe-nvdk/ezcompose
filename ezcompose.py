import os

def prompt_input(prompt, valid_responses=None, default=None):
    while True:
        response = input(prompt).strip().lower()
        if valid_responses and response in valid_responses:
            return response
        elif response == '' and default is not None:
            return default
        print("Invalid input.")

def add_simple_entry(key, prompt, file):
    response = prompt_input(f"{prompt} [y/n]: ", valid_responses=["y", "n"], default="n")
    if response == "y":
        value = input(f"Enter {key}: ").strip()
        file.write(f"\n    {key}: {value}")

def add_list_entry(key, entry_prompt, add_more_prompt, file):
    add_entry = prompt_input(f"Do you want to add {key}? [y/n]: ", valid_responses=["y", "n"], default="n")
    if add_entry == "y":
        file.write(f"\n    {key}:")
        while add_entry == "y":
            entry = input(entry_prompt).strip()
            file.write(f"\n      - {entry}")
            add_entry = prompt_input(add_more_prompt, valid_responses=["y", "n"], default="n")

# Clear terminal screen
os.system("clear")
print("Welcome to EZCompose - Docker Compose File Builder\n")

with open("docker-compose.yml", "w") as file:
    file.write('version: "3.8"\nservices:')

    add_container = "y"
    while add_container == "y":
        service_name = input("\nName of the service: ").strip()
        file.write(f"\n  {service_name}:")
        image = input("Enter the image name: ").strip()
        file.write(f"\n    image: {image}")

        # Simple entries
        add_simple_entry("container_name", "Do you want to add a container name?", file)
        add_simple_entry("restart", "Do you want to add a restart policy?", file)

        # List entries
        add_list_entry("ports", "Enter <external>:<internal> port mapping: ", "Add more ports? [y/n]: ", file)
        add_list_entry("depends_on", "Enter dependent service name: ", "Add more dependencies? [y/n]: ", file)
        add_list_entry("environment", "Enter environment variable in KEY=VALUE format: ", "Add more environment variables? [y/n]: ", file)
        add_list_entry("volumes", "Enter <local_path>:<container_path> volume mapping: ", "Add more volumes? [y/n]: ", file)

        add_container = prompt_input("\nDo you want to add another service? [y/n]: ", valid_responses=["y", "n"], default="n")

    # Networks and volumes at the top level
    add_list_entry("networks", "Enter network name: ", "Add more networks? [y/n]: ", file)
    add_list_entry("volumes", "Enter volume name: ", "Add more volumes? [y/n]: ", file)

print("\nFile building is done. You'll find it in this folder:")
print("\n" + os.getcwd())
