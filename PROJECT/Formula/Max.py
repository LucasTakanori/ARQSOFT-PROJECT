from typing import List
from abc import ABC, abstractmethod

class Argument(ABC):
    @abstractmethod
    def getValue(self):
        pass

class Function(ABC):
    @abstractmethod
    def calculate(self):
        pass

class Max(Function):
    def __init__(self, args: List[Argument]):
        self.args = args

    def getArgs(self):
        return self.args

    def calculate(self):
        values = [arg.getValue() for arg in self.args]
        max_value = max(values)

        return max_value