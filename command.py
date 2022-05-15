from collections import defaultdict

LINE_FEED = "\n"
CARRIAGE_RETURN = "\r"

class CommandFactory:
    def __init__(self):
        self.commands = defaultdict(str)
        
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