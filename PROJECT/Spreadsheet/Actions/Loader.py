import os
import csv
#from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
#from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
#from Spreadsheet.Actions.ShowContent import ShowContent
#from Spreadsheet.Spreadsheet import Spreadsheet

class Loader:
    def __init__(self):
        pass

    def load_s2v_to_dict(filename):
        """
        Load a .s2v file and return its contents as a dictionary.
        Each key in the dictionary is a cell coordinate like 'A1', and the value is the content of the cell.
        Before storing the cell content, replace every comma ',' with a semicolon ';'.
        """
        result = {}
        with open(filename, 'r') as file:
            rows = file.readlines()
            for row_idx, row in enumerate(rows, start=1):
                cells = row.strip().split(';')  # Splitting the row into cells
                for col_idx, cell in enumerate(cells, start=1):
                    cell_key = f'{chr(64 + col_idx)}{row_idx}'  # Converts column index to letter (1 -> A, 2 -> B, etc.)
                    modified_cell = cell.replace(',', ';')  # Replace commas with semicolons
                    result[cell_key] = modified_cell
        return result



    def initialize_spreadsheet_from_dict(spreadsheet, data_dict):
        """
        Initializes a Spreadsheet object with values from a dictionary.
        
        :param spreadsheet: An instance of the Spreadsheet class.
        :param data_dict: A dictionary where keys are cell coordinates (e.g., 'A1') 
                        and values are the contents of those cells.
        """
        for coord, value in data_dict.items():
            spreadsheet.set_cell_content(coord, value)
    

    def load_s2v_to_spreadsheet(self, filename, spreadsheet):
        """
        Load a .s2v file and initialize a Spreadsheet object with its contents.
        """
        data_dict = Loader.load_s2v_to_dict(filename)
        Loader.initialize_spreadsheet_from_dict(spreadsheet, data_dict)
        return spreadsheet