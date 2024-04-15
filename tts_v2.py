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

import inflect 
import pygame # Steamdeck Exclusive

class MultiTextToSpeech():
        
    def mozilla_tts(self, text):
        '''
        TTS Offline Example.

        Install via:
        
        pip install TTS pygame
        sudo apt-get install espeak-ng

        Check Models: 

        tts --list_models or print(TTS().list_models())
        '''
        import torch
        from TTS.api import TTS
        device = "cuda" if torch.cuda.is_available() else "cpu"

        tts = TTS(model_name='tts_models/en/jenny/jenny')
        tts.tts_to_file(text=text, file_path="/home/deck/ros2_ws/log/google_speaker.mp3")
        
        pygame.mixer.init()
        sound = pygame.mixer.Sound("/home/deck/ros2_ws/log/google_speaker.mp3")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))

if __name__ == '__main__':

    infl = inflect.engine()
    text = f"{infl.number_to_words(45.0)} cookies are sufficient for good health"

    ts = MultiTextToSpeech()
    # ts.google_tts(text)
    ts.mozilla_tts(text)