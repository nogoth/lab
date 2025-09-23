from fastmcp import FastMCP

import torch
from TTS.api import TTS
import sounddevice as sd

# rough set up of tts server
model = "tts_models/en/ljspeech/glow-tts"
model = "tts_models/en/vctk/vits"
#  device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model)#.to(device)

mcp = FastMCP("speakingExample")

@mcp.tool
def speak_it(content: str):
  """Speaks the provided text content.

  This function takes a string as input and uses the system's text-to-speech
  capabilities to vocalize the content.

  Args:
      content (str): The string of text to be spoken aloud.
  """
  wav = tts.tts(text=content, speaker="p330")
  sd.play(wav, samplerate=22050)
  sd.wait() # Wait until file is done playing


mcp.run(transport="http")
