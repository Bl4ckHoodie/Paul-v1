def setReminder():
 date = AskDate()
 time = AskTime()
 descript = AskDescript()
 return addReminder(time,date,descript)

def AskDate():
  return input('Enter date #dd-mm-yyyy: ')
 
def AskTime():
  return input('Enter time #hh:mm: ')

def AskDescript():
  return input('Enter Description: ')

def addReminder(ti,da,des):
  try:
   file = open("Remind/"+da+".txt","a")
   file.writelines(ti+"\n")
   file.writelines(des+"\n")
   file.close()
   return "Reminder has been successfully set."
  except :
   file = open("Remind/"+da+".txt","w")
   file.writelines(ti+"\n")
   file.writelines(des+"\n")
   file.close()
   return "New reminder has been successfully set."

def getReminder():
   da = input("Enter date #dd-mm-yyyy: ")
   try:
    askRemind(da)
    return "Done!"
   except:
    return "No reminder was set for "+da
def askRemind(da):
  try:
   file = open("Remind/"+da+".txt","r")
   print("Displaying Remind for "+da+"\n")
   print("==============================")
   for a in file:
    print(a)
   file.close()
   print("==============================")
  except ex:
    print("Error :"+ex)
	
