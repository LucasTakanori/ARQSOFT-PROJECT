

class ReadingSpreadsheetException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __init__(self,mssg):
        Exception.__init__(self,mssg)