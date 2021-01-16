# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:23:42 2020

@author: mac
"""
def logo():
    print("                                           | ")
    print("                       ____________    __ -+-  ____________ ")
    print("                       \_____     /   /_ \ |   \     _____/")
    print("                        \_____    \____/  \____/    _____/")
    print("                         \_____                    _____/")
    print("                            \___________  ___________/")
    print("                                      /____\ ")
    print("__________             .__    _________                                          .___      ")
    print("\______   _____   __ __|  |   \_   ___ \  ____   _____   _____ _____    ____   __| _/______")
    print(" |     ___\__  \ |  |  |  |   /    \  \/ /  _ \ /     \ /     \\__  \  /    \ / __ |/  ___/")
    print(" |    |    / __ \|  |  |  |__ \     \___(  <_> |  Y Y  |  Y Y  \/ __ \|   |  / /_/ |\___ \ ")
    print(" |____|   (____  |____/|____/  \______  /\____/|__|_|  |__|_|  (____  |___|  \____ /____  >")
    print("               \/                     \/             \/      \/     \/     \/     \/    \/ ")
    print("")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
def sysCommands():
    print("SYSTEM COMMANDS:- \n")
    print("&& Still to be updated &&")
    print("")
    print("")
    

def genCommands():
    print("GENERAL COMMANDS:-\n")
    print("-- Show Commands         Displays all commands that can be executed by paul v1.0")
    print("-- News Update           Displays and reads out the latest news and news source")
    print("-- Weather Update        Displays the weather at location of the current ip address")
    print("-- Wiki search Newton    Searches and displays information on Isaac Newton from Wikipidia")
    print("-- Set Alarm             Enable you to set an alarm that will greet you with news and weather update")
    print("-- Get Alarm             Displays the time of which the set alarm will go off")
    print("-- Set Reminder          Enables user to set reminder for a certain date with description")
    print("-- Get Reminder          Displays a reminder that was set for specific date")
    print("-- Google *              Uses the google search engine and displays results and url")
    print("-- Get info on *         Displays information of a user stored in local database")
    print("-- Stop Listening        Stops listening until a specific phrase is said")
    print("-- Start Listening       Brings paul back online and ready to execute commands")
    print("-- Exit                  Stops the assistant from listening")
    print("-- Black Hat Mode        High level access that is only given to admin users\n")

def showCommnds():
    logo()
    genCommands()
    sysCommands()
    return 'Here you go'