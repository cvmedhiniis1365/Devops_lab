import docker

client = docker.from_env()

print("Building Flask image...")
client.images.build(path=".", tag="flask-apparmor:1.0")

print("Starting container with requested AppArmor profile...")
container = client.containers.run(
    "flask-apparmor:1.0",
    name="flask-sdk-test",
    ports={"5000/tcp": 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)

try:
    info = client.api.inspect_container(container.id)
    print("Container started:", container.short_id)
    print("Requested security options:", info["HostConfig"]["SecurityOpt"])
    print("Process security label:", container.exec_run("cat /proc/self/attr/current").output.decode().strip())
finally:
    container.remove(force=True)
    print("Test container removed.")
