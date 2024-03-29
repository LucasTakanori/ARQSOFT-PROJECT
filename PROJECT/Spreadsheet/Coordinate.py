class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getRowNum(self):
        return self.row

    def getColNum(self):
        return self.col

    def setRow(self, row):
        self.row = row

    def setCol(self, col):
        self.col = col

    def column_to_number(column):
        """
        Convert a column string into a number
        """
        col_num = 0
        for char in column:
            col_num = col_num * 26 + (ord(char.upper()) - ord('A')) + 1
        return col_num

    def coordinate_to_xy(coordinate):
        """
        Convert a coordinate string into a tuple of (row, col)
        """
        col_str = ""
        row_str = ""
        for char in coordinate:
            if char.isalpha():
                row_str += char
            elif char.isdigit():
                col_str += char
        col = Coordinate.column_to_number(row_str)
        row =  int(col_str)
        return row, col

    def __repr__(self):
        return f"Coordinate(row={self.row}, col={self.col})"


    @staticmethod
    def to_spreadsheet_format(row, col):
        """
        Convert row and column numbers back to spreadsheet-style format (e.g., "A1").
        """
        col_str = ""
        while col > 0:
            col, remainder = divmod(col - 1, 26)
            col_str = chr(65 + remainder) + col_str
        return f"{col_str}{row}"
