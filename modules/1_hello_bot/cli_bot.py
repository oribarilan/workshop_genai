# Exercise:
# Create a command line chatbot that can talk to a user about a specific topic.
# Give your chatbot a personality and a name.
# Optionally, give your bot some knowledge about the topic you want to talk about, in the system meesage.
# If conversation is too difficult for you, you can create a simple question-answer bot.

from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage, AIMessage
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

model = AzureChatOpenAI(
    api_version=api_version,  # type: ignore
    azure_deployment=deployment_name,
)

sys_msg = SystemMessage(
    content="You are an awkward dad, that always makes dad jokes. You are talking to your son."
)

msgs: list[BaseMessage] = [sys_msg]
bot_msg = "Hey son, how are you doing today?"
msgs.append(AIMessage(content=bot_msg))
print(bot_msg)
while True:
    user_input = input(">>> ")
    user_msg = HumanMessage(content=user_input)
    msgs.append(user_msg)
    response = model.invoke(msgs)
    print(response.content)
    if user_input == "exit":
        break
