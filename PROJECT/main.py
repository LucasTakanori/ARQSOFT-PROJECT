from Controller.SpreadsheetController import SpreadSheetController
from Exceptions.SpreadsheetException import SpreadSheetException

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetController()

    while True:
        try:
            spreadsheetcontroller.showMenu()
        except SpreadSheetException as Error:
            print(str(Error))
