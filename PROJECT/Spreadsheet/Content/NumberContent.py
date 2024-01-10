from PROJECT.Spreadsheet.Content.Content import Content
#from Spreadsheet.Content.Content import Content
class NumberContent(Content):
    def __init__(self, number : float):
        super(). __init__(number)


    def get_value(self) -> float:
        return self.value
    
    def set_value(self, value: float) -> None:
        self.value = value