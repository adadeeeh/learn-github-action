# learn-github-action

## Description

This repository is used to learn GitHub Actions. This repository app uses FastAPI which is a Python web framework and then dockerize it and push it to Docker Registry. [This](.github/workflows/python-app.yml) GitHub Action is used as CI to build and test FastAPI app. [This](.github/workflows/push-docker-dev.yml) GitHub Action is used as CI to build docker image in dev branch for non-production environment and push it to Docker Registry. [This](.github/workflows/push-docker-main.yml) GitHub Action is used as CI to build docker image in main branch for production environment and push it to Docker Registry.

## Develop Locally

1. Create Python virtual environment

   ```
   python3 -m venv env
   ```

2. Activate virtual environment

   ```
   source env/bin/activate
   ```

   To deactivae virtual environment

   ```
   deactivate
   ```

3. Install requirements

   ```python
   pip3 install -r requirements.txt
   ```

4. Run FastAPI app

   ```
   uvicorn src.main:app --reload
   ```

   Or

   ```
   pyton3 src/main.py
   ```

5. Build Docker image

   ```
   docker build -t fastapi-cicd:1.0 .
   ```

6. Create and run container from Docker image

   ```
   docker run -d --name fastapi -p 80:8000 fastapi-cicd:1.0
   ```

   If container already exist, run container with

   ```
   docker start <container_name>
   ```

7. Acces the FastAPI container in **127.0.0.1:80**
