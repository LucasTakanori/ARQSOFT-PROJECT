from Controller.UserInterface import UserInterface

class SpreadSheetController:
    
    def __init__(self):
        self.UI = UserInterface()
        self.spreadSheet = None

    def showMenu(self):
        command = self.UI.main_menu()
        self.applyCommand(command)

    def applyCommand(self, command):
        """
        The function `applyCommand` takes a command as input and performs different actions based on the
        command type.
        
        :param command: The `command` parameter is a string that represents a command to be executed. It is
        split into a list of words using the space character as the delimiter. The first word in the list
        (`co[0]`) represents the type of command to be executed. The remaining words in the list are the 
        contents to process`
        """
        print(command)
        
        if command[0] == 'E': #Edit
            if self.spreadSheet == None:
                raise SpreadSheetCommandException("YOU ARE TRYING TO EDIT A CELL BEFORE CREATING A SPREADSHEET")
            
            self.spreadSheet.insertContentInCell(cell_id=command[1], content=command[2])  ##LE PASO DIRECTO STRING CELL & CONTENT (A4 4.4) NÓTESE QUE EN ESTE PUNTO LA ASEGURO QUE LA SINTAXI ES CORRECTA
            self.spreadSheet.printMyself()
            
        elif command[0] == 'C': #Create
            if self.spreadSheet != None and self.spreadSheet.getName()==command[1]:
                raise SpreadSheetCommandException("THE NAME OF THE NEW SPREADSHEET IS ALREADY USED")
            self.spreadSheet = SpreadSheet(command[1], self.formulaComputing)
            print("SpreadSheet created")
        