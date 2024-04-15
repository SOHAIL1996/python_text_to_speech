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
A Class for quick speech to text (stt).

pip3 install SpeechRecognition pyaudio pocketsphinx vosk
'''
import sys
import os
import json
import time
import speech_recognition as sr

class SpeechToText():
    
    def __init__(self) -> None:

        self.voice_recognizer = sr.Recognizer()
        self.original_stdout = sys.stdout

    def record_speech(self):        

        try:
            with sr.Microphone() as mic:

                print(f'{self.colorize('Recording Started', 'green')}')
                strt_time = time.time()
                self.voice_recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.voice_recognizer.listen(mic)
                print(f'{self.colorize(f'Recording Completed! Processing Audio! Processing time: {time.time() - strt_time}', 'yellow')}')

                strt_time = time.time()
                online_google_recognized_text = self.voice_recognizer.recognize_google(audio)
                print(f'{self.colorize(f'Processing time Google: {time.time() - strt_time}', 'yellow')}')

                strt_time = time.time()
                offline_sphinx_recognized_text = self.voice_recognizer.recognize_sphinx(audio) 
                print(f'{self.colorize(f'Processing time Sphinx: {time.time() - strt_time}', 'yellow')}')

                # strt_time = time.time()
                # # Disable vosk model output
                # sys.stdout = open(os.devnull, "w")
                # offline_vosk_recognized_text = self.voice_recognizer.recognize_vosk(audio_data=audio) # vosk models: https://alphacephei.com/vosk/models
                # offline_vosk_recognized_text = json.loads(offline_vosk_recognized_text)
                # offline_vosk_recognized_text = offline_vosk_recognized_text["text"]
                # sys.stdout.close()
                # sys.stdout = self.original_stdout
                # print(f'{self.colorize(f"Processing time Vosk: {time.time() - strt_time}", "yellow")}')

                print(f'You said: {self.colorize(online_google_recognized_text, 'orange')}')
                print(f'You said: {self.colorize(offline_sphinx_recognized_text  , 'orange')}')
                # print(f'You said: {self.colorize(offline_vosk_recognized_text  , 'orange')}')

        except sr.UnknownValueError:
            print(f"{self.colorize('Unable to recognize speech','red')}")
        except sr.RequestError as e:
            print(f"{self.colorize('Could not request results from IBM Speech to Text service','red')} {e}")
                
    def colorize(self, text, color):
        color_codes = {
            'green': '\033[92m',
            'yellow': '\033[93m',
            'orange': '\033[38;5;208m', 
            'blue': '\033[94m',
            'red': '\033[91m'
        }
        return color_codes[color] + text + '\033[0m'
    
if __name__ == '__main__':

    sst = SpeechToText()
    sst.record_speech()