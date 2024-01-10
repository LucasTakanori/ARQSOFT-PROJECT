#from PROJECT.Spreadsheet.Content.Content import Content
from Spreadsheet.Content.Content import Content

class FormulaContent(Content):
    def __init__(self, formula):
        super(). __init__(formula)
        result = self.evaluate(formula)

    def get_value(self) -> str : 
        return self.value
    
    def get_result(self):
        result = self.evaluate(None)
        return result if result is not None else 0
        
    def set_value(self, value: str) -> None:
        self.value = value