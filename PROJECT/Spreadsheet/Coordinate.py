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
