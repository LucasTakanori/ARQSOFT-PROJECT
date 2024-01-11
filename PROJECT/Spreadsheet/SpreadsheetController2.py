from Controller.UserInterface import UserInterface
from Exceptions.SpreadsheetException import SpreadSheetException
from Spreadsheet.Spreadsheet import Spreadsheet
from Spreadsheet.Actions.Saver import Saver
from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.ShowContent import ShowContent
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
import sys
from pathlib import Path
import random 
import string
import os

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir.parent.parent))


class SpreadSheetController:
    
    def __init__(self):
        self.UI = UserInterface()
        self.spreadSheet = None
        self.command_history = " " #Cadena que almacena los comandos ejecutados 
        self.spreadSheet_created = False #Flag para verificar si se ha creado el spreadsheet correspondiente 
        self.spreadSheets = {}
        self.saver = Saver()
        self.loader = Loader()
        self.show = ShowContent()
    
    def showMenu(self):
        command = self.UI.main_menu()
        self.applyCommand(command)

    def imprimir(self):
        self.data = [[0.0 for _ in range(self.cols)] for _ in range(self.rows)]
        print("   " + " ".join(chr(i) for i in range(65, 65 + self.cols)))
        for i, row in enumerate(self.data, start=1):
            print(f"{i:2d} {' '.join(str(cell) for cell in row)}")

    def create_new_spreadsheet(self):
        spreadsheet_id = random.choices(string.ascii_lowercase)
        self.spreadsheet = Spreadsheet(spreadsheet_id)

    def editar_celda(spreadsheet, fila, columna, valor):
        spreadsheet[fila - 1][columna] = valor
    
    def applyCommand(self, command):
        
        if command[0] == 'C':  # Create
            self.command_history += 'C, '
            self.spreadSheet_created = True
            new_spreadsheet_name = input("Enter the name for the new spreadsheet: ")

            if new_spreadsheet_name in self.spreadSheets and self.spreadSheet is not None:
                raise SpreadSheetException(f"A spreadsheet with the name '{new_spreadsheet_name}' already exists.")

            directory_path = "/Users/eliacandela/ARQSOFT-LAB/PROJECT/"
            file_path = os.path.join(directory_path, f"{new_spreadsheet_name}.s2v")

            with open(file_path, 'w') as file:
                file.write("")

            # Crear un nuevo objeto Spreadsheet y asignarlo a self.spreadSheet
            self.spreadSheet = Spreadsheet(new_spreadsheet_name)

            # Imprimir el nuevo Spreadsheet
            print("New spreadsheet created:")
            print(self.spreadSheet)
                
        elif command[0] == 'S':  # Save
            if not self.spreadSheet:
                print("¡Crea un spreadsheet primero!")
            else:
                filename = input("Enter filename to save the Spreadsheet: ")
                Saver.save_spreadsheet_to_file(self.spreadSheet, filename)

        elif command[0] == 'L':  # Load
            self.command_history += 'L, '
            try:
                filename = input("Enter the name of the spreadsheet file to load:")
                self.loader.load_s2v_to_spreadsheet(filename)
            except:
                raise ReadingSpreadsheetException("Spreadsheet can not be load it")

        elif command[0] == 'RF':  # Read Commands File
            self.command_history += 'RF, '
            try:
                self.show.printContentSpreadsheet(self.spreadSheet)
            except:
                raise SpreadSheetException("Spreadsheet can not be save it")
        elif command[0] == 'E':  # Edit
            # self.command_history += 'E, '
            # try:
            #     self.show.printContent(self.spreadSheet)
            #     save_after_edit = input("Do you want to save the changes? (y/n): ").lower()
            #     if save_after_edit == 'y':
            #         self.saver.run_saver(self.spreadSheet)
            # except:
            #     raise SpreadSheetException("Spreadsheet can not be edited")

            if not self.spreadSheet_created:
                print("¡Crea un spreadsheet primero!")
            else:
                fila = int(input("Ingrese el número de fila: "))
                columna = ord(input("Ingrese la letra de la columna: ")) - 65
                valor = input("Ingrese el nuevo valor: ")
                self.editar_celda(self.spreadSheet_created, fila, columna, valor)
                print(f"Celda ({fila}, {chr(columna + 65)}) editada.")
                # comando = input("Ingrese el comando de edición (por ejemplo, B1=4 o C4=A1+B2): ")
                # self.imprimir_spreadsheet(self.spreadSheet)
        elif command[0] == 'Q':
            print('You have selected to end the execution of the programm')
            sys.exit()            
            





            