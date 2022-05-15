from comms import CommunicationAdapter

def main():
    print("CLI Task")
    print("\n*** Main Menu ***\n")
    commLayer = CommunicationAdapter()
    commLayer.displayCommPorts()
    portNumber = input("Select the port from the available COM ports ")
    baudRate = int(input("Enter the baud rate "))
    timeOut = int(input("Enter the timeout ")) 
    commLayer.openComPort(portNumber, baudRate, timeOut)
    
if __name__ == "__main__":
    main()