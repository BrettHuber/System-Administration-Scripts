# !/usr/bin/env python3
# Name: Brett Huber
# Date: 24 September 2022

# Imports
import os
import subprocess
import platform
import socket
import shutil

from datetime import date

# Creates a set of variable to memory or storage size conversion
KB = 1024
MB = 1024 * KB
GB = 1024 * MB

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')
output = "" # Creates the global output variable

def printDeviceInfo():
    global output # Allows the global output variable to be updated 
    host = socket.gethostname() # Gets the hostname and sets it equal to the host variable
    domain = socket.getfqdn() # Gets the domain and sets it equal to the domain variable
    
    # Prints out the device information and variables
    print("Hostname:", host)
    print("Domain:", domain)

    # Adds the content to the global output
    output += "Hostname: " + host + "\n"
    output += "Domain: " + domain + "\n"


def getDefaultGateway():
    dg = subprocess.run(['ip route | grep default'], stdout = subprocess.PIPE, shell = True)
    # print(subprocess.run(['ip', 'route'], stdout = subprocess.PIPE))
    stdout = dg.stdout.split()
    default = stdout[2].decode("utf-8")
    return default

def printNetworkInfo():
    global output # Allows the global output variable to be updated 
    host = socket.gethostname()
    # ipAddress = socket.gethostbyname(host)
    defaultGateway = getDefaultGateway()

    # Get IP address of ens192
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 0))
    ipAddress = sock.getsockname()[0]
    
    # Runs the subprocess command 'fconfig | grep -i mask' and sets the netmask variable equal to the third index of the terminal output in utf-8 form
    mask = subprocess.run(['ifconfig | grep -i mask'], stdout = subprocess.PIPE, shell = True)
    stdout = mask.stdout.split()
    netmask = stdout[3].decode("utf-8")
    
    # Opens the file and prints out the DNS values (1st index on each line) to each of the two variables
    countDNS = 0
    with open('/etc/resolv.conf') as file:
        for fileLine in file:
            if 'nameserver' in fileLine:
                if countDNS == 0:
                    dnsOne = fileLine.split()[1]
                    countDNS += 1
                elif countDNS == 1:
                    dnsTwo = fileLine.split()[1]
                    countDNS += 1    
            if countDNS == 2:
                break      

    # Prints out the network information and variables
    print("IP Address:", ipAddress)
    print("Gateway:", defaultGateway)
    print("Network Mask:", netmask)
    print("DNS1:", dnsOne)
    print("DNS2:", dnsTwo)

    # Adds the content to the global output
    output += "IP Address: " + ipAddress + "\n"
    output += "Gateway: " + defaultGateway + "\n"
    output += "IP Address: " + netmask + "\n"
    output += "DNS1: " + dnsOne + "\n"
    output += "DNS2: " + dnsTwo + "\n"


def printOsInfo():
    global output # Allows the global output variable to be updated 
    disInfo = platform.linux_distribution() # Gets the specific linux distribution and version
    os = disInfo[0] # Sets os variable to the first index of disInfo
    osVersion = disInfo[1] # Sets osVersion variable to the first index of disInfo

    # Runs the subprocess command 'uname -r' and sets the kernel variable equal to its terminal output without the newlines
    kerCommand = subprocess.run(['uname -r'], stdout = subprocess.PIPE, shell = True, universal_newlines = True)
    kernel = kerCommand.stdout.replace('\n', '')

    # Prints out os informations and variables
    print("Operating System:", os)
    print("Operating Version:", osVersion)
    print("Kernel Version:", kernel)

    # Adds the content to the global output
    output += "Operating System: " + os + "\n"
    output += "Operating Version: " + osVersion + "\n"
    output += "Kernel Version: " + kernel + "\n"


def printStorageInfo():
    global output # Allows the global output variable to be updated 
    total = ((shutil.disk_usage("/").total)/GB) # Get total space in the hard drive and converts it to Gb
    free = ((shutil.disk_usage("/").free)/GB) # Get free space in the hard drive and converts it to Gb
    # Prints out hard drive information and variables
    print("Hard Drive Capacity: " + str(round(total,2)) + " Gb")
    print("Available Space: " + str(round(free,2)) + " Gb")

    # Adds the content to the global output
    output += "Hard Drive Capacity: " + str(round(total,2)) + "\n"
    output += "Available Space: " + str(round(free,2)) + "\n"

