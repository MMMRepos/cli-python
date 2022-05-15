from collections import deque


class KeyLogger:
    def __init__(self):
        self.keyQueue = deque(maxlen = 500)
    
    def printKeyQueue(self):
        print(self.keyQueue)
        
    def appendLastKey(self, key):
        self.keyQueue.append(key)
    
    def popLastKey(self):
        if self.keyQueue:
            return self.popleft()
        else:
            return None
        