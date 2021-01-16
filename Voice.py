# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:56:11 2019

@author: mac
Function voice
"""
import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
def Speak(words):
    engine.say(str(words))
    engine.runAndWait()
    engine.stop()

