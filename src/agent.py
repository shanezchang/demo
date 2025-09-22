import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

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


def send_email(to: str, subject: str, body: str):
    """Send an email"""
    email = {
        "to": to,
        "subject": subject,
        "body": body
    }
    # ... email sending logic
    print(email)

    return f"Email sent to {to}"


agent = create_react_agent(
    model=llm,
    tools=[send_email],
    prompt="You are an email assistant. Always use the send_email tool.",
)
