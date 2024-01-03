from abc import ABC, abstractmethod

class Content(ABC):
    @abstractmethod
    def getValue(self):
        pass

    @abstractmethod
    def setValue(self, value):
        pass

class Formula(Content):
    def __init__(self, expression, value):
        self.expression = expression
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value
