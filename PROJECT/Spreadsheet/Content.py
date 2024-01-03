from abc import ABC, abstractmethod

class Content(ABC):
    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def setValue(self):
        pass
