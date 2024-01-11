import os
import sys
from pathlib import Path


current_dir = Path(__file__).resolve().parent

sys.path.append(str(current_dir.parent.parent))

#from PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependencies_test import CircularDependenciesTest
# from PythonProjectAutomaticMarkerForGroupsOf2.PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependency_exception import CircularDependencyException
from Spreadsheet.Content.FormulaContent import FormulaContent
from collections import OrderedDict
from Spreadsheet.Cell import Cell
from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.Saver import Saver

#from PROJECT.Spreadsheet.Actions.Saver import Saver

#from Spreadsheet.Cell import Cell

#from Cell import Cell
from Spreadsheet.CellRange import CellRange

sys.path.append(str(current_dir.parent.parent))

class Spreadsheet:
    def __init__(self, name):
        self.name = name
        self.cells = {}
        self.dependent_cells = {}
        
    def __str__(self):
        rows = []
        for row_number in range(1, 6): 
            row_values = []
            for col_letter in range(ord('A'), ord('Z') + 1):
                coordinate = f"{chr(col_letter)}{row_number}"
                cell_value = self.cells.get(coordinate, 0.0)  
                row_values.append(cell_value)
            rows.append(row_values)
        result = []
        for row in rows:
            result.append('\t'.join(map(str, row)))
        return '\n'.join(result)

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
        path = os.path.join(os.getcwd(),s_name_in_user_dir)
        print("saving",s_name_in_user_dir)
        return Saver().save_spreadsheet_to_file(path, self)   
    
    def load_spreadsheet_from_file(self,  s_name_in_user_dir):
        path = os.path.join(os.getcwd(),s_name_in_user_dir)
        print("loading",s_name_in_user_dir)
        return Loader().load_s2v_to_spreadsheet(path, self)