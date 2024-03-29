import sys
from pathlib import Path
#from PROJECT.Spreadsheet.Spreadsheet import Spreadsheet

current_dir = Path(__file__).resolve().parent
#print('BUENAS')
#print(current_dir)
#dir = str(current_dir.parent.parent.parent.parent.parent)
#print('TETAS')
#print(str(dir))


sys.path.append(str(current_dir.parent.parent.parent.parent.parent))
#from PROJECT.Spreadsheet.Spreadsheet import Spreadsheet
from Spreadsheet.Spreadsheet import Spreadsheet
from SpreadsheetMarkerForStudents.usecasesmarker.spreadsheet_controller_for_checker import ISpreadsheetControllerForChecker

class SpreadSheetFactoryForChecker:

    ##@brief Creates and returns an object of a class that implements the methods specified within
    # ISpreadsheetControllerForChecker (this emulates an interface for encapsulating your particular implementation of
    # a controller, and that includes only the methods required for marking your project features). This method
    # must create the framework of objects that allow that, once finalized its execution,
    # everything is ready for invoking the methods of the object implementing the methods specified within
    # ISpreadsheetControllerForChecker and starting setting contents in the spreadsheet cells and start checking results
    # and marking your code
    # @return an object of a class that implements the methods specified within ISpreadsheetControllerForChecker.

    def create_spreadsheet_controller() -> ISpreadsheetControllerForChecker:
        #REPLACE THE FOLLOWING CODE!!!
        return Spreadsheet('test')
        # raise Exception("SpreadsheetFactoryForChecker::" \
        #                 + "create_spreadsheet_controller(). You MUST implement the code of " \
        #                 + "this method in this class. The code MUST create a class that " \
        #                 + "implements the methods specified within ISpreadsheetControllerForChecker. " \
        #                 + "This code must create the framework of objects that allow that, once finalized its execution, " \
        #                 + "everything is ready for invoking the methods of the object implementing the methods specified within " \
        #                 + "ISpreadsheetControllerForChecker and starting setting contents in the spreadsheet cells and start checking results " \
        #                 + "marking your code"
        #                 )