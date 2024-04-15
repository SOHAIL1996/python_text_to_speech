#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Software License Agreement (BSD)
#
# @author    Salman Omar Sohail <sorox23@gmail.com>
# @copyright (c) 2024, Salman Omar Sohail, Inc., All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Salman Omar Sohail nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

# Redistribution and use in source and binary forms, with or without
# modification, is not permitted without the express permission
# of Salman Omar Sohail.

'''
A Class for quick text to speech (tts).
'''

import time
import inflect 
from termcolor import colored

# Chatgpt
import os
from openai import OpenAI
from pathlib import Path
import json

# Google Text to Speech
from gtts import gTTS
import playsound

# Espeak Text to Speech
import pyttsx3

# Transformer Text to Speech
# import torch
# import soundfile as sf
# import playsound
# import time
# from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
# from datasets import load_dataset

class GPT():
    '''
    Quick GPT Example.

    Install via:
    
    pip install openai
    '''
    def __init__(self) -> None:
        API_KEY = 
        self.client = OpenAI(
        api_key=API_KEY, 
        )

    def chatgpt_single_query(self, question:str):

        model_id = "gpt-4" # gpt-3.5-turbo

        conversation = []

        conversation.append({"role": "system", 
                             "content": "You are a robotic expert."})
        
        conversation.append({"role": "user", 
                             "content": question})
        
        response = self.client.chat.completions.create(model=model_id,
                                                messages=conversation)
        return response.choices[0].message.content
    
    def chatgpt_function_query(self, question:str):

        model_id = "gpt-4" # gpt-3.5-turbo

        conversation = []

        conversation.append({"role": "system", 
                             "content": "You are a robotic expert."})
        
        conversation.append({"role": "user", 
                             "content": question})
        
        function_callback = []

        function_callback.append({"type": "function",
                                  "function":{
                                  "name": "chatgpt_call_tts", 
                                  "description": "Converting the provided user question to speech",
                                  "parameters":{
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                        "type": "string",
                                        "description": "The text for which Text-to-Speech (TTS) conversion is requested."
                                        }
                                    },
                                    "required": ["text"]}
                                    }})
        
        function_callback.append({"type": "function",
                                  "function":{
                                  "name": "chatgpt_test", 
                                  "description": "Prints User Speech",
                                  "parameters":{
                                    "type": "object",
                                    "properties": {
                                        "text": {
                                        "type": "string",
                                        "description": "Prints User questions"
                                        }
                                    },
                                    "required": ["text"]}
                                    }})
        
        response = self.client.chat.completions.create(model=model_id,
                                                messages=conversation,
                                                tools=function_callback,
                                                tool_choice='auto',
                                                temperature=0)
        
        response_message = response.choices[0].message

        print(response)

        try:
            for function_calls in response_message.tool_calls:
                print(colored(f'Activating Function: {function_calls.function.name}', 'blue'))
                if function_calls.function.name == 'chatgpt_call_tts':
                    arguments_dict = json.loads(function_calls.function.arguments)
                    text_content = arguments_dict.get('text', '')
                    self.chatgpt_call_tts(text_content)
                
                if function_calls.function.name == 'chatgpt_test':
                    arguments_dict = json.loads(function_calls.function.arguments)
                    text_content = arguments_dict.get('text', '')
                    self.chatgpt_test(text_content)
        except TypeError:
            print(colored(f'No suitable function found!', 'red'))

    def chatgpt_audio(self, text:str):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = self.client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
        )
        response.stream_to_file(speech_file_path)

    def chatgpt_test(self,text):
        print(text)
        return True

    def chatgpt_call_tts(self,text):

        tts = gTTS(text, lang='en')
        tts.save("google_speaker.mp3")
        playsound.playsound("google_speaker.mp3")
        return True

class MultiTextToSpeech():

    def google_tts(self, text):
        '''
        Quick TTS Online Example.

        Install via:
        
        pip install soundfile gtts 
        '''
        tts = gTTS(text, lang='en')
        tts.save("google_speaker.mp3")
        playsound.playsound("google_speaker.mp3")

    def mozilla_tts(self, text):
        '''
        TTS Offline Example.

        Install via:
        
        pip install TTS
        sudo apt-get install espeak-ng

        Check Models: 

        tts --list_models or print(TTS().list_models())
        '''
        import torch
        from TTS.api import TTS
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tts = TTS(model_name='tts_models/en/jenny/jenny')
        tts.tts_to_file(text=text, file_path="google_speaker.mp3")
        playsound.playsound("google_speaker.mp3")

    def espeak_tts(self, text):
        '''
        Quick TTS Offline Example.

        Install via:
        
        pip3 install libespeak1 
        sudo apt-get install libespeak1 espeak 
        '''
        engine = pyttsx3.init('espeak') 
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

class TransformerTextToSpeech():

    def __init__(self) -> None:
        '''
        Recommended TTS Offline Example using Transformer.

        Install via:
        
        pip install soundfile transformers datasets sentencepiece torch numpy==1.21.6 
        '''        
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts").to(self.device)
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan").to(self.device)
        self.embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")

    def save_text_to_speech(self, text, speaker='slt', output_filename = f"google_speaker.wav"):

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

        inputs = self.processor(text=text, return_tensors="pt").to(self.device)
        speaker_embeddings = torch.tensor(self.embeddings_dataset[speaker_id]["xvector"]).unsqueeze(0).to(self.device)
        speech = self.model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=self.vocoder)
        sf.write(output_filename, speech.cpu().numpy(), samplerate=16000, format='wav', subtype='PCM_16')
        playsound.playsound(output_filename)    
        # return output_filename
    
if __name__ == '__main__':

    infl = inflect.engine()
    text = f"{infl.number_to_words(3.0)} cookies are sufficient for good health"

    ts = GPT()
    ts.chatgpt_function_query(text)

    # ts = MultiTextToSpeech()
    # ts.espeak_tts(text)
    # ts.mozilla_tts(text)

    # ts = TransformerTextToSpeech()
    # ts.save_text_to_speech(text)
