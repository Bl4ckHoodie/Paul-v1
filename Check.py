import datetime
def Check():
 #check time and do appropriate command
 current = datetime.datetime.now()
 hr = current.hour
 min = current.minute
 if (hr == 8 and min == 00):
  tym = str(current.hour)+":"+str(current.minute)
  return GoodM(tym)
 elif (hr == 22 and min == 00):
  tym = str(current.hour)+":"+str(current.minute)
  return GoodN(tym)
 else:
  return 0;

def GoodM(time):
 return "Good Morning Sir! The current time is "+time

def GoodN(time):
 return "The current time now is "+time+".I am switching to hibernate"
 
