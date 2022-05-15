from collections import defaultdict
from comms import CommunicationAdapter
from command import CommandFactory
from keyLogger import KeyLogger
from dfu import DeviceFirmwareUpdate
import sys

def main():
    commLayer = CommunicationAdapter()
    keyHistory = KeyLogger()
    cliCommandFactory = CommandFactory()
    bootload = DeviceFirmwareUpdate()
    
    cliCommandFactory.registerCommand("Hello", "Hello, it is nice to meet you.")
    cliCommandFactory.registerCommand("Good Bye", "I need to run; but it has been great talking.")
    cliCommandFactory.registerCommand("Hold Please", "Excuse me a moment, someone else is here.")
    
    print("CLI Task")
    print("\n*** Main Menu ***\n")
    menuDict = defaultdict(str)
    menuDict["1"] = "Send Command"
    menuDict["2"] = "Run Test"
    menuDict["3"] = "Update Device"
    menuDict["4"] = "Close"
    
    for key, value in menuDict.items():
        print("    " + key + ". " + str(value))
    print("\n")
    
    commLayer.displayCommPorts()
    portNumber = input("Select the port from the available COM ports ")
    baudRate = int(input("Enter the baud rate "))
    timeOut = int(input("Enter the timeout ")) 
    commLayer.openComPort(portNumber, baudRate, timeOut)
    
    while True:
        menuSelection = input("Enter your selection number ")
        print("Selected option", menuSelection)
        keyHistory.appendLastKey(menuDict[str(menuSelection)])
        
        if menuSelection == "1":
            cliCommandFactory.displayCommands()
            commandInput = input("Enter your choice of command ")
            # commandList = cliCommandFactory.processInputCommands(commandInput)
            print(commandInput)
            commandList = commandInput.split("+")
            print(commandList)
            for command in commandList:
                command = command.strip(" ")
                print(command)
                commandValue = cliCommandFactory.getCommandValue(command)
                if commandValue is not None:
                    print("Command entered ", command)
                    print("Message sent ", commandValue)
                    commandResponse = commLayer.executeCommand(command)
                    print("Command response ", commandResponse)            
                else:
                    print("Invalid command")
        elif menuSelection == "2":
            print("Running tests")
        elif menuSelection == "3":
            print("Update device")
            
        elif menuSelection == "4":
            print("Key Logger History")
            keyHistory.printKeyQueue()
            userInput = input("Press ENTER to close the CLI")
            print(userInput)
            print("Thank you for using the CLI")
            if userInput == "":
                sys.exit()
        
        
    
if __name__ == "__main__":
    main()