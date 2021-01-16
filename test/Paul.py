#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:21:51 2019

@author: n3uro
"""
import os
from gtts import gTTS
import Interpreter
#from googlesearch.googlesearch import GoogleSearch
import aiml

kernel = aiml.Kernel()
#def Google(ln):
#    response = GoogleSearch().search(ln)
#    result = response.results
#    return[ result.getText()
def Goodbye():
    print("GoodBye")
    tts = gTTS(text='GoodBye', lang='en')
    tts.save('speech.mp3')
    os.system('mpg321 speech.mp3')
if os.path.isfile("Paul_brain.brn"):
   kernel.bootstrap(brainFile = "Paul_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml",commands = "load aiml b")
    kernel.saveBrain("Paul_brain.brn")
# kernel now ready for use
while True:
    message = input("User >> ")
    if message.upper() == "EXIT":
        Goodbye()
        break
    else: 
        respon = kernel.respond(message)
        bot = Interpreter.users(respon)
        print("Paul >> "+bot)
        tts = gTTS(text=bot, lang='en')
        tts.save('speech.mp3')
        os.system('mpg321 speech.mp3')
        

    
