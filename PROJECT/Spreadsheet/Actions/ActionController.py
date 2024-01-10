from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.Saver import Saver

class ActionController:
    def __init__(self) -> None:
        self.loader = Loader()
        self.saver = Saver()

    def load_file(self, filename, spreadsheet):
        self.loader

    def save_file(self, spreadsheet): 
        self.saver.run_saver(spreadsheet)