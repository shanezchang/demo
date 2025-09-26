import os

from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    task="访问 http://www.people.com.cn/ 人民网，获取最新的时政信息，并选择有价值的可能可以总结出申论的主题话题文章，点击进去看详细的内容，并且输出一篇申论题目，然后根据读取的文章内容输出申论答题的内容答案。",
    llm=ChatOpenAI(
        model="x-ai/grok-4-fast:free",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        temperature=0.6,
        timeout=60,
        max_retries=3,
    ),
)
agent.run_sync()
