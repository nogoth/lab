import asyncio

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
import re
import prompty
import langchain
langchain.debug=True

from langchain.agents import create_react_agent, AgentExecutor
from fastmcp import Client

from langchain_mcp_adapters.tools import load_mcp_tools

def removeThinks(message: AIMessage):
    regex_pattern = r'<think>[\s\S]*?</think>'
    return  re.sub(regex_pattern, '', message)

async def talkToServer():
  print("hi")
  # Requires ollama be installed and a model downloaded
  #  ollama pull qwen3:1.7b
  # note: chatollama works with servers that are ollama starters not mozilla-ocho/llama.cpp servers
  model = "llava-v1.5-7b"
  model = "qwen3:1.7b"
  model = "llama3"
  model = "qwen2.5-coder:7b"
  temperature = 0.0 #lower the temp, the closer it could be to doing real json
  client = Client("http://localhost:8000/mcp")
  async with client:
    mcp_tools = await client.list_tools()
    tools = await load_mcp_tools(client.session)
    print(f"Loaded tools: {[tool.name for tool in tools]}")

    llm = ChatOllama(model=model, temperature=temperature) # reasoning=False) # for not think
    agent = create_react_agent(llm, tools, prompty.REACT_PROMPT) 
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    response = await agent_executor.ainvoke({"input": "using a tool, I would like you to speak two or three sentences. Make them random and rustic."})
    print(response)

asyncio.run(talkToServer())

