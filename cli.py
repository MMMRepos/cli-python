from collections import defaultdict
from comms import CommunicationAdapter
from command import CommandFactory
from keyLogger import KeyLogger
from dfu import DeviceFirmwareUpdate
import sys

firmwareImage = [0xFA, 0xCF, 0x04, 0xF0, 0xFB, 0xCF, 0x05, 0xF0, 0xE9, 0xCF, 0x06, 0xF0, 0xEA, 0xCF, 0x07, 0xF0,
                 0xE1, 0xCF, 0x08, 0xF0, 0xE2, 0xCF, 0x09, 0xF0, 0xD9, 0xCF, 0x0A, 0xF0, 0xDA, 0xCF, 0x0B, 0xF0,
                 0xF3, 0xCF, 0x0C, 0xF0, 0xF4, 0xCF, 0x0D, 0xF0, 0xF6, 0xCF, 0x0E, 0xF0, 0xF7, 0xCF, 0x0F, 0xF0,
                 0xF8, 0xCF, 0x10, 0xF0, 0xF5, 0xCF, 0x11, 0xF0, 0xD7, 0x68, 0xD6, 0x68, 0xF2, 0x94, 0x9E, 0x96]

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
            for i in range(0, len(firmwareImage), 16):
                packet = []
                for j in range(i, i+16):
                    packet.append(firmwareImage[j])
                crcResult = bootload.crc16Calculate(packet)
                print("CRC result ", hex(crcResult))
                packet.append(crcResult & 0x00FF)
                packet.append(crcResult >> 8)
                commandResponse = commLayer.executeCommand(packet)
                print("Command response ", commandResponse)
        elif menuSelection == "4":
            print("Key Logger History")
            keyHistory.printKeyStack()
            userInput = input("Press ENTER to close the CLI")
            print(userInput)
            print("Thank you for using the CLI")
            if userInput == "":
                sys.exit()
        
        
    
if __name__ == "__main__":
    main()