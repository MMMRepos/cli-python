from collections import defaultdict
from comms import CommunicationAdapter
from command import CommandFactory
from keyLogger import KeyLogger

def main():
    commLayer = CommunicationAdapter()
    keyHistory = KeyLogger()
    cliCommandFactory = CommandFactory()
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
        if menuSelection == "1":
            cliCommandFactory.displayCommands()
            commandSelection = input("Enter your choice of command ").strip()
            print(commandSelection)
            commandList = commandSelection.split("+")
            print(commandList)
            for command in commandList:
                command = command.strip(" ")
                print(command)
                commandValue = cliCommandFactory.getCommandValue(command)
                if commandValue is not None:
                    print("Command entered ", commandValue)
                    commandResponse = commLayer.executeCommand(commandValue)
                    print("Command response ", commandResponse)            
                else:
                    print("Invalid command")
        elif menuSelection == "2":
            print("Running tests")
        elif menuSelection == "3":
            print("Update device")
        elif menuSelection == "4":
            print("Close")
            
        
        
        keyHistory.appendLastKey(menuDict[str(menuSelection)])
        keyHistory.printKeyStack()
    
if __name__ == "__main__":
    main()