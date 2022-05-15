import serial, serial.tools.list_ports

class CommunicationAdapter:
    def __init__(self):
        self.serialObject = None
        self.commPortsList = []
    
    def displayCommPorts(self):
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
    
    def selectComPort(self, portNumber):
        if portNumber in self.commPortsList:
            print("Selected {}".format(portNumber))
            return portNumber
        else:
            print("{} not available".format(portNumber))
            return None
    
    def openComPort(self, portNumber = "COM3", baudrate = 9600, timeout = 1):
        self.serialObject = serial.Serial(self.selectComPort(portNumber), baudrate = baudrate, timeout = timeout)
        # Add an exception when COM port fails to open
        
    def sendData(self, data):
        if isinstance(data, str):
            self.serialObject.write(data.encode())
        else:
            self.serialObject.write(data)
        
    def receiveData(self):
        return self.serialObject.readline().decode('ascii')
    
    def exchangeData(self, command):
        self.sendData(command)
        return self.receiveData()
        
        
    