def printProcessorInfo():
    global output # Allows the global output variable to be updated 
    CPU = platform.processor()
    processorCount = os.cpu_count()
    coreCount = os.cpu_count()

    cpuCommand = subprocess.run(["lscpu | grep 'Model name' | cut -f 2 -d ':' | awk '{$1=$1}1'"], stdout = subprocess.PIPE, shell = True, universal_newlines = True)
    cpuModel = cpuCommand.stdout.replace('\n', '')

    # Print the cpu information variables
    print("CPU Model:", cpuModel)
    print("Number of processors:", processorCount)
    print("Number of cores:", coreCount)
    
    # Adds the content to the global output
    output += "CPU Model: " + cpuModel + "\n"
    output += "Number of processors: " + str(processorCount) + "\n"
    output += "Number of cores: " + str(coreCount) + "\n"
    
def printMemoryInfo():
    global output # Allows the global output variable to be updated 
    count = 0
    # Open the file at the specified location and iterated the lines
    with open('/proc/meminfo') as file:
        for fileLine in file:
            # If the line contains MemTotal it executes the following code
            if 'MemTotal' in fileLine: 
                # Sets the totalRam variable to the value of the second string in the line, which is casted to int and rounded to two decimals
                totalRam = str(round((int(fileLine.split()[1])/1073741.824), 2)) + " Gi"
                count += 1 # Increments a count variable
            # If the line contains MemAvailable it executes the following code
            if 'MemAvailable' in fileLine:
                # Sets the availableRam variable to the value of the second string in the line, which is casted to int and rounded to two decimals
                availableRam = str(round((int(fileLine.split()[1])/1073741.824),2)) + " Gi"
                count += 1 # Increments a count variable
            if count == 2:
                break  # Breaks the for loop
    # Print the ram variables
    print("Total RAM:", totalRam)
    print("Available RAM:", availableRam)
    
    # Adds the content to the global output
    output += "Total RAM: " + totalRam + "\n"
    output += "Available RAM: " + availableRam + "\n"

    
def main():
    global output # Allows the global output variable to be updated 
    today = date.today() # Sets today variable to the current date
    dateVal = str(today.strftime("%B %d, %Y")) # Formats the display of the date

    print("\n\033[91mSystem Report -", dateVal)
    print("\033[0m")
    output += "System Report -" + dateVal + "\n"


    # Prints out the device information title and calls the function to print out corresponding information
    print("\n\033[92mDevice Information:\033[0m\n")
    output += "\nDevice Information:\n"
    printDeviceInfo()

    # Prints out the network information title and calls the function to print out corresponding information
    print("\nNetwork Information:\n")
    output += "\nNetwork Information:\n"
    printNetworkInfo()

    # Prints out the os information title and calls the function to print out corresponding information
    print("\n\033[92mOS Information:\033[0m\n")
    output += "\nOS Information:\n"
    printOsInfo()

    # Prints out the storage information title and calls the function to print out corresponding information
    print("\n\033[92mStorage Information:\033[0m\n")
    output += "\nStorage Information:\n"
    printStorageInfo()

    # Prints out the processor information title and calls the function to print out corresponding information
    print("\n\033[92mProcessor Information:\033[0m\n")
    output += "\nProcessor Information:\n"
    printProcessorInfo()

    # Prints out the memory information title and calls the function to print out corresponding information
    print("\n\033[92mMemory Information:\033[0m\n")
    output += "\nMemory Information:\n"
    printMemoryInfo()

    homeDirPath = os.path.expanduser('~') # Gets the path to the user home directory
    hostName = socket.gethostname() # Gets the host name
    sysReport = "_system_report" # Creates a sys report variable
    extension = "log" # Creates a variable for the file extension
    fileName = f'{hostName}{sysReport}.{extension}' # Constructs the file name
    filePath = homeDirPath + "/" + fileName # Constructs the file path
    file = open(filePath, "w") # Opens the file name using the file path with writing
    print("\nFile created in home directory!") # Prints out a message to terminal
    file.write(output) # Writes the contents of the global output to the the file
    file.close() # Closes the file

if __name__ == "__main__":
    main()