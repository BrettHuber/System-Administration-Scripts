#!/usr/bin/env python3
#Executable permissions set
#Name: Brett Huber
#Date: 17 October 2022

# Variable
import os
import re
from datetime import date

ipFormat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal
class Fail:
    def __init__(self, ipNumber, ipCountry):
        self.failCount = 1
        self.ipNumber = ipNumber
        self.ipCountry = ipCountry


def countAttacks(logName):    
    fails = []
    with open(logName, 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()
            if "Failed" in line:
                lineIP = ipFormat.search(line)[0]
                if len(fails) == 0:
                    fails.append(Fail(lineIP,"US"))
                elif len(fails) == 1:
                    if  lineIP == getattr(fails[0], 'ipNumber'):
                        newCount = getattr(fails[0], 'failCount')
                        newCount += 1
                        setattr(fails[0], 'failCount', newCount)
                    else: 
                        fails.append(Fail(lineIP,"US"))
                else:
                    checkCount = 0
                    for x in range(len(fails)):
                        if lineIP == getattr(fails[x], 'ipNumber'):
                            checkCount = x
                    if checkCount == 0:
                        fails.append(Fail(lineIP,"US"))
                    else:
                        newCount = getattr(fails[x], 'failCount')
                        newCount += 1
                        setattr(fails[x], 'failCount', newCount)   


    print("\nSize: " +str(len(fails)))
    for obj in fails:
        if getattr(obj, 'failCount') >= 10:
           print("IP: " + getattr(obj, 'ipNumber') + "    FailCount: " + str(getattr(obj, 'failCount')) + "\n")        


            # lineNum += 1
            # if lineNum == 3:
            #     lineContent = line.split()
            #     for x in lineContent:
            #         print(x + "\n")
            # line = file.readline()

def main():
    today = date.today() # Sets today variable to the current date
    dateVal = str(today.strftime("%B %d, %Y")) # Formats the display of the date
    print("\n\033[92mSystem Report\033[0m -", dateVal)
    print("\n\n")
    fileName = "syslog" # Creates a sys report variable
    fileExtension = "log" # Creates a variable for the file extension
    logFile = f'{fileName}.{fileExtension}' # Constructs the file name
    filePath = "/home/student/Downloads/System-Administration-Scripts/Attacker-Report/" + logFile
    countAttacks(filePath)

if __name__ == "__main__":
    main()