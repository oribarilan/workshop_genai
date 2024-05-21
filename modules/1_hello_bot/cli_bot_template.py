# Exercise:
# Create a command line chatbot that can talk to a user about a specific topic.
# Give your chatbot a personality and a name.
# Optionally, give your bot some knowledge about the topic you want to talk about, in the system meesage.
# If conversation is too difficult for you, you can create a simple question-answer bot.

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("DEPLOYMENT_NAME")
api_version = os.getenv("AZURE_OPENAI_API_VERSION")

assert (
    key and endpoint and deployment_name and api_version
), "Please set the environment variables"

while True:
    user_input = input(">>> ")
    print("Replace this with your chatbot's response")
    if user_input == "exit":
        break