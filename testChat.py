from enum import Enum
from commandOperation import Command, CommandOperation
from comms import CommunicationAdapter

LINE_FEED = "\n"
CARRIAGE_RETURN = "\r"

class CLITest(Enum):
    QUICK_CHAT = [Command.HELLO, Command.GOODBYE, Command.TERMINATOR]
    EXTENDED_CALL = [Command.HELLO, Command.HOLD, Command.TERMINATOR, 
                     Command.HELLO, Command.GOODBYE, Command.TERMINATOR]
    ON_HOLD = [Command.HELLO, Command.HOLD, Command.GOODBYE, Command.TERMINATOR,
               Command.HOLD, Command.TERMINATOR, Command.HOLD, Command.TERMINATOR,
               Command.HELLO, Command.GOODBYE, Command.TERMINATOR]
    def __init__(self, testSequence):
        self.testSequence = []
        for test in testSequence:
            self.testSequence.append(test)
        
class TestChat:
    """This class is used for handling CLI tests.
    
    This class uses the comms module for sending the test commands to the connected device.
    """
    
    def __init__(self, commLayer: CommunicationAdapter):
        self.commLayer = commLayer
    
    def runTests(self):
        """Run all the tests for CLI commands
        
        Parameters:
        None

        Returns:
        None
        """
        
        print("\n*** Running tests ***")
        print("\n\tTest 1: Quick Chat")
        self.runSingleTest(CLITest.QUICK_CHAT)
        print("")
        print("\n\tTest 2: Extended Call")
        self.runSingleTest(CLITest.EXTENDED_CALL)
        print("")
        print("\n\tTest 3: On Hold")
        self.runSingleTest(CLITest.ON_HOLD)
        print("")
        
    def runSingleTest(self, testType: CLITest):
        transmitBuffer = []
        for i in range(len(testType.testSequence)):
            if testType.testSequence[i] != Command.TERMINATOR:
                self.appendCommand(transmitBuffer, testType.testSequence[i])
            else:
                self.exchangeCommands(transmitBuffer)
                transmitBuffer = []

    def appendCommand(self, transmitBuffer, txCommand):
        if transmitBuffer == []:
            print("\n\tRequest:", end = "\t" )
        self.printItem(txCommand.commandKey)
        transmitBuffer.append(txCommand)
                
    def exchangeCommands(self, transmitBuffer):
        print("\n\tResponse:", end = " " )
        receiveBuffer = self.transmitCommands(transmitBuffer)
        for response in receiveBuffer:
            self.printItem(response)
    
    def printItem(self, item):
        print("\t" + item.strip("\n"), end = "\t")
    
    def transmitCommands(self, transmitBuffer):
        receiveBuffer = []
        for command in transmitBuffer:
            receiveBuffer.append(self.commLayer.exchangeData(command.message + LINE_FEED + CARRIAGE_RETURN))
        return receiveBuffer