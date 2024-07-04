# Hello RAGFlow

```bash
git clone https://github.com/infiniflow/ragflow.git

# Build the pre-built Docker images and start up the server:
cd ragflow/docker
chmod +x ./entrypoint.sh
docker compose up -d

# Check the server status after having the server up and running:
docker logs -f ragflow-server

```

# Build from source

```bash
git clone https://github.com/infiniflow/ragflow.git
cd ragflow/
docker build -t infiniflow/ragflow:dev .
cd ragflow/docker
chmod +x ./entrypoint.sh
docker compose up -d
```