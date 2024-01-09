from abc import ABC, abstractmethod

class Content(ABC):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    @abstractmethod
    def get_value(self):
        pass
    
    @abstractmethod
    def set_value(self, value):
        pass
