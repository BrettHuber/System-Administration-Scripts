# !/usr/bin/env python3
# Executable permissions set
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
    currentDirectory = os.path.expanduser("~") # Sets the current directory equal to the home directory since that is the intended location for the links
    path = [] # Creates an empty list for paths that match a specified file name
    for root, directories, files in os.walk(currentDirectory): # Traverses top-down through the current directory and all subdirectories
        if fileName in files: # Checks to see if the specified file name is in the files list
            path.append(os.path.join(root, fileName)) # Adds the file path of a match to the path list
    if(len(path) == 0): # Exectutes the following code if no file paths are in the path list
        print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m\n")
    else: # Exectutes the following code if there are file paths in the path list
        filePath = path[0] # Takes the first index of the path list and set it to a filepath variable
        if(str(os.path.basename(filePath)) == fileName): # Executes the following code if the base name matches the filename parameter
            source = filePath # Sets the source variable equal to the filepath
            destination = str(os.path.expanduser("~")) + "/" + fileName # Sets the destination variable equal the home directory / the filename parameter
            os.symlink(source, destination) # Creates a symbolic link using the source and destination variables
            print("\033[92mAdded link ...\033[0m\n") 
        else: # Executes the following code if the base name does not match the filename parameter
            print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m\n")

def removeSymbolink(fileName):
    currentDirectory = os.path.expanduser("~") # Sets the current directory equal to the home directory since that is the intended location for the links
    path = []  # Creates an empty list for paths that match a specified file name
    for root, directories, files in os.walk(currentDirectory): # Traverses top-down through the current directory and all subdirectories
        if fileName in files: # Checks to see if the specified file name is in the files list
            path.append(os.path.join(root, fileName)) # Adds the file path of a match to the path list
    if(len(path) == 0): # Exectutes the following code if no file paths are in the path list
        print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m\n")
    else: # Exectutes the following code if there are file paths in the path list
        filePath = path[0] # Takes the first index of the path list and set it to a filepath variable
        if(str(os.path.basename(filePath)) == fileName): # Executes the following code if the base name matches the filename parameter
            destination = str(os.path.expanduser("~")) + "/" + fileName # Sets the destination variable equal the home directory / the filename parameter
            if os.path.islink(destination): # Check to see if the path destination is a link and executes the following code if true
                os.unlink(destination) # Removes the symbolink
                print("\033[92mRemoved link ...\033[0m\n")
        else: # Executes the following code if the base name does not match the filename parameter
            print("Sorry, couldn't find \033[91m" + fileName + "!\033[0m\n")

def printSymbolicLinks():
    numSymbolicLinks = 0 # Creates an int variable to track the number of symbolinks
    currentDirectory = os.path.expanduser("~") # Sets the current directory equal to the home directory since that is the intended location for the links
    links = [] # Creates an empty list for links
    for link in os.listdir(currentDirectory): # Iterated through a list of directories in the current directory
        if link not in (os.curdir, os.pardir): # Executes the following code if the link is not in either the current or parent directories
            linkPath = os.path.join(currentDirectory, link) # Constructs the link path
            if os.path.islink(linkPath): # Executes the following code if the path is a link path
                links.append(str(link).ljust(42) + str(os.readlink(linkPath))) # Appends the lnik and linkpath to the links list
                numSymbolicLinks += 1 # Increments the number symbolic links
                print(str(link) + "--->" + str(os.readlink(linkPath)))

    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal
    print('\033[95m******************************\n****** Shortcut Report *******\n******************************\033[0m\n')
    print("Directory: \u001b[36m" + str(currentDirectory) + "\u001b[0m\n") # Prints out the directory of the symbolinks (home dir)
    print("Number of symbolic links: \u001b[36m" + str(numSymbolicLinks) + "\u001b[0m\n") # Prints out the number of symbolinks
    header = "\u001b[4mSymbolic Link\u001b[0m"
    header2 ="\u001b[4mTarget Path\u001b[0m"
    print(header.ljust(50) + header2 + "\n") # Prints out headers for links and their paths
    for l in links: # Iterates through list of links
        linkName = "\u001b[36m" + l + "\u001b[0m" # Sets linkName variable equal to link in the list
        print(str(linkName) + "\n") # Prints out links and destination paths

def main():
    boolVar = True # Sets a boolean variable to be used to run the while loop indefinitely
    while boolVar: # While loop to continuously run symbolink menu for user interactions
        os.system('cls' if os.name == 'nt' else 'clear')  # Clears the terminal
        currentDir = os.getcwd() # Set the currentDir variable to the current working directory
        print("Working Directory: " + currentDir + "\n")
        print('\033[95m******************************\n******** Symbolink Menu *********\n******************************\033[0m\n')
        printSymboMenu() # Calls printSymboMenu funtion to display symbolink menu
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
            fileName = str(input("Please enter a file name: "))
            removeSymbolink(fileName)
            input("Press enter to return to main menu: ")
        elif selection == '3': 
            printSymbolicLinks()
            input("Press enter to return to main menu: ")
        elif selection == 'QUIT' or 'Q':
            print("\033[94mProgram will now exit.\033[0m\n")
            quit() # Exits the program and while loop
        else:
            print('\033[91mError. Invalid input. Please try again and enter an integer between 1 and 3 or the word quit.\033[0m')
            input("Press enter to continue: ")

if __name__ == "__main__":
    main()