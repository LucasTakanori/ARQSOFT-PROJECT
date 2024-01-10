from typing import List
from rich import print
from Spreadsheet.Cell import Cell
from Spreadsheet.Coordinate import Coordinate

class CellRange:
    def __init__(self, range_string : str) -> None:
        self.range_string = range_string
        self.min_col = None
        self.max_col = None
        self.min_row = None
        self.max_row = None
    
    def get_range(self) -> List[Coordinate]:
        print(self.range_string)
        if ":" not in self.range_string:
            return [Coordinate(*Coordinate.coordinate_to_xy(self.range_string))]
        self.min_row, self.min_col, self.max_row, self.max_col = range_boundaries(self.range_string)
        # print(self.min_row, self.min_col, self.max_row, self.max_col)
        return boundaries_to_coordinates_list(self.min_row, self.min_col, self.max_row, self.max_col)
    
def range_boundaries(range_string : str):
    """
    Convert a range string into a tuple of boundaries:
    (min_col, min_row, max_col, max_row)
    Cell coordinates will be converted into a range with the cell at both end
    """
    first_coordinate, last_coordinate = range_string.split(":")
    print(first_coordinate, last_coordinate)
    min_row, min_col = Coordinate.coordinate_to_xy(first_coordinate)
    max_row, max_col = Coordinate.coordinate_to_xy(last_coordinate)
    return min_row, min_col, max_row, max_col

def boundaries_to_coordinates_list(min_row, min_col, max_row, max_col) -> List[Coordinate]:
    return [Coordinate(row, column) for row in range(min_row, max_row+1) for column in range(min_col, max_col+1)]
    # range_list = []
    # for i in range(min_row, max_row):
    #     for j in range(min_col, max_col):
    #         range_list.append(Coordinates(i,j))
    # return range_list

if __name__ == '__main__':
    #rango = CellRange("A2")
    rango2 = CellRange("A1:G2")
    print(rango2)
    #print(rango.get_range())