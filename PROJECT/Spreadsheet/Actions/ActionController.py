from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.Saver import Saver

class ActionController:
    def __init__(self) -> None:
        self.loader = Loader()
        self