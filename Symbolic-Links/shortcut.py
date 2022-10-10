# !/usr/bin/env python3
# Name: Brett Huber
# Dat: 10 October 2022

# Variables
import os
import subprocess

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
    print('Ping Test Menu:')
    for i in symboMenu.keys():
        print(i, '|', symboMenu[i])

def main():
    boolVar = True # Sets a boolean variable to be used to run the while loop indefinitely
    while boolVar: # While loop to continuously run ping menu for user interactions
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[95m******************************\n******** Symbolink Menu *********\n******************************\033[0m\n')
        printSymboMenu() # Calls printPingMenu funtion to display ping menu
        selection = ''
        # Try Catch to take input, which is wrapped as an int variable. Catches invalid input and prints an error
        try:
            selection = str(input('\nEnter a selection: ')).upper() # Take user input and sents it to int 
        except:
            print('\033[91mError. Invalid input. Please try again and enter an integer.\033[0m')
        # Conditional statements to run the method corresponding to the user input
        if selection == '1':
            input("Press enter to continue: ")
        elif selection == '2':
            input("Press enter to continue: ")
        elif selection == '3': 
            input("Press enter to continue: ")
        elif selection == 'QUIT':
            print("\033[94mProgram will now exit.\033[0m")
            quit() # Exits the program and while loop
        else:
            print('\033[91mError. Invalid input. Please try again and enter an integer between 1 and 3 or the word quit.\033[0m')
            input("Press enter to continue: ")


if __name__ == "__main__":
    main()