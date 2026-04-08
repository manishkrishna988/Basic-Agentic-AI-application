from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo


# First agent will be used for websearch
web_search_agent = Agent(
    name = "Web search agent",
    role = "Search the web for information",
    model = Groq(id="groq/compound"),
    tools = [DuckDuckGo()],
    instructions = ["Always include sources"],
    show_tool_calls = True,
    markdown = True,

)
