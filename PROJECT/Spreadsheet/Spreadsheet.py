import os
import sys
from pathlib import Path


current_dir = Path(__file__).resolve().parent

sys.path.append(str(current_dir.parent.parent))

#from PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependencies_test import CircularDependenciesTest
from PythonProjectAutomaticMarkerForGroupsOf2.PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependency_exception import CircularDependencyException
from PROJECT.Spreadsheet.Content.FormulaContent import FormulaContent
from collections import OrderedDict
from PROJECT.Spreadsheet.Cell import Cell
from PROJECT.Spreadsheet.Coordinate import Coordinate
from PROJECT.Spreadsheet.Actions.Loader import Loader
from PROJECT.Spreadsheet.Actions.Saver import Saver
#from PROJECT.Spreadsheet.Actions.Saver import Saver

#from Spreadsheet.Cell import Cell

#from Cell import Cell
from PROJECT.Spreadsheet.CellRange import CellRange
from rich import print
sys.path.append(str(current_dir.parent.parent))

class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.dependent_cells = {}
        

    def get(self, coordinate):
        if isinstance(self.cells.get(coordinate).get_content(), FormulaContent): 
            self.cells.get(coordinate).get_content().calculate_formula(self)
            return self.cells.get(coordinate, None)
        else:
            return self.cells.get(coordinate, None)
    
    def get_values_from_range(self, range):
        range_list = CellRange(range).get_range()
        values = []
        for cell in range_list:
            if cell in self.cells:
                values.append(self.cells[cell].get_content().get_value())
        return values
    


    def set(self, coordinate, value): #Introduce a coordinate and the value to this one 
        self.cells[coordinate] = Cell(coordinate, value, self)
        #print("Set cell {} to {}".format(coordinate, value))

    def set_cell_content(self, coord, str_content):
        self.set(coord, str_content)

    def get_cell_content_as_float(self, coord):
        return self.get(coord).get_content().get_value()
    
    def get_cell_content_as_string(self, coord):
        return self.get(coord).get_content().get_value()
    
    def get_cell_formula_expression(self, coord):
        #print(coord)
        return self.get(coord).get_content().get_formula()
    
    def save_spreadsheet_to_file(self, s_name_in_user_dir):
        Saver().save_spreadsheet_to_file(s_name_in_user_dir, self)
   
    
    def load_spreadsheet_from_file(self,  s_name_in_user_dir):
        path = os.path.join(os.getcwd(),s_name_in_user_dir)
        print("loading",path)
        return Loader().load_s2v_to_spreadsheet(path, self)


    def __str__(self):
        # Determine the size of the spreadsheet based on the cell keys
        max_row, max_col = 0, 0
        for coord in self.cells:
            row, col = Coordinate.coordinate_to_xy(coord)
            max_row = max(max_row, row)
            max_col = max(max_col, col)

        # Create a string representation of the spreadsheet
        result = []

        # Header with column letters
        header = "\t" + "\t".join(chr(64 + col_num) for col_num in range(1, max_col + 1))
        result.append(header)

        # Iterate over each cell in the rectangular matrix
        for row_num in range(1, max_row + 1):
            row_values = [str(row_num)]
            for col_num in range(1, max_col + 1):
                coord = Coordinate.to_spreadsheet_format(row_num, col_num)
                #print(coord)
                if(coord in self.cells):
                    cell = self.get(coord)
                    if isinstance(cell.get_content(), FormulaContent): 
                        output = str(cell.get_content().get_formula())
                        #print(cell.get_content().get_value())
                        if cell.get_content().get_value() is not None:
                            output += '=' + str(cell.get_content().get_value())
                    else:
                        output = str(cell.get_content().get_value())
                else:
                    output = ""
                row_values.append(output)
                output = ""
            result.append('\t'.join(row_values))

        return '\n'.join(result)

