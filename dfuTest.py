import unittest
from dfu import DeviceFirmwareUpdate
from comms import CommunicationAdapter

class TestCRC16(unittest.TestCase):
    def testForArrayWithSingleElementZero(self):
        commLayer = CommunicationAdapter()
        dfuObject = DeviceFirmwareUpdate(commLayer)
        data = [0x00]
        result = dfuObject.calculateCRC16(data)
        self.assertEqual(result, 0xE1F0)
    
    def testForArrayWithSingleNonZeroElement(self):
        commLayer = CommunicationAdapter()
        dfuObject = DeviceFirmwareUpdate(commLayer)
        data = [0xA9]
        result = dfuObject.calculateCRC16(data)
        self.assertEqual(result, 0xC533)
    
    @unittest.expectedFailure
    def testForIntegerValue(self):
        commLayer = CommunicationAdapter()
        dfuObject = DeviceFirmwareUpdate(commLayer)
        data = 0x00
        self.assertRaises("Incorrect input type",  dfuObject.calculateCRC16(data))
    
    def testForArrayWithMultipleElements(self):
        commLayer = CommunicationAdapter()
        dfuObject = DeviceFirmwareUpdate(commLayer)
        data = [0x8C, 0x2A, 0xAE, 0xEC, 0x08, 0xF0, 0x00, 0xD0, 0x11, 0xC0, 0xF5, 0xFF, 0x10, 0xC0, 0xF8, 0xFF]
        result = dfuObject.calculateCRC16(data)
        self.assertEqual(result, 0x455B)
    

if __name__ == '__main__':
    unittest.main()

    