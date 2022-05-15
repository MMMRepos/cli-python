from collections import defaultdict

from comms import CommunicationAdapter

LINE_FEED = "\n"
CARRIAGE_RETURN = "\r"

HELLO = "Hello"
GOODBYE = "Good Bye"
HOLD = "Hold Please"

HELLO_MESSAGE = "Hello, it is nice to meet you."
GOODBYE_MESSAGE = "I need to run; but it has been great talking."
HOLD_MESSAGE = "Excuse me a moment, someone else is here."

class Command:
    def __init__(self):
        self.commands = defaultdict(str)
        self.registerCommands()
        
    def registerCommand(self, commandKey, commandValue):
        self.commands[commandKey] = commandValue
    
    def getCommandValue(self, commandKey):
        value = self.commands[commandKey] 
        if value == "":
            return None
        else:
            return value + LINE_FEED
        
    def displayCommands(self):
        print("\n*** List of Commands ***\n")
        for key, value in self.commands.items():
            print("    " + key + ": " + value)
        print("\n")
        # print(dict(self.commands))
        
    def splitInputCommands(self, commandInput):
        retList = []
        commandList = commandInput.split("+")
        # print(commandList)
        for command in commandList:
            command = command.strip(" ")
            # print(command)
            commandValue = self.getCommandValue(command)
            if commandValue is not None:
                print("Command entered ", command)
                print("Message sent ", commandValue)
                retList.append(command)
                # commandResponse = commLayer.executeCommand(commandValue)
                # print("Command response ", commandResponse)            
            else:
                print(command  + " is invalid")
        return retList
    
    def sendCommand(self, commLayer: CommunicationAdapter):
        self.displayCommands()
        commandInput = input("Enter your choice of command ")
        commandList = self.splitInputCommands(commandInput)
                # print(commandInput)
                # commandList = commandInput.split("+")
        print(commandList)
        for command in commandList:
                    # command = command.strip(" ")
                    # print(command)
            commandValue = self.getCommandValue(command)
                    # if commandValue is not None:
            print("Command entered ", command)
            print("Message sent ", commandValue)
            commandResponse = commLayer.executeCommand(commandValue)
            print("Command response ", commandResponse)          
            # else:
            #     print("Invalid command")

    def registerCommands(self):
        self.registerCommand(HELLO, HELLO_MESSAGE)
        self.registerCommand(GOODBYE, GOODBYE_MESSAGE)
        self.registerCommand(HOLD, HOLD_MESSAGE)