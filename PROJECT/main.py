import sys
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir.parent))

from PROJECT.Exceptions.SpreadsheetException import SpreadSheetException
from PROJECT.Controller.SpreadsheetController import SpreadSheetController

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetController()

    while True:
        try:
            spreadsheetcontroller.showMenu()
        except SpreadSheetException as Error:
            print(str(Error))
