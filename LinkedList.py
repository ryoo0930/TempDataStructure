from MyList import _MyList

class _Node(object):
    
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        self.next_node = new_next
        
class _LinkedList(_MyList):
    
    def __init__(self, head = None):
        self.head = None
        self.length = 0
        
    def len(self):
        return self.length
    
    def getItem(self, j):
        if 0 <= j < self.length:
            current_node = self.head
            for i in range(j):
                current_node = current_node.get_next()
            return current_node.get_data()
        raise ValueError('Index is out of bound')
    
    def setItem(self, val, j):
        if 0 <= j < self.length:
            current_node = self.head
            for i in range(j):
                current_node = current_node.get_next()
            current_node.set_data(val)
            return
        raise ValueError('Index is out of bound')
    
    def insertItem(self, item, j=0):
        if not 0 <= j <= self.length:
            raise ValueError('Index is out of bound')
        
        new_node = _Node(item)
        if j == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            current_node = self.head
            for i in range (j - 1):
                current_node = current_node.get_next()
            new_node.set_next(current_node.get_next())
            current_node.set_next(new_node)
        self.length += 1
    
    def removeItem(self, j = 0):
        if not 0 <= j <= self.length:
            raise ValueError('Index is out of bound')
        
        if j == 0:
            self.head = self.head.get_next()
        else:
            current_node = self.head
            for i in range (j - 1):
                current_node = current_node.get_next()
            current_node.set_next(current_node.get_next().get_next())
        self.length -= 1
                
    def printMyList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data(), end = ' ')
            current_node = current_node.get_next()
        print("")
            
    
                
    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.get_data()
            current_node = current_node.get_next()
        
            