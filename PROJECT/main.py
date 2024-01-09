from Controller.UserInterface import UserInterface

if __name__ == "__main__":
    spreadsheetcontroller = SpreadSheetController()
    while True:
        
        try:
            spreadsheetcontroller.showMenu()
        except Exception as Error:
            print(Error.message)
        
if __name__ == "__main__":
    user = Main()
    main.promptUser()