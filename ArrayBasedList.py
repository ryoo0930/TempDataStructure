from MyList import _MyList

class _ArrayBasedList(_MyList):
    length = 0
    
    def __init__(self, size):
        self.item = size * [None]
        self.length = 0
        
    def len(self):
        return self.length
    
    def getItem(self, j):
        if (self.length > j):
            return self.item[j]
        raise ValueError('Value not in list')
    
    def setItem(self, val, j):
        if (self.length > j):
            self.item[j] = val
        raise ValueError('Index is out of bound')
    
    def insertItem(self, item, j = 0):
        if 0 <= j <= self.length:
            for i in range(self.length, j, -1):
                self.item[i] = self.item[i - 1]
            self.item[j] = item
            self.length += 1
            return
        raise ValueError('Index is out of bound')
    
    def removeItem(self, j = 0):
        if 0 <= j <= self.length:
            for i in range(j, self.length - 1):
                self.item[i] = self.item[i + 1]
            self.item[self.length - 1] = None
            self.length -= 1
            return
        raise ValueError('Index is out of bound')
        
    def printMyList(self):
        for i in range(self.length):
            print(self.item[i], end = ' ')
        print("")
        
    def __iter__(self):
        for i in range(self.length):
            yield self.item[i]
    
            
