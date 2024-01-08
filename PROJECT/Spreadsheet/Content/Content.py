from abc import ABC, abstractmethod

class Content(ABC):

    def __init__(self, type, stringvalue):
        super().__init__()
        self.type =type
        self.textulvalue = stringvalue
    
    @abstractmethod
    def getNumValue(self):
        pass
    
    @abstractmethod
    def getTextValue(self):
        pass
    
    @abstractmethod
    def getValue(self):
        return self.textulvalue
    
    def typeOfContent(self):
        return self.type
