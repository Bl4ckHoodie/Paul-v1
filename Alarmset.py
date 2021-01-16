def setAlarm ():
    time = asktime()
    return addAlarm(time)

def asktime():
    return input("Enter time #hh:mm: ")
                
def addAlarm(time,date):
    try:
      file = open("Alarm/alarm.txt","a")
      file.writelines(time+"\n")
      file.close()
    except:
      file = open("Alarm/alarm.txt","w")
      file.writelines(time+"\n")
    return "Alarm successfully added"

def getAlarm():
    try:
        file = open("Alarm/alarm.txt","r")
        for i in file:
            print(i)
        return "Done displaying all alarms"
    except:
        return "Alarm file could not be found"