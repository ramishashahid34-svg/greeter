# Greeter

A simple Python HTTP greeting application containerized with Docker.

## Application

The application runs a Python HTTP server on port `5000`.

The current version displays:

**Hello again, Ramisha!**

## Run Locally

Make sure Python is installed.

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Build Docker Image

Build version 1.0:

```bash
docker build -t ramishashahid8/greeter:1.0 .
```

Build version 1.1:

```bash
docker build -t ramishashahid8/greeter:1.1 .
```

## Run Docker Container

Run version 1.0:

```bash
docker run -d --name greeter-v1 -p 5001:5000 ramishashahid8/greeter:1.0
```

Run version 1.1:

```bash
docker run -d --name greeter-v11 -p 5002:5000 ramishashahid8/greeter:1.1
```

The application can then be accessed at:

```text
Version 1.0: http://localhost:5001
Version 1.1: http://localhost:5002
```

## Docker Hub

Docker Hub repository:

```text
ramishashahid8/greeter
```

Available tags:

```text
ramishashahid8/greeter:1.0
ramishashahid8/greeter:1.1
```

## Useful Docker Commands

Check running containers:

```bash
docker ps
```

View container logs:

```bash
docker logs <container-name>
```

Stop a container:

```bash
docker stop <container-name>
```

Remove a container:

```bash
docker rm <container-name>
```

## Ports

| Version | Container Port | Host Port |
| ------- | -------------: | --------: |
| 1.0     |           5000 |      5001 |
| 1.1     |           5000 |      5002 |

Both versions can run simultaneously because they use different host ports.
