#!/usr/bin/env python3

######################## Online Example
from gtts import gTTS
import playsound

text = "Robot is Navigating to x coordinate: 0.5 meters and to y coordinate: 3 meters"
tts = gTTS(text, lang='en')
tts.save("c:/Users/HyperShot/Downloads/output.mp3")

playsound.playsound("c:/Users/HyperShot/Downloads/output.mp3")

######################## Offline Example

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
# engine.setProperty('rate', 150)
engine.setProperty('volume', 0.8)
engine.say(text)
engine.runAndWait()