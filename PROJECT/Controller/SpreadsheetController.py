from Controller.UserInterface import UserInterface
from Exceptions.SpreadsheetException import SpreadSheetException
from PythonProjectAutomaticMarkerForGroupsOf2.PythonProjectAutomaticMarkerForGroupsOf2.SpreadsheetMarkerForStudents.SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from Spreadsheet.Spreadsheet import Spreadsheet
from Spreadsheet.Actions.Saver import Saver
from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.ShowContent import ShowContent
import sys
from pathlib import Path
import random 
import string
import os
import re
from rich import print

current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir.parent.parent))


class SpreadSheetController:
    
    def __init__(self):
        self.UI = UserInterface()
        self.spreadsheet_open = False
        self.spreadsheet = Spreadsheet()
        self.command_history = " " #Cadena que almacena los comandos ejecutados 
        self.saver = Saver()
        self.loader = Loader()
        self.show = ShowContent()
        self.spreadsheetpath = {}
    
    def showMenu(self):
        command = self.UI.main_menu()
        self.applyCommand(command)

    def create_spreadsheet(self):
        spreadsheet_id = random.choices(string.ascii_lowercase)
        self.spreadsheet = Spreadsheet(spreadsheet_id)

    def applyCommand(self, command):
        print("\n\n")
        if command[0] == 'C':  # Create
            self.command_history += 'C, '
            self.spreadsheet_open = True

            # Imprimir el nuevo Spreadsheet
            print("New spreadsheet created:")
            print(self.spreadsheet)
          
        elif command[0] == 'S':  # Save
            # Prompt the user for a filename
            filename = input("Please enter a filename to save the spreadsheet: ")

            # Check if the filename has a .s2v extension
            if not filename.endswith(".s2v"):
                print("Error: The file must have a .s2v extension.")
            else:
                # Check if the file already exists
                if os.path.exists(filename):
                    overwrite = input("File already exists. Do you want to overwrite it? (yes/no): ")
                    if overwrite.lower() != 'yes':
                        print("Saving cancelled.")
                    else:
                        # Save the spreadsheet
                        try:
                            Saver().save_spreadsheet_to_file(filename, self.spreadsheet)
                            print(f"Spreadsheet saved to {filename}")
                        except Exception as e:
                            print(f"An error occurred while saving the file: {e}")
                else:
                    # Save the spreadsheet if file does not exist
                    try:
                        Saver().save_spreadsheet_to_file(filename, self.spreadsheet)
                        print(f"Spreadsheet saved to {filename}")
                    except Exception as e:
                        print(f"An error occurred while saving the file: {e}")


        elif command[0] == 'L':  # Load
            self.command_history += 'L, '
            try:
                filename = input("Enter the name of the spreadsheet file to load:")
                print("loading",filename)
                self.spreadsheet = self.loader.load_s2v_to_spreadsheet(filename,self.spreadsheet)
                print(filename, 'loaded \n',self.spreadsheet)
                self.spreadsheet_open = True
            except:
                print("Spreadsheet can not be load it")

        elif command[0] == 'RF':  # Read Commands File
            self.command_history += 'RF, '
            try:
                self.show.printContentSpreadsheet(self.spreadsheet)
            except:
                raise SpreadSheetException("Spreadsheet can not be save it")
        elif command[0] == 'E':  # Edit
            if not self.spreadsheet_open:
                print("¡Crea/abre un spreadsheet primero!")
            else:
                comando = input("Ingrese el comando de edición primero la coordenada y el contenido separado por un espacio (por ejemplo, B1 4 o C4 =A1+B2): ")

                # Analizar el comando para obtener fila, columna y valor
                parts = comando.split(" ")
                if len(parts) == 2:
                    cell_coordinate = parts[0].upper()
                    valor = parts[1]
                    pattern = r'^[A-Z]+[0-9]+$'
                    if(re.match(pattern, cell_coordinate) is not None):
                        self.spreadsheet.set(cell_coordinate, valor)
                        print("Cell {} set to {}".format(cell_coordinate, valor))
                    else:
                        print("Coordenadas no validas")
                else:
                    print("Comando de edición no válido. Asegúrate de usar el formato correcto.")
            print(self.spreadsheet)
        elif command[0] == 'Q':
            print('You have selected to end the execution of the programm')
            sys.exit()            
            