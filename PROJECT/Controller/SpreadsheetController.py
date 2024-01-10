from Controller.UserInterface import UserInterface
from Exceptions.SpreadsheetException import SpreadSheetException

class SpreadSheetController:
    
    def __init__(self):
        self.UI = UserInterface()
        self.spreadSheet = None

    def showMenu(self):
        command = self.UI.main_menu()
        self.applyCommand(command)

    def applyCommand(self, command):
        # hay que guardar en memoria si anteriormente se ha generado el spreadsheet, pq si no no lo puede editar 
        # guardamos una cadena de los comandos que se van ejecutando, ej: "C, E, S, L, ..." 
        # si se quiere Editar(E) y antes se ha Creado(C), se podrá, sino salta error

        print(" Command Selected: ", command)
        
        if command[0] == 'E': #Edit
            if self.spreadSheet == None:
                raise SpreadSheetException("After EDIT(E) a Spreadsheet, you have to CREATE(C) one")
            
            self.spreadSheet.insertContentInCell(cell_id=command[1], content=command[2])
            self.spreadSheet.printMyself()
            
        elif command[0] == 'C': #Create
            if self.spreadSheet != None and self.spreadSheet.getName()==command[1]:
                raise SpreadSheetCommandException("THE NAME OF THE NEW SPREADSHEET IS ALREADY USED")
            self.spreadSheet = SpreadSheet(command[1], self.formulaComputing)
            print("SpreadSheet created")
        