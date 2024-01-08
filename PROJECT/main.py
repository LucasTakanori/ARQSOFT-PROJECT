import tkinter as tk
from Spreadsheet.Content.TextContent import TextContent
from Spreadsheet.Content.NumberContent import NumberContent
from Spreadsheet.Content.FormulaContent import FormulaContent
from Formula.FormulaEvaluator import FormulaEvaluator
from Spreadsheet import Spreadsheet
from Spreadsheet.Cell import Cell
from Controller.UserInterface import SpreadsheetUI

def main():
    # Crear una instancia de la hoja de cálculo y la interfaz de usuario
    spreadsheet = Spreadsheet(rows=5, cols=5)
    root = tk.Tk()
    app = SpreadsheetUI(root, spreadsheet)

    # Ejemplo de cómo establecer celdas en la hoja de cálculo a través de la UI
    # Puedes hacer esto mediante la interfaz de usuario creada, pero aquí solo proporciono ejemplos
    app.set_cell_value(0, 0, "text", "Hello")
    app.set_cell_value(1, 1, "number", "42")
    app.set_cell_value(2, 2, "formula", "=A1 + B2")

    # Ejemplo de cómo calcular la hoja de cálculo a través de la UI
    app.calculate_spreadsheet()

    # Puedes agregar más interacciones con la interfaz de usuario según sea necesario

    root.mainloop()

if __name__ == "__main__":
    main()


# from SpreadSheet.usecases.SpreadSheetController import SpreadSheetController

# if __name__ == "__main__":
#     spreadsheetcontroller = SpreadSheetController()
#     while True:
        
#         try:
#             spreadsheetcontroller.showMenu()
#         except Exception as Error:
#             print(Error.message)