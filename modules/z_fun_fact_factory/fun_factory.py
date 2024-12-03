import os
import random

from dotenv import load_dotenv
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, Field


class FunFact(BaseModel):
    fact: str = Field(description="A fun fact that is either true or false.")
    is_true: bool = Field(description="Whether the fact is true or false.")


class InMemoryHistory(BaseChatMessageHistory, BaseModel):
    messages: list[BaseMessage] = Field(default_factory=list)

    def add_messages(self, messages: list[BaseMessage]) -> None:  # type: ignore
        self.messages.extend(messages)

    def clear(self) -> None:
        self.messages = []


class FunFactory:
    def __init__(self):
        load_dotenv()
        key = os.getenv("AZURE_OPENAI_API_KEY")
        endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        deployment_name = os.getenv("DEPLOYMENT_NAME")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        assert (
            key and endpoint and deployment_name and api_version
        ), "Please set the environment variables"
        llm = AzureChatOpenAI(
            api_version=api_version,  # type: ignore
            azure_deployment=deployment_name,
            temperature=1,
        )

        self.generator_chain = self._init_generator_chain(llm=llm)
        self.followup_chain_true = self._init_followup_chain(llm=llm)

    def _init_generator_chain(self, llm: AzureChatOpenAI) -> Runnable:
        SYS_MSG = """
        You are a witty game host. Generate a random fun fact that is either true or false about {topic}.
        """

        parser = PydanticOutputParser(pydantic_object=FunFact)
        prompt = PromptTemplate(
            template=SYS_MSG + "\n{format_instructions}",
            input_variables=["topic"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | llm | parser

        return chain

    def _init_followup_chain(self, llm: AzureChatOpenAI) -> Runnable:
        SYS_MSG = """
        You are a witty game host. You generate random fun facts that are either true or false.
        The user has guessed if the fact is true or false.
        Respond with the correct answer.
        If true, provide more information about the fact.
        If false, make a witty comment about the false fact and/or provide a true fact that is very similar.
        """

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", SYS_MSG),
                ("ai", "{fact}"),
                ("human", "{answer}"),
            ]
        )

        chain = prompt | llm

        return chain

    def generate_fun_fact(self) -> FunFact:
        topic = self.roll_topic()
        return self.generator_chain.invoke({"topic": topic})

    def generate_followup(self, fact: FunFact, is_true: bool) -> str:
        response = self.followup_chain_true.invoke(
            {"fact": fact.model_dump_json(), "answer": str(is_true)}
        )
        return response.content

    def roll_topic(self) -> str:
        topics = [
            "Technology",
            "Animals",
            "Galaxy",
            "History",
            "Science",
            "Food",
            "Sports",
            "Movies",
            "Music",
            "Literature",
            "Art",
            "Nature",
            "Geography",
            "Space",
            "Inventions",
            "Famous People",
            "Mythology",
            "Languages",
            "Plants",
            "Oceans",
            "Weather",
            "Human Body",
            "Cultural Traditions",
            "Architecture",
            "Fashion",
            "Holidays",
            "Transportation",
            "Education",
            "Robots",
            "Computers",
        ]
        return random.choice(topics)
