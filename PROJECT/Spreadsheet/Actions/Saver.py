import os
import argparse
#from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from Spreadsheet.Cell import Cell
import sys
from pathlib import Path


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

    #def validateFileName(self, fileName):
        #if not os.path.splitext(fileName)[0]:
            #raise SavingSpreadsheetException("Invalid file name.")
        #elif os.path.splitext(fileName)[1].lower() not in ['.s2v', '.txt']:
            #raise SavingSpreadsheetException("Invalid file name.")

    #def validateDirectory(self, directoryPath):
    #    if not os.path.exists(directoryPath):
    #        #raise SavingSpreadsheetException("Invalid directory path.")

    def saveSpreadsheetData(self, fileName, directoryPath, spreadsheetData):
        #try:
            with open(os.path.join(directoryPath, fileName), 'w') as file:
                for row in spreadsheetData:
                    file.write(';'.join(map(str, row)) + '\n')
        #except Exception as e:
            #raise SavingSpreadsheetException(str(e))

    def displaySaveConfirmation(self):
        print("File saved successfully.")

    def run_saver(self, filename, spreadsheet):
        file_extension = ".s2v"
        file_name = filename
        directory_path = current_dir = Path(__file__)#self.promptForDirectory()
        max_row = max(sorted(set(int(key[1:]) for key in spreadsheet.cells.keys())))

        if file_name and directory_path:
            #try:
                #self.validateFileName(file_name)
                #self.validateDirectory(directory_path)
                letras = [chr(letra) for letra in range(ord('A'), ord('Z') + 1)]

                spreadsheet_data = [
                    [
                        str(spreadsheet.cells.get(f"{col}{row}", Cell()).content.getValue()).replace(";", ",") + ";"
                        for col in letras
                    ]
                    for row in range(1, max_row + 1)
                ]

                self.saveSpreadsheetData(file_name, directory_path, spreadsheet_data)
                self.displaySaveConfirmation()
            #except SavingSpreadsheetException as e:
            #    print(f"Error: {str(e)}")