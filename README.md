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
4. select "gpt-4o-mini" as the model (don't worry, you can deploy other models later)

(full instructions sent separately)

## Installation

Throughout the workshop, we will use dev-containers to minimize the setup time and ensure alignment between participants.
You may choose to avoid dev-containers and set up your local environment. 
However, I will have limited capacity to help you with the setup during the workshop.
If you do choose to set up your local environment, please follow the manual instructions in the next section below.

Once you are dont with the installation, you can proceed to the [Setup](#setup) section at the bottom.

### Dev Containers (Recommended)

#### Prerequisites

Follow the instructions here: https://code.visualstudio.com/docs/devcontainers/containers#_installation.
Windows users, not the WSL 2 instructions.

For any issues, refer to the [Trouble Shooting](#trouble-shooting) section below.

#### Coding in a Container

1. Install Visual Studio Code: https://code.visualstudio.com/

2. Install the Dev-Containers extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

3. Clone this repository to your local machine.

4. In Visual Studio Code, open the command pallette (Cmd/Ctrl+Shift+P) and run the command dev "Dev Containers: Open Folder in Container"

5. In the small pop-up, click the `(show logs)` link to enjoy the show. 😄

6. Wait until the container is built and the workspace is opened in the container.

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

## Setup

1. Clone the repository
2. Execute `cp .env.template .env`
3. Fill in the `.env` file with your OpenAI API key and endpoint, taken from [Azure OpenAI Studio](https://oai.azure.com/portal)

These appear in the "Keys and Endpoint" tab, under "Resource Management" in the Azure portal.

## Trouble Shooting

### Any issues with the dev-container

1. Make sure you are running the most up-to-date Docker Desktop version.
2. Make sure you are running the most up-to-date VSCode Dev Container extension.
3. Restart VSCode.
4. Try again.

### Validate Docker Installation

Validate the installation by running the following command in your terminal:
```bash
docker --version
```

### WSL Version

Windows users: Please run `wsl --update` in the terminal as an administrator. This will update your WSL2 kernel to the latest version.
If you experience issues, try referring this: [Get started: Prep Windows for containers
](https://learn.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=dockerce)

### VS Code Settings
Add this to your user-settings json file: `"dev.containers.forwardWSLServices": false`
    
Or, using the GUI: `ctrl+shift+p` --> `Preferences: Open User Settings` --> enter this in the search box: `"dev.containers.forwardWSLServices"` and uncheck it. restart VS Code afterwards.

Consider turning this back to `true` after the workshop, if required.

### Dev container won't mount the workspace

Make sure your Docker allows file sharing on this folder
(Something like `Settings --> Resource --> File Sharing` and add this repo folder)