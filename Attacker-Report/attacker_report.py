#!/usr/bin/env python3
#Executable permissions set
#Name: Brett Huber
#Date: 17 October 2022

# Variable
from operator import ge
import os
import re
from datetime import date
from geoip import geolite2

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
            if "Failed password" in line:
                lineIP = ipFormat.search(line)[0]
                country = ""
                geo = geolite2.lookup(lineIP)
                if geo is not None: 
                    country = geo.country
                if len(fails) == 0:
                    fails.append(Fail(lineIP,country))
                elif len(fails) == 1:
                    if lineIP == getattr(fails[0], 'ipNumber'):
                        newCount = getattr(fails[0], 'failCount')
                        newCount += 1
                        setattr(fails[0], 'failCount', newCount)
                    else: 
                        fails.append(Fail(lineIP,country))
                else:
                    checkCount = 0
                    for x in range(len(fails)):
                        if lineIP == getattr(fails[x], 'ipNumber'):
                            checkCount = x
                            break
                    if checkCount == 0:
                        fails.append(Fail(lineIP,country))
                    else:
                        newCount = getattr(fails[x], 'failCount')
                        newCount += 1
                        setattr(fails[x], 'failCount', newCount)   

    # print("\nSize: " +str(len(fails)))
    fails.sort(key = lambda x: x.failCount)
    header = "\u001b[4mCOUNT\u001b[0m"
    header2 ="\u001b[4mIP ADDRESS\u001b[0m"
    header3 ="\u001b[4mCOUNTRY\u001b[0m"
    print("\n\033[91m" + header.ljust(24) + "\033[0m\033[91m" + header2.ljust(30) + "\033[0m\033[91m" + header3.ljust(20) + "\033[0m")
    for obj in fails:
        if getattr(obj, 'failCount') >= 10:
           print(str(getattr(obj, 'failCount')).ljust(16) + str(getattr(obj, 'ipNumber')).ljust(22) + str(getattr(obj, 'ipCountry')))        
    print("\n")

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
    fileName = "syslog" # Creates a sys report variable
    fileExtension = "log" # Creates a variable for the file extension
    logFile = f'{fileName}.{fileExtension}' # Constructs the file name
    filePath = "/home/student/Downloads/System-Administration-Scripts/Attacker-Report/" + logFile
    countAttacks(filePath)

if __name__ == "__main__":
    main()