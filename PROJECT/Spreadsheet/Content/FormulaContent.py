from Content.Content import Content

class FormulaContent(Content):
    def __init__(self, formula):
        super(). __init__("FormulaContent", formula)
        
    def getNumValue(self):
        result = self.evaluate(None)
        return result if result is not None else 0
    
    def getTextValue(self):
        return str(self.getNumValue())
    
    def getValue(self):
        return self.evaluate(None)
    
    