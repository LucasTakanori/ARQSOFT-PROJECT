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

    def applyCommand(self, command):
        # hay que guardar en memoria si anteriormente se ha generado el spreadsheet, pq si no no lo puede editar 
        # guardamos una cadena de los comandos que se van ejecutando, ej: "C, E, S, L, ..." 
        # si se quiere Editar(E) y antes se ha Creado(C), se podrá, sino salta error

        print(" Command Selected: ", command)
        
        if command[0] == 'E' and not self.spreadSheet_created: #Edit
            raise SpreadSheetException("*** Before EDIT(E) a Spreadsheet, you have to CREATE(C) one. ***")
        elif command[0] == 'S' and not self.spreadSheet_created: #Save
            raise SpreadSheetException("*** Before SAVE(S), you have to CREATE(C) and EDIT(E) a Spreadsheet. ***")
        # elif command[0] in ['L', 'RF'] and not self.spreadSheet_created: #Load and ReadFile(Mostrar)
        #     raise SpreadSheetException("*** Before LOAD(L) or READ COMMANDS FILE(RF), you have to CREATE(C) a Spreadsheet. ***")
        
        if command[0] == 'E':  # Edit
            self.command_history += 'E, '
            try:
                self.show.printContent(self.spreadSheet)
                save_after_edit = input("Do you want to save the changes? (y/n): ").lower()
                if save_after_edit == 'y':
                    self.saver.run_saver(self.spreadSheet)
            except:
                raise SpreadSheetException("Spreadsheet can not be edited")
        
        elif command[0] == 'S':  # Save
            self.command_history += 'S, '
            try:
                if not self.spreadSheet_created:
                    raise SavingSpreadsheetException("Before saving, you have to create and edit a Spreadsheet.")
                self.saver.run_saver(self.spreadSheet)
            except:
                raise SavingSpreadsheetException("Spreadsheet can not be save it")

        elif command[0] == 'L':  # Load
            self.command_history += 'L, '
            try:
                self.loader.run_loader()
            except:
                raise ReadingSpreadsheetException("Spreadsheet can not be load it")

        elif command[0] == 'RF':  # Read Commands File
            self.command_history += 'RF, '
            try:
                self.show.printContentSpreadsheet(self.spreadSheet)
            except:
                raise SpreadSheetException("Spreadsheet can not be save it")

        elif command[0] == 'C':  # Create
            self.command_history += 'C, '
            self.spreadSheet_created = True
            new_spreadsheet_name = input("Enter the name for the new spreadsheet: ")

            if new_spreadsheet_name in self.spreadSheets and self.spreadSheet is not None:
                raise SpreadSheetException(f"A spreadsheet with the name '{new_spreadsheet_name}' already exists.")

            directory_path = "/Users/eliacandela/ARQSOFT-LAB/PROJECT/"
            file_path = os.path.join(directory_path, f"{new_spreadsheet_name}.s2v")

            with open(file_path, 'w') as file:
                file.write("")  

            # os.system(f"open {file_path}")
            # new_spreadsheet = Spreadsheet(file_path)
            # self.spreadSheets[file_path] = new_spreadsheet
            print(f"Spreadsheet '{file_path}' created successfully and opened for editing!")
            self.spreadSheet_state = True

        elif command[0] == 'Q':
            print("Exiting the program. Goodbye!")
            exit()





           