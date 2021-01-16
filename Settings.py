# -*- coding: utf-8 -*-
import Commands
import os
from sys import executable
from subprocess import Popen, CREATE_NEW_CONSOLE

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def search(setting):
    try:
        line =""
        com ="false"
        file = open("Admin/settings.txt","r")
        for ln in file:
            line = ""
            for i in ln:
                line += str(i)
                if line.lower() == str(setting):
                    com = str(ln).lower().replace(str(setting)+": ","")
        file.close()
    except:
        return "error 14b"
    return com
def show_commands():
    resp = Commands.showCommnds()
    return resp
    
def clear():
    try:
        clear = lambda : os.system("cls")#if Windows Console
    except:
        clear = lambda : os.system("clear")#if Linux Console
    clear()

def exeScript():
    Popen([executable, 'Morning.py'], creationflags=CREATE_NEW_CONSOLE)