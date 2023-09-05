#!/usr/bin/env python3

######################## Online Example
from gtts import gTTS
import playsound

text = "Robot is Navigating to x coordinate: 0.5 meters and to y coordinate: 3 meters"
tts = gTTS(text, lang='en')
tts.save("/home/administrator/Downloads/output.mp3")

playsound.playsound("/home/administrator/Downloads/output.mp3")

######################## Offline Example

# sudo apt-get install libespeak1 espeak 
# pip3 install libespeak1 

import pyttsx3

text = "Robot is Navigating to x cordinate: 0.5 meters"

engine = pyttsx3.init('espeak') # espeak
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)

# engine.setProperty('pitch', 0)
engine.setProperty('voice', 'mb-en1')
engine.setProperty('rate', int(engine.getProperty('rate')*0.5))
engine.setProperty('volume', 0.8)
engine.say(text)
engine.runAndWait()

######################## Transformer Example

# pip install soundfile transformers datasets sentencepiece torch

import inflect
import torch
import soundfile as sf
import playsound
import time

from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset

infl = inflect.engine()
device = "cuda" if torch.cuda.is_available() else "cpu"
start_time = time.time()
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(device)
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(device)
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
end_time = time.time()
print(f"Time taken for Preprocessing: {end_time - start_time} seconds")

def save_text_to_speech(text, speaker='slt'):

    speakers = {
    'awb': 0,     # Scottish male
    'bdl': 1138,  # US male
    'clb': 2271,  # US female
    'jmk': 3403,  # Canadian male
    'ksp': 4535,  # Indian male
    'rms': 5667,  # US male
    'slt': 6799   # US female
    }

    if speaker in speakers:
        speaker_id = speakers[speaker]
    else:
        speaker_id = speakers['clb']  # Use 'clb' as the default speaker

    inputs = processor(text=text, return_tensors="pt").to(device)

    speaker_embeddings = torch.tensor(embeddings_dataset[speaker_id]["xvector"]).unsqueeze(0).to(device)

    start_time = time.time()
    speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
    end_time = time.time()
    print(f"Time taken for TTS generation: {end_time - start_time} seconds")

    output_filename = f"/home/administrator/Downloads/transformer_speaker.wav"
    start_time = time.time()
    sf.write(output_filename, speech.cpu().numpy(), samplerate=16000, format='wav', subtype='PCM_16')
    end_time = time.time()
    print(f"Time taken for File generation: {end_time - start_time} seconds")

    return output_filename

text = f"Robot is Navigating to x cordinate: {infl.number_to_words(0.5)} meters\
         and to y cordinate: {infl.number_to_words(3.0)} meters"
output_filename = save_text_to_speech(text)

playsound.playsound("/home/administrator/Downloads/transformer_speaker.wav")
