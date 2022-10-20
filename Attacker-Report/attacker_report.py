#!/usr/bin/env python3
#Executable permissions set
#Name: Brett Huber
#Date: 20 October 2022

# Imports
import os 
import re 
from datetime import date 
from geoip import geolite2

ipFormat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') # Uses regex to create the pattern of an IP address

os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal
class Fail: # Creates Fail class
    def __init__(self, ipNumber, ipCountry): # Initializes the values of the Fail instance using parameters
        self.failCount = 1 # Sets the initial value of fail count to 1
        self.ipNumber = ipNumber # Sets the initial ip number to the ipNumber parameter
        self.ipCountry = ipCountry # Sets the initial ip country to the ipCountry parameter

def countAttacks(logName): # Takes the name of the log file as parameter   
    failRecords = [] # Creates an empty list to stored the record of failed login attempts
    with open(logName, 'r') as file: # Opens the log in read mode
        line = file.readline() # Sets the variable line equal to the first line of the file
        while line: # Executes the while loop when line exists
            line = file.readline() # Sets the variable line equal to the next line of the file
            if "Failed password" in line: # Executes the following code if "Failed password" is in line
                lineIP = ipFormat.search(line)[0] # Gets the IP address on that line
                country = "" # Initialized country variable for later use
                geo = geolite2.lookup(lineIP) # Gets the complete geolocation of an IP address
                if geo is not None: # Executes if the geolocation is not null
                    country = geo.country # Set the country variable equal to the country aspect of the geolocation
                if len(failRecords) == 0: # Executes if the length of failRecords is 0 (list is empty)
                    failRecords.append(Fail(lineIP,country)) # Appends a new Fail object to the failRecords using the country and lineIP variable
                elif len(failRecords) == 1: # Executes if the length of failRecords is 1 (1 object in list)
                    if lineIP == getattr(failRecords[0], 'ipNumber'): # Executes if the comparison of lineIP and the ipNumber attribute of the first object in the list 
                        newCount = getattr(failRecords[0], 'failCount') # Retrieves the failCount attribute
                        newCount += 1 # Increments the failCount attribute
                        setattr(failRecords[0], 'failCount', newCount) # Sets the failCount attribute equal to the incremented newCount attribute
                    else: # Executes if line IP does not equal the retrieved IP number attribute 
                        failRecords.append(Fail(lineIP,country)) # Appends a new Fail object to the failRecords using the country and lineIP variable
                else: # Executes if the length of fail records in not 0 or 1
                    checkCount = -1 # Initialized checkCount to -1
                    for x in range(len(failRecords)): # Iterates through the failRecords list
                        if lineIP == getattr(failRecords[x], 'ipNumber'): # Executes if lineIP equals the ipNumber of an existing object in the list
                            checkCount = x # Sets checkCount equal to x, the spot in the list where there is a match
                            break # Breaks the foor loop
                    if checkCount == -1: # If checkCount is still -1
                        failRecords.append(Fail(lineIP,country)) # Appends a new Fail object to the failRecords using the country and lineIP variable
                    else: # Executes if checkCount is not -1
                        newCount = getattr(failRecords[x], 'failCount') # Gets failCount attribute
                        newCount += 1 # Increments failCount attribute
                        setattr(failRecords[x], 'failCount', newCount) # Sets the failCount attribute equal to the incremented newCount attribute

    failRecords.sort(key = lambda x: x.failCount) # Sorts the list of objects using the failCount attribute
    header = "\u001b[4mCOUNT\u001b[0m" 
    header2 ="\u001b[4mIP ADDRESS\u001b[0m"
    header3 ="\u001b[4mCOUNTRY\u001b[0m"
    print("\n\033[91m" + header.ljust(24) + "\033[0m\033[91m" + header2.ljust(30) + "\033[0m\033[91m" + header3.ljust(20) + "\033[0m")
    for obj in failRecords: # Iterated through objects in failRecords
        if getattr(obj, 'failCount') >= 10: # Executes if failCount is greatet than 10
           print(str(getattr(obj, 'failCount')).ljust(16) + str(getattr(obj, 'ipNumber')).ljust(22) + str(getattr(obj, 'ipCountry'))) # Prints out the object in the list, including fail count, ip number, and ip country    
    print("\n")

def main():
    today = date.today() # Sets today variable to the current date
    dateVal = str(today.strftime("%B %d, %Y")) # Formats the display of the date
    print("\n\033[92mSystem Report\033[0m -", dateVal)
    fileName = "syslog" # Creates a sys report variable
    fileExtension = "log" # Creates a variable for the file extension
    logFile = f'{fileName}.{fileExtension}' # Constructs the file name
    filePath = "/home/student/Downloads/System-Administration-Scripts/Attacker-Report/" + logFile # Constructs the filePath
    countAttacks(filePath) # Calls the countAttacks with the filePath as a paramter

if __name__ == "__main__":
    main()