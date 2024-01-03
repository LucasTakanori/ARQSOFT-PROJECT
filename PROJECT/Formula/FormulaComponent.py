from abc import ABC, abstractmethod

class FormulaComponent(ABC):
    @abstractmethod
    def method_to_implement(self):
        pass