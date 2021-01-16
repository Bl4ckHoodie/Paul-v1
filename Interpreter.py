'''
Load comment line and check if whether the dictation exist
among the required command set
'''
import WebSearch
import Info
import Weather
import News
import Alarmset
import Remind
import Settings
from Admin import Admin

def users(ln):
 word = ''
 for c in ln:
  word += c
  if word.lower() =="google":
    ln = str(ln).lower().replace("google ","")
    WebSearch.Google(ln)
    ln = "done googling"
  elif word.lower() == "wiki":
    ln =  str(ln).lower().replace("wiki ","")
    ln = WebSearch.Wiki(ln)
  elif word.lower() == "info ":
    ln = str(ln).lower().replace("info ","").upper()
    Info.Find()
    ln = "done"
  elif word.lower() == "news":
    ln = News.GetNews() 
  elif word.lower() == "setreminder":
    ln = Remind.setReminder()
  elif word.lower() == "getreminder":
    ln = Remind.getReminder() 
  elif word.lower() == "commands":
    Settings.clear()
    ln = Settings.show_commands()
  elif word.lower() == "blackhat":
    Settings.clear()
    ln = Admin.login()
  elif word.lower() == "setalarm":
    ln = Alarmset.setAlarm()
  elif word.lower() == "getalarm":
    ln = Alarmset.getAlarm()
  elif word.lower() == "getweather":
    ln = Weather.getWeather()
  else: 
     ln = ln
 return ln
