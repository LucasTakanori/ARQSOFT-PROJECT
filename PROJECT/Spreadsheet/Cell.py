class Coordinate:
    def __init__(self, rowNum, colNum):
        self.rowNum = rowNum
        self.colNum = colNum

class Content:
    def __init__(self, data):
        self.data = data

class Cell:
    def __init__(self, rowNum, colNum):
        self.coordinate = Coordinate(rowNum, colNum)
        self.refCells = []
        self.content = None

    def getCoordinate(self):
        return self.coordinate

    def setCoordinate(self, coordinate):
        self.coordinate = coordinate

    def setContent(self, content):
        self.content = content

    def getContent(self):
        return self.content

    def getRefCells(self):
        return self.refCell
