import sys
from pathlib import Path


current_dir = Path(__file__).resolve().parent

sys.path.append(str(current_dir.parent.parent))

#from PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependencies_test import CircularDependenciesTest
from PythonProjectAutomaticMarkerForGroupsOf2.PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.entities.circular_dependency_exception import CircularDependencyException
from PROJECT.Spreadsheet.Content.FormulaContent import FormulaContent
from collections import OrderedDict
from PROJECT.Spreadsheet.Cell import Cell

#from Spreadsheet.Cell import Cell

#from Cell import Cell
from PROJECT.Spreadsheet.CellRange import CellRange

sys.path.append(str(current_dir.parent.parent))

class Spreadsheet:
    def __init__(self, name):
        self.name = name
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
        return self.get(coord).get_content().get_expression()
    
    