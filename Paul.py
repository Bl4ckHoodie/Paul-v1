#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 10:21:51 2019

@author: n3uro
"""
import os
#from gtts import gTTS
import Interpreter
import Voice
#from googlesearch.googlesearch import GoogleSearch
import aiml
import Check
kernel = aiml.Kernel()
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#def Google(ln):
#    response = GoogleSearch().search(ln)
#    result = response.results
#    return[ result.getText()
def Goodbye():
    print("GoodBye")
    Voice.Speak("Goodbye")
#    tts = gTTS(text='GoodBye', lang='en')
#    tts.save('speech.mp3')
#    os.system('mpg321 speech.mp3')
if os.path.isfile("Paul_brain.brn"):
   kernel.bootstrap(brainFile = "Paul_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml",commands = "load aiml b")
    kernel.saveBrain("Paul_brain.brn")
# kernel now ready for use
def Listening():
    message = 'listening'
    while (message != 'stop listening'):
        if (Check.Check()!= 0):
            bot = Check.Check()
            print("Paul >> "+bot)
            Voice.Speak(''+str(bot))
#            tts = gTTS(text=bot, lang='en')
#            tts.save('speech.mp3')
#           os.system('mpg321 speech.mp3')
            message = input("User >> ")
        if message.upper() == "EXIT":
            Goodbye()
            break
        else:
            message = input("User >> ")
            if (message != "stop listening"):
             respon = kernel.respond(message)
             bot = Interpreter.users(respon)
             print("Paul >> "+bot)
             Voice.Speak(''+str(bot))
#             tts = gTTS(text=bot, lang='en')
#             tts.save('speech.mp3')
    #        os.system('mpg321 speech.mp3')
    print("Paul >> I am offline")
    Voice.Speak("I am offline")
    Waiting()
def Waiting():
    message = input("User >> ")
    while(message != 'start listening'):
            message = input("User >> ")
    print("Paul >> I am online and ready")
    Voice.Speak("I am online and ready")
    Listening()
Listening()