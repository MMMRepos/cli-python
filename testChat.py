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
        print("    ", end = "")
        # print(len(CLITest.QUICK_CHAT.testSequence))
        for i in range(len(CLITest.QUICK_CHAT.testSequence)):
            print(CLITest.QUICK_CHAT.testSequence[i].commandKey.strip("\n"), end = " ")
        # for command in CLITest.QUICK_CHAT.testSequence:
            if CLITest.QUICK_CHAT.testSequence[i] != Command.TERMINATOR:
                transmitBuffer.append(CLITest.QUICK_CHAT.testSequence[i])
            else:
                print("\n    Response", end = " " )
                print(self.transmitCommands(transmitBuffer))
                transmitBuffer = []
    
    def runOnHoldTest(self):
        transmitBuffer = []
        print("    ", end = "")
        for i in range(len(CLITest.ON_HOLD.testSequence)):
            print(CLITest.ON_HOLD.testSequence[i].commandKey.strip("\n"), end = " ")
            if CLITest.ON_HOLD.testSequence[i] != Command.TERMINATOR:
                transmitBuffer.append(CLITest.ON_HOLD.testSequence[i])
            else:
                print("\n    Response ", end = " " )
                print(self.transmitCommands(transmitBuffer))
                print("    ", end = "")
                transmitBuffer = []
    
    def runExtendedCallTest(self):
        transmitBuffer = []
        print("    ", end = "")
        for i in range(len(CLITest.EXTENDED_CALL.testSequence)):
            print(CLITest.EXTENDED_CALL.testSequence[i].commandKey.strip("\n"), end = " ")
            if CLITest.EXTENDED_CALL.testSequence[i] != Command.TERMINATOR:
                transmitBuffer.append(CLITest.EXTENDED_CALL.testSequence[i])
            else:
                print("\n    Response ", end = " " )
                print(self.transmitCommands(transmitBuffer))
                print("    ", end = "")
                transmitBuffer = []
    
    def transmitCommands(self, transmitBuffer):
        receiveBuffer = []
        for command in transmitBuffer:
            receiveBuffer.append(self.commLayer.exchangeData(command.message + LINE_FEED + CARRIAGE_RETURN))
        return receiveBuffer
    
    def runTests(self):
        print("\n*** Running tests ***\n")
        print("    Test 1: Quick Chat")
        self.runTest()
        print("")
        print("    Test 2: Extended Call")
        self.runExtendedCallTest()
        print("")
        print("    Test 3: On Hold")
        self.runOnHoldTest()
        print("")
            
        
    
    
    