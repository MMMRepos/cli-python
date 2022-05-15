from collections import defaultdict
from enum import Enum

from comms import CommunicationAdapter

LINE_FEED = "\n"
CARRIAGE_RETURN = "\r"

class Command(Enum):
    HELLO = ("Hello", "Hello, it is nice to meet you.")
    GOODBYE = ("Good Bye", "I need to run; but it has been great talking.")
    HOLD = ("Hold Please", "Excuse me a moment, someone else is here.")
    TERMINATOR = ("\n\r", "")
    def __init__(self, commandKey, message):
        self.commandKey = commandKey       
        self.message = message  

class CommandOperation:
    """This class is used for handling CLI command operations.
    
    This class uses the comms module for sending the CLI commands to the connected device.
    """
    
    def __init__(self, commLayer: CommunicationAdapter):
        self.commands = defaultdict(str)
        self.registerCommands()
        self.commLayer = commLayer
    
    def sendCommand(self):
        """Send the command selected from a list of commands to the communication layer
        
        Parameters:
        None

        Returns:
        None
        """
        
        self.displayCommands()
        commandKey = input("Enter your choice of command ")
        commandValue = self.getCommandValue(commandKey)
        if commandValue is None:
            print("Invalid Command")
        else:
            print("Command entered ", commandKey)
            print("Message sent ", commandValue)
            commandResponse = self.commLayer.exchangeData(commandValue)
            print("Command response ", commandResponse)   

    def registerCommand(self, commandKey, commandValue):
        self.commands[commandKey] = commandValue
    
    def getCommandValue(self, commandKey):
        value = self.commands[commandKey] 
        if value == "":
            return None
        else:
            return value + LINE_FEED + CARRIAGE_RETURN
        
    def displayCommands(self):
        print("\n*** List of Commands ***\n")
        for key, value in self.commands.items():
            print("    " + key + ": " + value)
        print("\n")
        # print(dict(self.commands))

    def registerCommands(self):
        self.registerCommand(Command.HELLO.commandKey, Command.HELLO.message)
        self.registerCommand(Command.GOODBYE.commandKey, Command.GOODBYE.message)
        self.registerCommand(Command.HOLD.commandKey, Command.HOLD.message)