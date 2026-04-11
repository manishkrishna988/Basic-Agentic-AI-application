from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Debug check
openai_key = os.getenv("OPENAI_API_KEY")
print("OPENAI_API_KEY:", openai_key)

if not openai_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

# Create one shared OpenAI model instance
openai_model = OpenAIChat(
    id="gpt-4o-mini",
    api_key=openai_key
)

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=openai_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=openai_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Multi-modal AI agent configuration
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    model=openai_model,
    instructions=[
        "Always include sources",
        "Use tables to display the data"
    ],
    show_tool_calls=True,
    markdown=True,
)

# Run Query
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA",
    stream=True,
)