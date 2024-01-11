from PROJECT.Spreadsheet.Content.Content import Content
from PROJECT.Formula.EvaluatePostfix import EvaluatePostfix
#from Formula.EvaluatePostfix import EvaluatePostfix
#from Spreadsheet.Content.Content import Content

class FormulaContent(Content):
    def __init__(self, formula, spreadsheet):
        super().__init__(formula)
        self.evaluator = EvaluatePostfix(formula)
        self.value : self.evaluator.evaluate(spreadsheet)#float = None
        self.formula = formula

    def get_value(self) -> float : 
        return self.value
    
    def get_formula(self) -> str:
        return self.formula
    
    def set_value(self, formula: str) -> None:
        self.formula = formula

    def calculate_formula(self, spreadsheet):        
        self.value = self.evaluator.evaluate(spreadsheet)
        

    def __repr__(self) -> str:
        return f"Formula: {self.formula}, Value: {self.value}"
    

    