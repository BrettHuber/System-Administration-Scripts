# !/usr/bin/env python3
# Name: Brett Huber
# Dat: 10 October 2022

# Variables
from macpath import islink
import os

# If the OS is Windows cls will clear the terminal
# If the OS is Unix clear will clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

symboMenu = {
    '1   ': 'Make a symbolic link',
    '2   ': 'Delete a symbolic link',
    '3   ': 'Display symbolic link report',
    'Quit': 'Exit Program'
}

# Used a for loop to print out the end user menu
def printSymboMenu():
    for i in symboMenu.keys():
        print(i, '|', symboMenu[i])

def makeSymbolink(fileName):
    currentDirectory = os.path.expanduser("~")
    path = []
    for root, directories, files in os.walk(currentDirectory):
        if fileName in files:
            path.append(os.path.join(root, fileName))
    if(len(path) == 0):
        print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m")
    else:
        filePath = path[0]
        print(filePath)
        if(str(os.path.basename(filePath)) == fileName):
            source = filePath
            destination = str(os.path.expanduser("~")) + "/" + fileName
            os.symlink(source, destination)
            print("\033[92mAdded link ...\033[0m\n")
        else:
            print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m")

  

def printSymbolicLinks():
    numSymbolicLinks = 0

def main():
    boolVar = True # Sets a boolean variable to be used to run the while loop indefinitely
    while boolVar: # While loop to continuously run ping menu for user interactions
        os.system('cls' if os.name == 'nt' else 'clear')

        currentDir = os.getcwd()
        print("Working Directory: " + currentDir + "\n")

        print('\033[95m******************************\n******** Symbolink Menu *********\n******************************\033[0m\n')
        printSymboMenu() # Calls printPingMenu funtion to display ping menu
        selection = ''
        # Try Catch to take input, which is wrapped as an string variable. Catches invalid input and prints an error
        try:
            selection = str(input('\nEnter a selection: ')).upper() # Take user input and sents it to int 
        except:
            print('\033[91mError. Invalid input. Please try again and enter an integer (1-3) or quit.\033[0m')
        # Conditional statements to run the method corresponding to the user input
        if selection == '1':
            fileName = str(input("Please enter a file name: "))
            makeSymbolink(fileName)
            input("Press enter to return to main menu: ")
        elif selection == '2':
            input("Press enter to return to main menu: ")
        elif selection == '3': 
            printSymbolicLinks()
            input("Press enter to return to main menu: ")
        elif selection == 'QUIT' or 'Q':
            print("\033[94mProgram will now exit.\033[0m")
            quit() # Exits the program and while loop
        else:
            print('\033[91mError. Invalid input. Please try again and enter an integer between 1 and 3 or the word quit.\033[0m')
            input("Press enter to continue: ")


if __name__ == "__main__":
    main()