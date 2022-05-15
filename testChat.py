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
    def __init__(self, commLayer: CommunicationAdapter):
        self.commLayer = commLayer
    
    def runTest(self):
        transmitBuffer = []
        print(len(CLITest.QUICK_CHAT.testSequence))
        for i in range(len(CLITest.QUICK_CHAT.testSequence)):
            print(CLITest.QUICK_CHAT.testSequence[i])
        # for command in CLITest.QUICK_CHAT.testSequence:
            if CLITest.QUICK_CHAT.testSequence[i] != Command.TERMINATOR:
                transmitBuffer.append(CLITest.QUICK_CHAT.testSequence[i])
            else:
                print(self.transmitCommands(transmitBuffer))
                transmitBuffer = []
    
    def transmitCommands(self, transmitBuffer):
        receiveBuffer = []
        for command in transmitBuffer:
            receiveBuffer.append(self.commLayer.exchangeData(command.message + LINE_FEED + CARRIAGE_RETURN))
        return receiveBuffer
            
        
    
    
    