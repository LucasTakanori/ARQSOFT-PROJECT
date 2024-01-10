from typing import List
from rich import print
from PROJECT.Spreadsheet.Cell import Cell
from PROJECT.Spreadsheet.Coordinate import Coordinate

#from typing import List
#from rich import print
#from Spreadsheet.Cell import Cell
#from Spreadsheet.Coordinate import Coordinate




class CellRange:
    def __init__(self, range_string : str) -> None:
        self.range_string = range_string
        self.min_col = None
        self.max_col = None
        self.min_row = None
        self.max_row = None
    
    # def get_range(self) -> List[Coordinate]:
    #     if ":" not in self.range_string:
    #         return [Coordinate(*Coordinate.coordinate_to_xy(self.range_string))]
    #     self.min_row, self.min_col, self.max_row, self.max_col = self.range_boundaries(self.range_string)
    #     return self.boundaries_to_coordinates_list(self.min_row, self.min_col, self.max_row, self.max_col)
    
    def range_boundaries(self, range_string : str):
        """
        Convert a range string into a tuple of boundaries:
        (min_col, min_row, max_col, max_row)
        Cell coordinates will be converted into a range with the cell at both end
        """
        first_coordinate, last_coordinate = range_string.split(":")
        min_row, min_col = Coordinate.coordinate_to_xy(first_coordinate)
        max_row, max_col = Coordinate.coordinate_to_xy(last_coordinate)
        return min_row, min_col, max_row, max_col


    def get_range(self) -> List[str]:
        if ":" not in self.range_string:
            coord = Coordinate.coordinate_to_xy(self.range_string)
            return [Coordinate.to_spreadsheet_format(*coord)]
        self.min_row, self.min_col, self.max_row, self.max_col = self.range_boundaries(self.range_string)
        return self.boundaries_to_spreadsheet_format(self.min_row, self.min_col, self.max_row, self.max_col)

    @staticmethod
    def boundaries_to_spreadsheet_format(min_row, min_col, max_row, max_col) -> List[str]:
        result = []
        for row in range(min_row, max_row + 1):
            for col in range(min_col, max_col + 1):
                #print(row, col)
                result.append(Coordinate.to_spreadsheet_format(row, col))
        return result




    def boundaries_to_coordinates_list(min_row, min_col, max_row, max_col) -> List[Coordinate]:
        return [Coordinate(row, column) for row in range(min_row, max_row+1) for column in range(min_col, max_col+1)]
        # range_list = []
        # for i in range(min_row, max_row):
        #     for j in range(min_col, max_col):
        #         range_list.append(Coordinates(i,j))
        # return range_list



