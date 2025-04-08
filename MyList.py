from abc import ABCMeta, abstractmethod

class _MyList(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def len(self):
        pass
    @abstractmethod
    def getItem(self, j):
        pass
    @abstractmethod
    def setItem(self, val, j):
        pass
    @abstractmethod
    def insertItem(self, item, j = 0):
        pass
    @abstractmethod
    def removeItem(self, j = 0):
        pass
    @abstractmethod
    def printMyList(Self):
        pass