import os
import argparse
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from Spreadsheet.Cell import Cell

class Saver:
    def __init__(self):
        pass

    def promptForFileName(self, file_extension):
        file_name = input(f"Enter the file name: ")
        file_name += file_extension
        return file_name

    def promptForDirectory(self):
        directory_path = input("Enter the directory path: ")
        return directory_path

    def validateFileName(self, fileName):
        if not os.path.splitext(fileName)[0]:
            raise SavingSpreadsheetException("Invalid file name.")

    def validateDirectory(self, directoryPath):
        if not os.path.exists(directoryPath):
            raise SavingSpreadsheetException("Invalid directory path.")

    def saveSpreadsheetData(self, fileName, directoryPath, spreadsheetData):
        try:
            with open(os.path.join(directoryPath, fileName), 'w') as file:
                for row in spreadsheetData:
                    file.write(';'.join(map(str, row)) + '\n')
        except Exception as e:
            raise SavingSpreadsheetException(str(e))

    def displaySaveConfirmation(self):
        print("File saved successfully.")

    def run_saver(self, spreadsheet):
        file_extension = ".s2v" 
        file_name = self.promptForFileName(file_extension)
        directory_path = self.promptForDirectory()
        coord = sorted(set(coord for coord in spreadsheet.get.keys()))
        max_row = max(int(coord[1:]) for coord in coord)

        #lista de letras de A a Z
        letras = [chr(letra) for letra in range(ord(coord[0][0]), ord(coord[-1][0]) + 1)]

        spreadsheet_data = []
        spreadsheet_data = [
            [
                str(spreadsheet.cells.get(f"{col}{row}", Cell()).content.getValue()).replace(";", ",") + ";"
                for col in letras
            ]
            for row in range(1, max_row + 1)
        ]

        if file_name and directory_path:
            try:
                self.validateFileName(file_name)
                self.validateDirectory(directory_path)
                self.saveSpreadsheetData(file_name, directory_path, spreadsheet_data)
                self.displaySaveConfirmation()
            except SavingSpreadsheetException as e:
                print(f"Error: {str(e)}")