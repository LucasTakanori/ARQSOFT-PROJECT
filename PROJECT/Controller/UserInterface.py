# from Spreadsheet.Content.TextContent import TextContent
# from Spreadsheet.Content.NumberContent import NumberContent
# from Spreadsheet.Content.FormulaContent import FormulaContent
# from Formula.FormulaEvaluator import FormulaEvaluator
# from Spreadsheet import Spreadsheet

# class SyntaxException(Exception):
#     pass

# class UserInterface:
#     def __init__(self) -> None:
#         pass

#     def main_menu(self, command):
#         print(20 * "-", "\nMain menu:", 20 * "-")
#         print("Now yo can choice with the next commands: ")
#         print("\t1. If you want to edit the spreadsheet, press E.")
#         print("\t--> Info del edit.... ")
#         print("\t2. If you want to save the spreadsheet, press S.")
#         print("\t--> Info del save.... ")
#         print("\t3. If you want to read commands file, press RF.")
#         print("\t--> Info del read commands.... ")
#         print("\t4. If you want to load an s2v file, press L.")
#         print("\t--> Info del load.... ")
#         print("\t5. If you want to create a new spreadsheet, press C.")
#         print("\t--> Info del load.... ")
        
#         user_input = input("Ingrese su opción: ").upper().split(' ') # Convertir a mayúsculas para manejar entradas en minúsculas
#         if user_input[0]!="RF" and user_input[0]!="C" and user_input[0]!="E" and user_input[0]!="L" and user_input[0]!="S":
#             raise SyntaxException("Command not correct")
#         else:
#             return user_input
        
import sys
sys.path.append('/Users/eliacandela/ARQSOFT-LAB/PROJECT')

import tkinter as tk
from tkinter import messagebox
from Exceptions.SpreadsheetException import SpreadSheetException

class UserInterface:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Spreadsheet GUI")
        self.command_var = tk.StringVar()
        self.new_spreadsheet_name_var = tk.StringVar()

    def main_menu(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=20)

        label = tk.Label(frame, text="Main Menu", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=2, pady=10)

        options = [
            ("Edit Spreadsheet", "E"),
            ("Save Spreadsheet", "S"),
            ("Read Commands File", "RF"),
            ("Load S2V File", "L"),
            ("Create New Spreadsheet", "C")
        ]

        for i, (text, command) in enumerate(options, start=1):
            button = tk.Button(frame, text=f"{i}. {text}", command=lambda c=command: self.set_command(c))
            button.grid(row=i, column=0, sticky="w", pady=5)

        entry_label = tk.Label(frame, text="Enter your option:")
        entry_label.grid(row=len(options) + 1, column=0, pady=10)

        entry = tk.Entry(frame, textvariable=self.command_var)
        entry.grid(row=len(options) + 1, column=1, pady=10)

        submit_button = tk.Button(frame, text="Submit", command=self.handle_submit)
        submit_button.grid(row=len(options) + 2, column=0, columnspan=2, pady=10)

        self.root.mainloop()

    def set_command(self, command):
        self.command_var.set(command)

    def handle_submit(self):
        user_input = self.command_var.get().upper().split(' ')
        try:
            if user_input[0] not in ["RF", "C", "E", "L", "S"]:
                raise SpreadSheetException("Command not correct")
            else:
                if user_input[0] == 'C':
                    self.get_new_spreadsheet_name_from_user()
                else:
                    messagebox.showinfo("Command Selected", f"Command Selected: {user_input}")
        except SpreadSheetException as e:
            messagebox.showerror("Error", str(e))

    def get_new_spreadsheet_name_from_user(self):
        name_prompt = tk.Toplevel(self.root)
        name_prompt.title("New Spreadsheet Name")

        prompt_label = tk.Label(name_prompt, text="Enter the name for the new spreadsheet:")
        prompt_label.grid(row=0, column=0, padx=10, pady=10)

        entry = tk.Entry(name_prompt, textvariable=self.new_spreadsheet_name_var)
        entry.grid(row=1, column=0, padx=10, pady=10)

        submit_button = tk.Button(name_prompt, text="Submit", command=name_prompt.destroy)
        submit_button.grid(row=2, column=0, padx=10, pady=10)

        name_prompt.wait_window(name_prompt)

