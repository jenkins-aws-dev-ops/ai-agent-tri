from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import argparse
parser = argparse.ArgumentParser(description="A Python script with arguments.")
parser.add_argument('-q', '--query', type=str, help="Your query", required=True)
args = parser.parse_args()
load_dotenv()

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    # tools=[YFinanceTools(stock_price=True,analyst_recommendations=True, stock_fundamentals=True)],
    # show_tool_calls=True,
    # markdown=True,
    # instructions=["Use tables to display data."]
)
agent.print_response(f"{args.query}")