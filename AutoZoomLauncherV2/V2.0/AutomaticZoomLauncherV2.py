import webbrowser
from datetime import datetime
import time 

file = open('ZoomLinks.csv', 'r')
# Read and print the entire file line by line
lst = []
while True:
    mydata = file.readline()
    if mydata == "":
        break
    mydata = mydata[:-1] if mydata[-1] == '\n' else mydata
    lst.append(mydata)
if lst[0] == '1':
    file.close()
    file = open('ZoomLinks.csv', 'w')
    periodA = (input("Paste the zoom link for Period A here: ") + '\n')
    periodB = (input("Paste the zoom link for Period B here: ") + '\n')
    periodC = (input("Paste the zoom link for Period C here: ") + '\n')
    periodD = (input("Paste the zoom link for Period D here: ") + '\n')
    periodE = (input("Paste the zoom link for Period E here: ") + '\n')
    periodF = (input("Paste the zoom link for Period F here: ") + '\n')
    periodG = (input("Paste the zoom link for Period G here: ") + '\n')
    file.write(periodA)
    file.write(periodB)
    file.write(periodC)
    file.write(periodD)
    file.write(periodE)
    file.write(periodF)
    file.write(periodG)
    file.close()
else:
    periodA = lst[0]
    periodB = lst[1]
    periodC = lst[2]
    periodD = lst[3]
    periodE = lst[4]
    periodF = lst[5]
    periodG = lst[6]
    file.close()
        
firstPeriod = (input("Enter first period of the day: ")).upper()

if firstPeriod == 'A':
    while True:
        t = datetime.now()
        seconds = str(t.second)
        minutes = str(t.minute)
        hours = str(t.hour)
        timeNow = str(hours + ":" + minutes + ":" + seconds)
        time.sleep(1)
    
        if timeNow == '7:55:0':
            webbrowser.open(periodA)
        if timeNow == '9:0:0':
            webbrowser.open(periodB)
        if timeNow == '10:10:0':
            webbrowser.open(periodC)
        if timeNow == '11:35:0':
            webbrowser.open(periodD)
        if timeNow == '12:35:0':
            webbrowser.open(periodE)
        if timeNow == '13:35:0':
            webbrowser.open(periodF)
            break
if firstPeriod == 'G':
    while True:
        t = datetime.now()
        seconds = str(t.second)
        minutes = str(t.minute)
        hours = str(t.hour)
        timeNow = str(hours + ":" + minutes + ":" + seconds)
        time.sleep(1)
    
        if timeNow == '7:55:0':
            webbrowser.open(periodG)
        if timeNow == '9:0:0':
            webbrowser.open(periodA)
        if timeNow == '10:10:0':
            webbrowser.open(periodB)
        if timeNow == '11:10:0':
            webbrowser.open(periodC)
        if timeNow == '12:35:0':
            webbrowser.open(periodD)
            break
if firstPeriod == 'E':
    while True:
        t = datetime.now()
        seconds = str(t.second)
        minutes = str(t.minute)
        hours = str(t.hour)
        timeNow = str(hours + ":" + minutes + ":" + seconds)
        time.sleep(1)
    
        if timeNow == '7:55:0':
            webbrowser.open(periodE)
        if timeNow == '9:0:0':
            webbrowser.open(periodF)
        if timeNow == '10:10:0':
            webbrowser.open(periodG)
        if timeNow == '11:10:0':
            webbrowser.open(periodA)
        if timeNow == '12:35:0':
            webbrowser.open(periodB)
            break
if firstPeriod == 'C':
    while True:
        t = datetime.now()
        seconds = str(t.second)
        minutes = str(t.minute)
        hours = str(t.hour)
        timeNow = str(hours + ":" + minutes + ":" + seconds)
        time.sleep(1)
    
        if timeNow == '7:55:0':
            webbrowser.open(periodC)
        if timeNow == '9:0:0':
            webbrowser.open(periodD)
        if timeNow == '10:10:0':
            webbrowser.open(periodE)
        if timeNow == '11:10:0':
            webbrowser.open(periodF)
        if timeNow == '12:35:0':
            webbrowser.open(periodG)
            break

       
        
            
