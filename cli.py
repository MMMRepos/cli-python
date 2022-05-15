from collections import defaultdict
from comms import CommunicationAdapter
from command import Command
from keyLogger import KeyLogger
from dfu import DeviceFirmwareUpdate
import sys
from enum import Enum



menuDict = defaultdict(str)

def main():
    keyHistory = KeyLogger()
    cliCommands = Command()
    commLayer = initializeCommLayer()
    bootload = DeviceFirmwareUpdate(commLayer)

    displayMainMenu()
    
    while True:
        menuSelection = input("Enter your selection number ")
        print("Selected option", menuSelection)
        keyHistory.appendLastKey(menuDict[str(menuSelection)])
        
        if menuSelection == CLIMenu.SEND_COMMAND.number:
            cliCommands.sendCommands(commLayer)  
        elif menuSelection == CLIMenu.RUN_TEST.number:
            runTests()
        elif menuSelection == CLIMenu.UPDATE_DEVICE.number:
            bootload.updateDevice()
        elif menuSelection == CLIMenu.CLOSE.number:
            close(keyHistory)

def close(keyHistory):
    print("Key Logger History")
    keyHistory.printKeyQueue()
    userInput = input("Press ENTER to close the CLI")
    print(userInput)
    print("Thank you for using the CLI")
    if userInput == "":
        sys.exit()

def runTests():
    print("Running tests")
    print("Test 1: Quick Chat")
    buffer1 = ["Hello", "Good Bye"]
    print("Test 2: Extended Call")
    print("Test 1: On Hold")

def displayMainMenu():
    print("CLI Task")
    print("\n*** Main Menu ***\n")
    menuDict[CLIMenu.SEND_COMMAND.number] = CLIMenu.SEND_COMMAND.text
    menuDict[CLIMenu.RUN_TEST.number] = CLIMenu.RUN_TEST.text
    menuDict[CLIMenu.UPDATE_DEVICE.number] = CLIMenu.UPDATE_DEVICE.text
    menuDict[CLIMenu.CLOSE.number] = CLIMenu.CLOSE.text
    for key, value in menuDict.items():
        print("    " + key + ". " + str(value))
    print("\n")
    
def initializeCommLayer():
    commLayer = CommunicationAdapter()
    commLayer.displayCommPorts()
    portNumber = input("Select the port from the available COM ports ")
    baudRate = int(input("Enter the baud rate "))
    timeOut = int(input("Enter the timeout ")) 
    commLayer.openComPort(portNumber, baudRate, timeOut)
    return commLayer

class CLIMenu(Enum):
    SEND_COMMAND = ("1", "Send Command")
    RUN_TEST = ("2", "Run Test")
    UPDATE_DEVICE = ("3", "Update Device")
    CLOSE = ("4", "Close")
    def __init__(self, number, text):
        self.number = number       
        self.text = text   
    
        
        
    
if __name__ == "__main__":
    main()