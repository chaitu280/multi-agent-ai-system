import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is missing."
    )


llm = ChatOpenAI(
    model="gpt-6-luna",
    api_key=OPENAI_API_KEY,
    reasoning_effort="none",
)