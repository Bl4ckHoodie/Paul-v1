# -*- coding: utf-8 -*-
"""
The idea behind this is to find ways of storing my ideas for easy and fast access 
and to also provide easy manipulation
"""
def getList():
    try:
        f = open("Admin/ideas/List.txt","r")
    except:
        print("unable able to open list file")
    return f

def getByNum(num):
    f = getList()
    idea = "#"+str(num)
    for ln in f:
        i = str(ln[0])+str(ln[1])+str(ln[2])
        if i == idea :
            return ln
    return "not found"
        
def getByName(name):
    f = getList()
    for ln in f:
        i = ln.count("- ")
        nm = ln[i:len(ln)]
        nm.lower()
        name.lower()
        if nm == name:
            return ln
    return "not found"
            
