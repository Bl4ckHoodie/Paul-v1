# @author: mac
"""
==============================================
"""
import os
import time
import datetime
def checkAlarm():
   current = datetime.datetime.now()
   h = current.hour
   m = current.minute
   tm = h+":"+m
   turn = 0
   file = open("Alarm/alarm.txt","r")
   for i in file:
      if i == tm:
         turn = 1;
   file.close()
   while turn == 1:
      playalarm()
      turn = input("Enter '0' to turn off >>")
def playalarm():
    os.system("mpg321 Alarm/m1.mp3")
onoff = "off"    
while (onoff == "off"):
   time.sleep(30)
   checkAlarm()  