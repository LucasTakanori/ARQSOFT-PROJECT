from Controller.SpreadsheetController import SpreadSheetController

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetController()
    while True:
        
        try:
            spreadsheetcontroller.showMenu()
        except Exception as Error:
            print(Error.message)
