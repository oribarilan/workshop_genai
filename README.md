# Applied GenAI Workshop

This is a workshop on Applied Generative AI. We will focus on practical application of LLMs using LangChain.
The content of this repository is not meant to be self-served. It is meant to be used in conjunction with the workshop.
Enjoy the workshop!

## Resource

We will use Azure OpenAI Studio for this workshop.
Make sure you have a valid Azure subscription with credits, and an Azure OpenAI resource set up.
Deploy 

1. Go to [Azure OpenAI Studio](https://oai.azure.com/portal)
2. Click "Deployments"
3. Click "Create new deployment"
4. select "gpt-35-turbo" as the model (don't worry, you can deploy other models later)

## Installation

Throughout the workshop, we will use dev-containers to minimize the setup time and ensure alignment between participants.
You may choose to avoid dev-containers and set up your local environment. 
However, I will have limited capacity to help you with the setup during the workshop.
If you do choose to set up your local environment, please follow the manual instructions in the next section below.

### Dev Containers (Recommended)
1. Docker
    a. Install Docker Desktop: https://www.docker.com/products/docker-desktop
    b. Validate the installation by running the following command in your terminal:
    ```bash
    docker --version
    ```
    c. Get to know docker a bit using this walkgthrough (Optional) https://docs.docker.com/guides/walkthroughs/run-a-container/
2. Visual Studio Code
    a. Install Visual Studio Code: https://code.visualstudio.com/
    b. Install the Dev-Containers extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
    c. Open Visual Studio Code and click on the green icon on the bottom left corner. Select "Remote-Containers: Open Folder in Container" and select the folder where you have cloned the repository.
3. That's it! (The magic of dev-containers 😉)

### Manual Installation (Not recommended)

Skip this if you are using dev-containers.

1. Python
    a. You will need a Python 3.9 environment. You can install it globally or use a virtual environment, but make sure you are using Python 3.9.
    b. Install Python 3.9.18: https://www.python.org/downloads/
    c. Validate:
    ```bash
    python --version
    ```
2. Jupyter Notebook
    a. Install Jupyter Notebook: https://jupyter.org/install
    b. Validate:
    ```bash
    jupyter --version
    ```
3. Install the required Python packages
    a. Execute
    ```bash
    pip install -r requirements.txt
    ```
    b. Validate:
    ```bash
    python -c "import langchain; print(langchain.__version__)"
    ```
4. Just command runner
    a. Install Just [https://](https://github.com/casey/just)
    b. Validate:
    ```bash
    just --version
    ```

### Setup
1. Clone the repository
2. Execute `cp .env.template .env`
3. Fill in the `.env` file with your OpenAI API key and endpoint, taken from [Azure OpenAI Studio](https://oai.azure.com/portal)

These appear in the "Keys and Endpoint" tab, under "Resource Management" in the Azure portal.