import docker

client = docker.from_env()

image = 'httpd'
binding = {80: 8084}

print("Downloading Image...")
image = client.images.pull(image)
print("Image downloaded")
print("Running container..")
container = client.containers.run(image, detach=True, ports=binding)
print("Container started with ID: {}".format(container.id))
print("Container running with the port binding " + str(binding))
for container in client.containers.list():
    print("Los id de los contenedores que existen son:",container.id)