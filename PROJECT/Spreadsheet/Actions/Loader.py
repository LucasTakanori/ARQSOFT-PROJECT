import os
import csv
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException

class Loader:
    def __init__(self):
        pass

    def promptForFilePath(self):
        return input("Enter the file path: ")

    def validateFileFormat(self, filePath):
        _, ext = os.path.splitext(filePath)
        if ext != '.csv':
            raise ReadingSpreadsheetException("Unsupported file format.")

    def loadSpreadsheetData(self, filePath):
        try:
            with open(filePath, 'r') as file:
                reader = csv.reader(file)
                return list(reader)
        except Exception as e:
            raise SavingSpreadsheetException(str(e))

    def displaySpreadsheet(self, spreadsheetData):
        for row in spreadsheetData:
            print(', '.join(row))

    def run(self):
        filePath = self.promptForFilePath()
        self.validateFileFormat(filePath)
        spreadsheetData = self.loadSpreadsheetData(filePath)
        self.displaySpreadsheet(spreadsheetData)
