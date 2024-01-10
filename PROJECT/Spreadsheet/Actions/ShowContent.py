from Spreadsheet.CellRange import CellRange
from Spreadsheet.Spreadsheet import Spreadsheet

class ShowContent:

    def __init__(self):
        pass

    def printContentSpreadsheet(self, spreadsheet_data):
        if not spreadsheet_data:
            print("No data to display.")
            return

        for row in spreadsheet_data:
            for cell_data in row:
                print(cell_data.replace(';', '\t'), end='\t')
            print()

    # def calculate_row_range(self):
    #     range_list = CellRange(self.name).boundaries_to_coordinates_list()
    #     all_rows = [coord[0] for coord in range_list]
    #     return min(all_rows), max(all_rows) if all_rows else (1, 1)