# 🤗 Hugging Face Azure Deployment
Learn how to deploy an ML container with FastAPI and deploy it to `Azure Container Apps` (`https://learn.microsoft.com/fr-fr/azure/container-apps/overview?WT.mc_id=academic-0000-alfredodeza`)
 with GitHub Actions. 

Fork this repository `https://github.com/alfredodeza/huggingface-azure-acr` which gives you a good starting point with a Dockerfile, GitHub Actions workflow, and Python code that already works for generating text using GPT-2 with HuggingFace Transformers.

Start by going through an architectural overview of the end-result, then you go through every configuration item needed to set the automation right between Azure and GitHub Actions and the GitHub Container Registry. Finally, you'll deploy doing a few crucial requirements needed for everything to work, like ingress ports and setting the right amount of RAM and CPU.

Follow these steps to get everything right:
- Use GitHub Container Registry to push a built container
- Use the Azure CLI in a GItHub Action to authenticate to Azure
- How to generate an Azure Service Principal and a Personal Access Token to authenticate
- Configure Azure Container Apps to correctly serve a model with enough resources
- Look at deployment logs to ensure things are working right


## Requirements
To complete this lab follow these steps:

1. Fork the following GitHub repository: `https://github.com/alfredodeza/huggingface-azure-acr`

2. Create an Azure account (or sign into your account):
    a.  Azure For Students account (no credit card required) with free credits (`https://azure.microsoft.com/fr-fr/free/students/?WT.mc_id=academic-0000-alfredodeza`)

    b. Create a new Azure account `https://azure.microsoft.com/en-US/?WT.mc_id=academic-0000-alfredodeza`
 

3. Follow the steps in the repository README to capture every component needed like tokens, secrets, and application names


`Recommendation`: Use the video lessons in the course as a reference on how to deploy to Azure.

## Extra challenges:
1. Try using a different Hugging Face model
2. Add a different endpoint

