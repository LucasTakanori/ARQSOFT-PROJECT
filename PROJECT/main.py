class PROJECT:
    def __init__(self, rowNum, colNum, spreadsheetId):
        self.rowNum = rowNum
        self.colNum = colNum
        self.spreadsheetId = spreadsheetId
        self.cells = []

    def getId(self):
        return self.spreadsheetId

    def getRowNum(self):
        return self.rowNum

    def getColNum(self):
        return self.colNum

    def getCells(self):
        return self.cells

if __name__ == "__main__":
    project = PROJECT(10, 10, 1)
    print("Spreadsheet ID:", project.getId())
    print("Spreadsheet Row Number:", project.getRowNum())
    print("Spreadsheet Column Number:", project.getColNum())
    print("Spreadsheet Cells:", project.getCells())


# from SpreadSheet.usecases.SpreadSheetController import SpreadSheetController

# if __name__ == "__main__":
#     spreadsheetcontroller = SpreadSheetController()
#     while True:
        
#         try:
#             spreadsheetcontroller.showMenu()
#         except Exception as Error:
#             print(Error.message)