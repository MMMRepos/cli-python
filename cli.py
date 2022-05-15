from collections import defaultdict
from comms import CommunicationAdapter
from keyLogger import KeyLogger

def main():
    commLayer = CommunicationAdapter()
    keyHistory = KeyLogger()
    print("CLI Task")
    print("\n*** Main Menu ***\n")
    menuDict = defaultdict(str)
    menuDict["1"] = "Send Command"
    menuDict["2"] = "Run Test"
    menuDict["3"] = "Update Device"
    menuDict["4"] = "Close"
    for key, value in menuDict.items():
        print("    " + key + ". " + value)
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
        keyHistory.printKeyStack()
    
if __name__ == "__main__":
    main()