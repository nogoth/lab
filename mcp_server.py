from fastmcp import FastMCP

import torch
from TTS.api import TTS
import sounddevice as sd



from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# rough set up of tts server
model = "tts_models/en/ljspeech/glow-tts"
voice_model = "tts_models/en/vctk/vits"
#  device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(voice_model)#.to(device)

def setup_ollama_chain()-> callable:
  llm = ChatOllama(model="qwen3:1.7b", temperature=1.0,tokens=256, reasoning=False)
  prompt = ChatPromptTemplate.from_template("You are a helpful AI assistant. Answer concisely the question: {question}")
  chain = prompt | llm | StrOutputParser()
  return chain

ollama_chain = setup_ollama_chain()

mcp = FastMCP("speakingExample")

def internallyspeak(content: str):
  wav = tts.tts(text=content, speaker="p330")
  sd.play(wav, samplerate=22050)
  sd.wait() # Wait until file is done playing
@mcp.tool
def speak_it(content: str):
  """Speaks the provided text content.

  This function takes a string as input and uses the system's text-to-speech
  capabilities to vocalize the content.

  Args:
      content (str): The string of text to be spoken aloud.
  """
  internallyspeak(content)

@mcp.tool
def ask_ollama_question(question: str) -> str:
  """Ask a question to an Ollama model and returns the response.

  This function sends a question to a specified Ollama model and retrieves
  the model's response. Questions have question marks.

  Args:
      question (str): The question to be asked to the Ollama model. it should have a question mark in it. 

  Returns:
      str: The response from the Ollama model.
  """

  internallyspeak(f"asking ollama the question: {question}")
  response = ollama_chain.invoke({"question": question})
  return response

@mcp.tool
def send_notification_to_app(app: str="print", message: str="Hello from MCP!"):
  """Sends a notification message to a specified app.

  This function sends a notification message to a given app. The default
  app is "print".

  Args:
      app (str): The name of the app to send the notification to.
                     Defaults to "print".
      message (str): The notification message to be sent. Defaults to
                     "Hello from MCP!".
  """
  if app == "print":
    print(f"Notification sent to {app}: {message}")
  else:
    print(f"Notification not sent to {app}: {message}")

mcp.run(transport="http")
