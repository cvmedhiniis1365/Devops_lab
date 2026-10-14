# Exercise 4: Docker Networking with Multiple Containers

## Objective
Understand Docker bridge networking and configure communication between multiple containers.

## Application Components
- **Flask:** REST API available at port 5001.
- **MySQL:** Database container accessible internally on port 3306.
- **Redis:** Cache container accessible internally on port 6379.
- **Docker bridge network:** `my-bridge-net`.

## Files
- `app.py` — Flask REST API.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Flask image configuration.
- `screenshots/` — Exercise evidence.

## Commands Executed

### Create and inspect the network
```powershell
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

### Run the containers
```powershell
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabRoot123! mysql:8.0
docker run -d --name redis --network my-bridge-net redis:7-alpine
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api:1.0
```

### Test the Flask API
```powershell
curl.exe http://localhost:5001/about
```

### Test connectivity from Flask
```powershell
docker exec flask python -c "import socket; print(socket.create_connection(('redis', 6379), timeout=5).getpeername())"
docker exec flask python -c "import socket; print(socket.create_connection(('mysql', 3306), timeout=5).getpeername())"
```

## Questions and Answers

### 1. What is the purpose of the `--network` flag?
It connects a container to the specified Docker network.

### 2. How do containers communicate on the same network?
Containers on a user-defined bridge network can communicate using container names or IP addresses. Docker provides DNS-based name resolution.

### 3. What is the difference between bridge and host networking?
- **Bridge:** Containers use an isolated virtual network and can communicate through that network.
- **Host:** A container shares the host network namespace, where supported.

### 4. How can a container port be exposed to the host?
Use the `-p` option, for example `-p 5001:5001`.

## Learning Outcomes
- Created and inspected a Docker bridge network.
- Connected Flask, MySQL, and Redis to the same network.
- Exposed the Flask API on host port 5001.
- Tested container-to-container TCP connectivity.
