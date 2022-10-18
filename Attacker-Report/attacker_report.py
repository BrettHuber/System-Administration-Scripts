#!/usr/bin/env python3
#Executable permissions set
#Name: Brett Huber
#Date: 17 October 2022

# Variable
import os
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal
class Fail:
    def __init__(self, ipNumber, ipCountry):
        self.failCount = 1
        self.ipNumber = ipNumber
        self.ipCountry = ipCountry


def countAttacks(logName):
    lineNum = 0
    
    fails = []
    lineContent = []
    with open(logName, 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()
            if "Failed" in line:
                lineContent = line.split()
                if len(fails) == 0:
                    # failedAttempt = Fail(lineContent[10],"US")
                    # failedAttempt.failCount += 1
                    print(lineContent[10])
                    fails.append(Fail(lineContent[10],"US"))
                elif len(fails) == 1:
                    if lineContent[10] == getattr(fails[0], 'ipNumber'):
                        newCount = getattr(fails[0], 'failCount')
                        newCount += 1
                        setattr(fails[0], 'failCount', newCount)
                    else: 
                        # failedAttempt = Fail(lineContent[10],"US")
                        # failedAttempt.failCount += 1
                        print(lineContent[10])
                        break
                        fails.append(Fail(lineContent[10],"US"))
                else:
                    checkCount = 0
                    for x in range(len(fails)):
                        if lineContent[10] == getattr(fails[x], 'ipNumber'):
                            checkCount = x
                    if checkCount == 0:
                        # failedAttempt = Fail(lineContent[10],"US")
                        # failedAttempt.failCount += 1
                        fails.append(Fail(lineContent[10],"US"))
                    else:
                        newCount = getattr(fails[x], 'failCount')
                        newCount += 1
                        setattr(fails[x], 'failCount', newCount)   



    for obj in fails:
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