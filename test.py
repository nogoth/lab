import torch
import sounddevice as sd
from TTS.api import TTS

# Get device. You can specify a different device if needed.
device = "cuda" if torch.cuda.is_available() else "cpu"

model = "tts_models/en/ljspeech/glow-tts"
model = "tts_models/multilingual/multi-dataset/xtts_v2" #this fails some torch weight issue
model = "tts_models/de/thorsten/tacotron2-DDC"
model = "tts_models/en/vctk/vits"
# Init TTS
tts = TTS(model).to(device)

# The text you want to synthesize
text_to_speak = "This is a test of the Coqui TTS library." +"This is a test of the Coqui TTS library." +"This is a test of the Coqui TTS library." +"This is a test of the Coqui TTS library." 

# Generate audio data
wav = tts.tts_with_vc(text=text_to_speak,
#wav = tts.tts(text=text_to_speak,
                      speaker_wav="voices/ben.wav",
                      speaker="p330")

# Play the audio
sd.play(wav, samplerate=22050)
sd.wait() # Wait until file is done playing
