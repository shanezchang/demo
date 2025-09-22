import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="x-ai/grok-4-fast:free",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    temperature=0.6,
    max_tokens=1024,
    timeout=60,
    max_retries=3,
)

rsp = llm.invoke("Hello how are you?")

print(rsp)


def main():
    print("Hello from demo!")


if __name__ == "__main__":
    main()
