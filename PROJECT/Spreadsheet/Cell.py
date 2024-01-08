from Content.TextContent import TextContent
from Content.NumberContent import NumberContent
from Content.FormulaContent import FormulaContent

class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.content = None

    def modify_Content(self, content_type, content_value):
        if content_type == "text":
            self.content = TextContent(content_value)
        elif content_type == "number":
            self.content = NumberContent(float(content_value))
        elif content_type == "formula":
            self.content = FormulaContent(content_value)
        else: 
            raise ValueError("Invalid content type, rewrite")

    def get_content_value(self):
        if self.content:
            return self.content.getValue() # or use self.content.getTextValue() if we want the value as text 
        return ""
    
    def get_content_type(self):
        if self.content:
            return self.content.typeOfContent()
        return "Empty"
    
    def evaluate_formula(self, spreadsheet):
        if isinstance(self.content, FormulaContent):
            return self.content.evaluate(spreadsheet)
        return None
    