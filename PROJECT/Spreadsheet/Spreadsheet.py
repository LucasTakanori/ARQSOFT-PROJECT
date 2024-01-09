
from collections import OrderedDict
from Spreadsheet.Cell import Cell


class Spreadsheet:
    def __init__(self, name):
        self.name = name
        self.cells = {}

    def get(self, coordinate):
        return self.cells.get(coordinate, None)
    
    def set(self, coordinate, value): #Introduce a coordinate and the value to this one 
        self.cells[coordinate] = Cell(coordinate, value)
        #print("Set cell {} to {}".format(coordinate, value))
