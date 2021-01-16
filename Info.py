#information 
import sqlite3

connection = sqlite3.connect("Info.db")
def Add(name,gend,dob):
 cursor = connection.cursor()
 num = 0
 sql_command = """ INSERT INTO information (usernum, Name, Gender, Dob) VALUES ('{0}','{1}','{2}','{3}');""".format(num,name, gend, dob)
 cursor.execute(sql_command)
 connection.commit()
 connection.close()
def Create():
 cursor = connection.cursor()
 sql_command = """CREATE TABLE information (usernum INT NOT NULL AUTO_INCREMENT, Name VARCHAR(20), Gender CHAR(1), Dob DATE);"""
 cursor.execute(sql_command)
 connection.commit()
 connection.close()
def Find(Name):
 cursor = connection.cursor()
 sql_command =""" SELECT Name, Gender,Dob FROM information WHERE Name = '{0}';""".format(Name)
 info = cursor.execute(sql_command)
 connection.commit()
 connection.close()
 if info == '0' or info == 0:
  return (Name+" could not be found")
 else:
  return ("Name:{0}\nGender:{1}\nDate of Birth{2}\n".format(info[0],info[1],info[2]))

