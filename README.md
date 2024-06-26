# Applied GenAI Workshop

This is a workshop on Applied Generative AI. We will focus on practical application of LLMs using LangChain.
The content of this repository is not meant to be self-served. It is meant to be used in conjunction with the workshop.
Enjoy the workshop!

## Azure Resources

We will use Azure OpenAI for this workshop.
Make sure you have a valid Azure subscription with credits, and an Azure OpenAI resource set up.
Once you have the set, you can follow the instructions below to deploy a model.

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

    b. On windows, please add this to your user-settings json file: `"dev.containers.forwardWSLServices": false`
    (or with GUI: `ctrl+shift+p` --> enter this in the search box: `"dev.containers.forwardWSLServices"` and uncheck it. restart VS Code afterwards.)

    b. Install the Dev-Containers extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

    c. Clone this repository to your local machine.

    d. In Visual Studio Code, open the command pallette (Cmd/Ctrl+Shift+P) and run the command dev "Dev Containers: Open Folder in Container"

    f. Wait until the container is built and the workspace is opened in the container.

3. That's it! (The magic of dev-containers 😉)

### Manual Installation (Not recommended)

Skip this if you are using dev-containers.

1. Python
    
    a. You will need a [Python 3.9](https://www.python.org/downloads/) environment. You can install it globally or use a virtual environment, but make sure you are using Python 3.9.
    If you do this manually, I strongly suggest using [pyenv](https://github.com/pyenv/pyenv)
    
    b. Activate your python 3.9 environment and validate:
    ```bash
    python --version
    ```

2. Jupyter Notebook

    a. Install [Jupyter Notebook](https://jupyter.org/install)

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

4. Install the required VS Code extensions (found in `devcontainer.json`)

5. Just command runner

    a. Install [Just](https://github.com/casey/just)

    b. Validate:
    ```bash
    just --version
    ```

### Setup
1. Clone the repository
2. Execute `cp .env.template .env`
3. Fill in the `.env` file with your OpenAI API key and endpoint, taken from [Azure OpenAI Studio](https://oai.azure.com/portal)

These appear in the "Keys and Endpoint" tab, under "Resource Management" in the Azure portal.