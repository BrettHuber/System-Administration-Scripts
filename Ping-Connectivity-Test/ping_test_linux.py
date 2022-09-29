# !/usr/bin/env python3
# Name: Brett Huber
# Date: 12 September 2022

# Variables
import os
import subprocess
import platform

# If the OS is Windows cls will clear the terminal
# If the OS is Unix clear will clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# RIT DNS
remoteIP = "129.21.3.17"

# Google URL
googleURL = "google.com"

determineOS = '-n' if platform.system().lower == 'windows' else '-c'

# Options for user menu and corresponding values
pingMenu = {
    1: 'Test Default Gateway Connectivity',
    2: 'Test Remote IP (RIT DNS) Connectivity',
    3: 'Test DNS Resolution',
    4: 'Display Default Gateway',
    5: 'Exit Program'
}

def pingTest(ipAddress):
    subprocessCommand = ['ping', determineOS, '4', ipAddress]
    ping = subprocess.run(subprocessCommand)
    if(ping.returncode == 0): # ping.returnCode returns 0 if successful, 1 if failure
        print("\n\033[92mTest successful!\033[0m\n")
    else:
        print("\n\033[91mTest failed!\033[0m\n")

# Using the ip route the default gateway is derived from the system
def getDefaultGateway():
    dg = subprocess.run(['ip route | grep default'], stdout = subprocess.PIPE, shell = True)
    stdout = dg.stdout.split()
    default = stdout[2].decode("utf-8")
    return default

# Calls the getDefaultGateway() function and sets the returned value to a variable before printing it out
def printDefaultGateway():
    defaultGate = getDefaultGateway()
    print("Default Gateway: " + defaultGate)

# Used a for loop to print out the end user menu
def printPingMenu():
    print('Ping Test Menu:')
    for i in pingMenu.keys():
        print(i, '|', pingMenu[i])
        
def main():
    boolVar = True # Sets a boolean variable to be used to run the while loop indefinitely
    while boolVar: # While loop to continuously run ping menu for user interactions
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[95m******************************\n******** Ping Tester *********\n******************************\033[0m\n')
        printPingMenu() # Calls printPingMenu funtion to display ping menu
        selection = ''
        # Try Catch to take input, which is wrapped as an int variable. Catches invalid input and prints an error
        try:
            selection = (int)(input('\nEnter a selection: ')) # Take user input and sents it to int 
        except:
            print('\033[91mError. Invalid input. Please try again and enter an integer.\033[0m')
        # Conditional statements to run the method corresponding to the user input
        if selection == 1:
            defaultGateway = getDefaultGateway() # Set the variable equal to the default gateway
            pingTest(defaultGateway) # Runs pingTest with the default gatway as parameter
            input("Press enter to continue: ")
        elif selection == 2:
            pingTest(remoteIP) # Runs pingTest with the RIT DNS as parameter
            input("Press enter to continue: ")
        elif selection == 3: 
            pingTest(googleURL) # Runs pingTest with the google.com as parameter
            input("Press enter to continue: ")
        elif selection == 4:
            printDefaultGateway() # Print out the default gateway to user
            input("Press enter to continue: ")
        elif selection == 5:
            print("\033[94mProgram will now exit.\033[0m")
            exit() # Exits the program and while loop
        else:
            print('\033[91mError. Invalid input. Please try again and enter an integer between 1 and 5.\033[0m')

if __name__ == "__main__":
    main()