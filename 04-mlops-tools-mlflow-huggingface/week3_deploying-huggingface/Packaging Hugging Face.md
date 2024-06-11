# Packaging Hugging Face

## 🤗 Hugging Face Packaging with GitHub Actions

For this lab you will use a GitHub repository which you must fork: 
`https://github.com/alfredodeza/huggingface-ghcr`
alfredodeza/huggingface-ghcr: MLOps packaging: build and push to GitHub Container Registry

Learn how to create a container and package it with GitHub Actions. This repository gives you a good starting point for a Dockerfile, GitHub Actions workflow, and Python code.

The web application uses FastAPI with Hugging Face and exposes a single endpoint that you can interact with it.

Instructions:
1. Fork this repository : `https://github.com/alfredodeza/huggingface-ghcr`

2. Run the GitHub Actions as-is so that you can register your own containerized application with no modifications needed.

3. Inspect that the container is registered as a GitHub package

4. Make new changes to the application and re-publish the container

5. Change the trigger in the workflow file to allow publishing when code is merged to main

