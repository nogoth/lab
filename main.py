from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
import re

import torch
from TTS.api import TTS
import sounddevice as sd


def speak_it(content: str):
  # TODO: abstract this tts set up out of a single method...
  # cargo cult, might not really care to try and cuda since laptop is intel gpu
  device = "cuda" if torch.cuda.is_available() else "cpu"
  tts = TTS("tts_models/en/ljspeech/glow-tts")#.to(device)
  wav = tts.tts(text=content)
  sd.play(wav, samplerate=22050)
  sd.wait() # Wait until file is done playing

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
  temperature = 2.2
  llm = ChatOllama(model=model, temperature=temperature) # reasoning=False) # for not think
  response = llm.invoke([HumanMessage(content="Tell me a story, in the style of Hansel and Gretel, that is at least 30 sentences long")])
  print(removeThinks(response.content))
  print(response.content)
  #now say it... i hope
  speak_it(removeThinks(response.content))


talkToServer()

