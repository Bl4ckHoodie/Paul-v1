import time
import Voice
import Weather
import Settings
# -*- coding: utf-8 -*-
def alarmtime():
	if Settings.search("alarmtime") != "error 4b":
		return Settings.search("alarmtime")
	else:
		return "error 6a" 
def gettime():
	t = time.localtime()
	return time.strftime("%H:%M", t)

def test():
	if Settings.search("setalarm")!="error 14b":
		return Settings.search("setalarm").lower()
	else:
		return "error 14b"
def MornGreet():
	ln = "Good morning, Sir!"
	loc = Settings.search("currentloc")
	temp = Weather.monWeather(loc)
	greet = ln + temp
	Voice.Speak(greet)
print("Paul Alarm is online and ready\n\nAlarm set for "+str(alarmtime()))        
while test():
	time.sleep(20)
	if alarmtime() != "error 6a":
		if str(gettime()) == str(alarmtime()).replace("\n",""):
			MornGreet()
			time.sleep(60)
    