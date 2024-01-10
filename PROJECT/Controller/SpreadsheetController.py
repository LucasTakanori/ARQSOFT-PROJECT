# class SpreadSheetController:
    
#     def __init__(self):
#         self.UI = UserInterface()
#         self.spreadsheets = {}  # Cambiado de 'self.spreadSheet' a 'self.spreadsheets'
#         self.command_history = ""  # Cadena que almacena los comandos ejecutados
#         self.spreadSheet_state = False  # Flag para verificar si se ha creado el spreadsheet correspondiente

#     def showMenu(self):
#         command = self.UI.main_menu()
#         self.applyCommand(command)

#     def applyCommand(self, command):
#         # hay que guardar en memoria si anteriormente se ha generado el spreadsheet, pq si no no lo puede editar 
#         # guardamos una cadena de los comandos que se van ejecutando, ej: "C, E, S, L, ..." 
#         # si se quiere Editar(E) y antes se ha Creado(C), se podrá, sino salta error

#         print(" Command Selected: ", command)
        
#         if command[0] == 'E' and not self.spreadSheet_state:  # Edit
#             raise SpreadSheetException("After EDIT(E) a Spreadsheet, you have to CREATE(C) one")
#         elif command[0] == 'S' and not self.spreadSheet_state:  # Save
#             raise SpreadSheetException("Before SAVE(S), you have to CREATE(C) and EDIT(E) a Spreadsheet.")
#         elif command[0] in ['L', 'RF'] and not self.spreadSheet_state:  # Load and ReadFile(Mostrar)
#             raise SpreadSheetException("Before LOAD(L) or READ COMMANDS FILE(RF), you have to CREATE(C) a Spreadsheet.")
        
#         if command[0] == 'E':  # Edit
#             self.command_history += 'E, '
#             # Lógica para la acción de editar

#         elif command[0] == 'S':  # Save
#             self.command_history += 'S, '
#             # Lógica para la acción de guardar

#         elif command[0] == 'L':  # Load
#             self.command_history += 'L, '
#             # Lógica para la acción de cargar

#         elif command[0] == 'RF':  # Read Commands File
#             self.command_history += 'RF, '
#             # Lógica para la acción de leer comandos desde un archivo

#         elif command[0] == 'C':  # Create
#             self.command_history += 'C, '
#             new_spreadsheet_name = self.UI.get_new_spreadsheet_name()
            
#             # Verificar si ya existe un spreadsheet con el mismo nombre
#             if new_spreadsheet_name in self.spreadsheets:
#                 raise SpreadSheetException(f"A spreadsheet with the name '{new_spreadsheet_name}' already exists.")
            
#             # Crear una nueva instancia de la clase Spreadsheet y agregarla al diccionario de spreadsheets
#             new_spreadsheet = Spreadsheet(new_spreadsheet_name)
#             self.spreadsheets[new_spreadsheet_name] = new_spreadsheet
#             print(f"Spreadsheet '{new_spreadsheet_name}' created successfully! ")

from Controller.UserInterface import UserInterface
from collections import OrderedDict
from Exceptions.SpreadsheetException import SpreadSheetException
from Spreadsheet import Spreadsheet
from Spreadsheet.Actions.Saver import Saver

class SpreadSheetController:
    
    def __init__(self):
        self.UI = UserInterface()
        self.spreadSheet = None
        self.command_history = " " #Cadena que almacena los comandos ejecutados 
        self.spreadSheet_created = False #Flag para verificar si se ha creado el spreadsheet correspondiente 
        self.spreadSheets = {}

    def showMenu(self):
        command = self.UI.main_menu()
        self.applyCommand(command)

    def applyCommand(self, command):
        # hay que guardar en memoria si anteriormente se ha generado el spreadsheet, pq si no no lo puede editar 
        # guardamos una cadena de los comandos que se van ejecutando, ej: "C, E, S, L, ..." 
        # si se quiere Editar(E) y antes se ha Creado(C), se podrá, sino salta error

        print(" Command Selected: ", command)
        
        if command[0] == 'E' and not self.spreadSheet_created: #Edit
            raise SpreadSheetException("After EDIT(E) a Spreadsheet, you have to CREATE(C) one")
        elif command[0] == 'S' and not self.spreadSheet_created: #Save
            raise SpreadSheetException("Before SAVE(S), you have to CREATE(C) and EDIT(E) a Spreadsheet.")
        elif command[0] in ['L', 'RF'] and not self.spreadSheet_created: #Load and ReadFile(Mostrar)
            raise SpreadSheetException("Before LOAD(L) or READ COMMANDS FILE(RF), you have to CREATE(C) a Spreadsheet.")
        
        if command[0] == 'E':  # Edit
            self.command_history += 'E, '
            # Lógica para la acción de editar

        elif command[0] == 'S':  # Save
            self.command_history += 'S, '
            try:
                self.saver.run_saver(self.spreadSheet, )
            except:
                raise SpreadSheetException("Spreadsheet can not be save it")

        elif command[0] == 'L':  # Load
            self.command_history += 'L, '
            # Lógica para la acción de cargar

        elif command[0] == 'RF':  # Read Commands File
            self.command_history += 'RF, '
            # Lógica para la acción de leer comandos desde un archivo

        elif command[0] == 'C':  # Create
            self.command_history += 'C, '
            self.spreadSheet_state = True
            new_spreadsheet_name = input("Enter the name for the new spreadsheet: ")
            
            # Verificar si ya existe un spreadsheet con el mismo nombre
            if new_spreadsheet_name in self.spreadSheets:
                raise SpreadSheetException(f"A spreadsheet with the name '{new_spreadsheet_name}' already exists.")
            
            # Crear una nueva instancia de la clase Spreadsheet y agregarla al diccionario de spreadsheets
            new_spreadsheet = Spreadsheet(new_spreadsheet_name)
            self.spreadSheets[new_spreadsheet_name] = new_spreadsheet
            print(f"Spreadsheet '{new_spreadsheet_name}' created successfully! ")