import unittest
from keyLogger import KeyLogger

# Array of 500 keys
keys = ["Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close", 
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close", "Send Command", "Run Test", "Update Device", "Close",
        "Send Command", "Run Test", "Update Device", "Close"]

class TestKeyLogger(unittest.TestCase):
    def testForFirstElement(self):
        keyQueue = KeyLogger()
        for element in keys:
            keyQueue.appendLastKey(element)
        result = keyQueue.popKey()
        self.assertEqual(result, "Send Command")
    
    def testForRollOver(self):
        keyQueue = KeyLogger()
        for element in keys:
            keyQueue.appendLastKey(element)
        keyQueue.appendLastKey("Run Test")
        result = keyQueue.popKey()
        self.assertEqual(result, "Run Test")
    
    @unittest.expectedFailure
    def testForIntegerValue(self):
        keyQueue = KeyLogger()
        for element in keys:
            keyQueue.appendLastKey(element)
        
        keyQueue.appendLastKey("Run Test")
        result = keyQueue.popKey()
        self.assertEqual(result, "Send Command")
    

if __name__ == '__main__':
    unittest.main()

    