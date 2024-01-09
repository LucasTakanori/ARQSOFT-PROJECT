import tkinter as tk
from tkinter import messagebox

from Spreadsheet.Content.TextContent import TextContent
from Spreadsheet.Content.NumberContent import NumberContent
from Spreadsheet.Content.FormulaContent import FormulaContent
from Formula.FormulaEvaluator import FormulaEvaluator
from Spreadsheet import Spreadsheet

class SyntaxException(Exception):
    pass

class UserInterface:
    def __init__(self) -> None:
        pass

    def main_menu(self, command):
        print(20 * "-", "\nMain menu:", 20 * "-")
        print("Now yo can choice with the next commands: ")
        print("\t1. If you want to edit the spreadsheet, press E.")
        print("\t--> Info del edit.... ")
        print("\t2. If you want to save the spreadsheet, press S.")
        print("\t--> Info del save.... ")
        print("\t3. If you want to read commands file, press RF.")
        print("\t--> Info del read commands.... ")
        print("\t4. If you want to load an s2v file, press L.")
        print("\t--> Info del load.... ")
        print("\t5. If you want to create a new spreadsheet, press C.")
        print("\t--> Info del load.... ")
        
        user_input = input("Ingrese su opción: ").upper().split(' ') # Convertir a mayúsculas para manejar entradas en minúsculas
        if user_input[0]!="RF" and user_input[0]!="C" and user_input[0]!="E" and user_input[0]!="L" and user_input[0]!="S":
            raise SyntaxException("Command not correct")
        else:
            return user_input