#from Spreadsheet.Content.Content import Content

from PROJECT.Spreadsheet.Content.Content import Content


class TextContent(Content):
    def __init__(self, string: str):
        super(). __init__(string)
        

    def get_value(self) -> str : 
        return self.value
    
    def set_value(self, value: str) -> None:
        self.value = value