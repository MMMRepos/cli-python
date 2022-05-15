import serial, serial.tools.list_ports

class CommunicationAdapter:
    """This class is used to communicate with an embedded device.
    
    This class uses the PySerial module for communication over UART.
    """
    
    def __init__(self):
        self.serialObject = None
        self.commPortsList = []
    
    def displayCommPorts(self):
        """Print the list of available COM ports.
        
        Parameters:
        None

        Returns:
        None
        """
        
        ports = serial.tools.list_ports.comports()
        # loop through the ports
        for port, desc, hwid in sorted(ports):
            self.commPortsList.append(port)
            # print("Found {}: {} [{}]".format(port,desc,hwid))
        if self.commPortsList == []:
            print("No COM ports connected")
            return 
        else:
            print("Available COM ports", end = " ")
            print(self.commPortsList)
            return 

    def openComPort(self, portNumber = "COM3", baudrate = 9600, timeout = 1):
        """Open port with specified settings.
        
        Parameters:
        portNumber: The name of the COM port to be opened. E.g.: COM3, COM4, COM5, etc.
        baudrate: Speed of data exchange.
        timeout: Time (seconds) to wait for a response from the connected device

        Returns:
        serialObject: Initialized COM port object
        """
        
        self.serialObject = serial.Serial(self.selectComPort(portNumber), baudrate = baudrate, timeout = timeout)
    
    
    def exchangeData(self, command):
        """Exchange data with a device over UART using the opened COM port
        
        Parameters:
        command: String or data bytes to be sent

        Returns:
        str: Response from the connected device in ASCII format
        """
        
        self.sendData(command)
        return self.receiveData()
    
    def selectComPort(self, portNumber):
        if portNumber in self.commPortsList:
            print("Selected {}".format(portNumber))
            return portNumber
        else:
            print("{} not available".format(portNumber))
            return None
    
    def sendData(self, data):
        if isinstance(data, str):
            self.serialObject.write(data.encode())
        else:
            self.serialObject.write(data)
        
    def receiveData(self):
        return self.serialObject.readline().decode('ascii')
    
        
    