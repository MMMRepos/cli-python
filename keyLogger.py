from collections import deque

class KeyLogger:
    """This class is used for storing the log of actions performed on using the CLI."""
    
    def __init__(self):
        self.keyQueue = deque(maxlen = 500)
    
    def printKeyQueue(self):
        """Print the actions stored in the key logger queue
        
        Parameters:
        None

        Returns:
        None
        """
        
        print(list(self.keyQueue))
        
    def appendLastKey(self, key):
        self.keyQueue.append(key)
    
    def popLastKey(self):
        if self.keyQueue:
            return self.popleft()
        else:
            return None
        