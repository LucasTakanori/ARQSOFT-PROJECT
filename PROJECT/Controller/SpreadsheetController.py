from Controller.UserInterface import UserInterface
from Exceptions.SpreadsheetException import SpreadSheetException
from Spreadsheet.Spreadsheet import Spreadsheet
from Spreadsheet.Actions.Saver import Saver
from Spreadsheet.Actions.Loader import Loader
from Spreadsheet.Actions.ShowContent import ShowContent
from SpreadsheetMarkerForStudents.usecasesmarker.reading_spreadsheet_exception import ReadingSpreadsheetException
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException

import os

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

    #verificamos que hay contenido en la celda de la posición idx
    def check_content(new_content: list[str], idx: int):
        try:
            new_content[idx]
        except:
            return False
        return True
                    
    def applyCommand(self, command):
        
        # if command[0] == 'E' and not self.spreadSheet_created: #Edit
        #     raise SpreadSheetException("*** Before EDIT(E) a Spreadsheet, you have to CREATE(C) one. ***")
        # elif command[0] == 'S' and not self.spreadSheet_created: #Save
        #     raise SpreadSheetException("*** Before SAVE(S), you have to CREATE(C) and EDIT(E) a Spreadsheet. ***")
        # # elif command[0] in ['L', 'RF'] and not self.spreadSheet_created: #Load and ReadFile(Mostrar)
        # #     raise SpreadSheetException("*** Before LOAD(L) or READ COMMANDS FILE(RF), you have to CREATE(C) a Spreadsheet. ***")
        
        command_parts = command.split(' ')
        if len(command_parts) == 1:
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
            if command_parts[0] == 'Q':
                print("Exiting the program. Goodbye!")
                exit()
        elif len(command_parts) == 2:
            if command_parts[0] == 'S':  # Save
                self.command_history += 'S, '
                try:
                    if not self.spreadSheet_created:
                        raise SavingSpreadsheetException("Before saving, you have to create and edit a Spreadsheet.")
                    self.saver.run_saver(self.spreadSheet)
                except:
                    raise SavingSpreadsheetException("Spreadsheet can not be save it")

            elif command_parts[0] == 'L':  # Load
                self.command_history += 'L, '
                try:
                    self.loader.run_loader()
                except:
                    raise ReadingSpreadsheetException("Spreadsheet can not be load it")

            elif command_parts[0] == 'RF':  # Read Commands File
                self.command_history += 'RF, '
                try:
                    self.show.printContentSpreadsheet(self.spreadSheet)
                except:
                    raise SpreadSheetException("Spreadsheet can not be save it")
        else: 
            self.command_history += 'E, '
            coord = command_parts[1]
            new_content = command_parts[2]
            idx = 3

            while check_content(command_parts, idx):
                new_content = new_content + ' ' + command_parts[idx]
                idx = idx + 1
            self.edit_cell(coord, new_content)
            print(self.spreadsheet.cells)
            return 0
                

    





            