from pathlib import Path

from dotenv import load_dotenv

_ = load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults


tool = TavilySearchResults(max_results=4) #increased number of results
print(type(tool))
print(tool.name)


