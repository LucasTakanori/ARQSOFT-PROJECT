from Spreadsheet.Content.TextContent import TextContent
from Spreadsheet.Content.NumberContent import NumberContent
from Spreadsheet.Content.FormulaContent import FormulaContent
from Formula.FormulaEvaluator import FormulaEvaluator
from Exceptions.SpreadsheetException import SpreadSheetException

class UserInterface:
    def __init__(self) -> None:
        pass

    def main_menu(self):
        print("\n\tMain menu:")
        print("\tSelect Action: ")
        print("\t1. Edit a cell, press E.")
        print("\t2. Save the spreadsheet, press S.")
        print("\t4. Load an s2v file, press L.")
        print("\t5. Create a new spreadsheet, press C.")
        print("\t6. Quit, press Q.\n")

        user_input = input("\tSelection: ").upper().split(' ') # Convertir a mayúsculas para manejar entradas en minúsculas
        if user_input[0]!="RF" and user_input[0]!="C" and user_input[0]!="E" and user_input[0]!="L" and user_input[0]!="S" and user_input[0]!="Q":
            raise SpreadSheetException("Command not correct")
        else:
            return user_input
        
