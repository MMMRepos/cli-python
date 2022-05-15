from collections import deque

class KeyLogger:
    def __init__(self):
        self.keyStack = deque(maxlen = 500)
    
    def printKeyStack(self):
        print(self.keyStack)
        
    def appendLastKey(self, key):
        self.keyStack.append(key)
    
    def popLastKey(self):
        if self.keyStack:
            return self.pop()
        else:
            return None
        