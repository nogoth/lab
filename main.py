from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
import re

def removeThinks(message: AIMessage):
    regex_pattern = r'<think>[\s\S]*?</think>'
    return  re.sub(regex_pattern, '', message)

def talkToServer():
  print("hi")
  # Requires ollama be installed and a model downloaded
  #  ollama pull qwen3:1.7b
  # note: chatollama works with servers that are ollama starters not mozilla-ocho/llama.cpp servers
  model = "llava-v1.5-7b"
  model = "qwen3:1.7b"
  llm = ChatOllama(model=model, temperature=0.7) # reasoning=False) # for not think
  response = llm.invoke([HumanMessage(content="Hello, how are you?")])
  print(removeThinks(response.content))
  print(response.content)

talkToServer()

