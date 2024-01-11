import os
from PROJECT.Spreadsheet.Content.FormulaContent import FormulaContent

from PROJECT.Spreadsheet.Coordinate import Coordinate

class Saver:
    def __init__(self):
        pass

    def retrieve_data_from_spreadsheet(spreadsheet):
        result = {}
        for coord in spreadsheet.cells:
            if isinstance(spreadsheet.cells.get(coord).get_content(), FormulaContent): 
                cell_content = spreadsheet.get_cell_formula_expression(coord)
            else:
                cell_content = spreadsheet.cells.get(coord).get_content().get_value()
                if isinstance(cell_content, float) and cell_content == int(cell_content):
                    cell_content = int(cell_content)

            cell_content = str(cell_content).replace(';', ',')    
            result[coord] = cell_content
        return result

    @staticmethod
    def save_dict_to_s2v(filename, data_dict):
        row_dimensions = Saver.get_spreadsheet_row_dimensions(data_dict)
        grid = [["" for _ in range(row_dimensions[row])] for row in sorted(row_dimensions.keys())]

        for coord, cell_value in data_dict.items():
            row, col = Coordinate.coordinate_to_xy(coord)
            grid[row-1][col-1] = cell_value  # Adjust for zero-indexing

        with open(filename, 'w') as file:
            for row in grid:
                file.write(';'.join(row))
                file.write('\n')

    def save_spreadsheet_to_file(self, filename, spreadsheet):
        data_dict = Saver.retrieve_data_from_spreadsheet(spreadsheet)
        Saver.save_dict_to_s2v(filename, data_dict)

    @staticmethod
    def get_spreadsheet_row_dimensions(data_dict):
        row_dimensions = {}
        for coord in data_dict.keys():
            row, col = Coordinate.coordinate_to_xy(coord)
            if row not in row_dimensions:
                row_dimensions[row] = col
            else:
                row_dimensions[row] = max(row_dimensions[row], col)
        return row_dimensions

