#!/usr/bin/env python3
#Executable permissions set
#Name: Brett Huber
#Date: 17 October 2022

# Variable
import os
from datetime import date

os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal
class Fail:
    def __init__(self, failCount, ipName, ipCountry):
        self.failCount = failCount
        self.ipName = ipName
        self.failCount = ipCountry


def countAttacks():
    line = 0
    
    fails = []
    with open(r'syslog.log', 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()

def main():
    today = date.today() # Sets today variable to the current date
    dateVal = str(today.strftime("%B %d, %Y")) # Formats the display of the date
    print("\n\033[92mSystem Report\033[0m -", dateVal)
    print("\n\n")

if __name__ == "__main__":
    main()