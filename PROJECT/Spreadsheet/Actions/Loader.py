import os
import csv
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from Spreadsheet.Actions.ShowContent import ShowContent
from Spreadsheet.Spreadsheet import Spreadsheet

class Loader:
    def __init__(self):
        pass

    def promptForFilePath(self):
        filePath = input("Enter the file path: ")
        if filePath.strip():  
            return filePath
        else:
            print("Invalid file path. Please provide a valid path.")
            return None

    def validateFileFormat(self, filePath):
        if filePath is None:
            raise ReadingSpreadsheetException("Invalid file path: None")
        elif not os.path.exists(filePath):
            raise ReadingSpreadsheetException("File does not exist: {}".format(filePath))

        _, ext = os.path.splitext(filePath)
        if ext.lower() not in ['.csv', '.txt', '.s2v']:
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


    def run_loader(self):
        show = ShowContent()
        filePath = self.promptForFilePath()
        if filePath:
            try:
                self.validateFileFormat(filePath)
                spreadsheet_data = self.loadSpreadsheetData(filePath)
                print(spreadsheet_data)
                show.printContentSpreadsheet(spreadsheet_data)
                #self.displaySpreadsheet(spreadsheet_data)
            except ReadingSpreadsheetException as e:
                print(f"Error: {str(e)}")
        else:
            print("No file path provided. Aborting.")
    

