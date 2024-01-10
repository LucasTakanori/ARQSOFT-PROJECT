
import os
from SpreadsheetMarkerForStudents.usecasesmarker.saving_spreadsheet_exception import SavingSpreadsheetException
from tkinter import filedialog, messagebox
from Spreadsheet.Cell import Cell

class Saver:
    def __init__(self):
        pass

    def promptForFileName(self, file_extension):
        file_name = filedialog.asksaveasfilename(initialfile='Untitled', defaultextension=file_extension,
                                                  filetypes=[("Text Files", "*.txt"), ("S2V Files", "*.s2v")])
        if file_name:
            return file_name
        else:
            return None

    def validateFileName(self, fileName):
        if not os.path.splitext(fileName)[0]:
            raise SavingSpreadsheetException("Invalid file name.")

    def promptForDirectory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            return directory_path
        else:
            return None

    def validateDirectory(self, directoryPath):
        if not os.path.exists(directoryPath):
            raise SavingSpreadsheetException("Invalid directory path.")

    def saveSpreadsheetData(self, fileName, directoryPath, spreadsheetData):
        try:
            with open(os.path.join(directoryPath, fileName), 'w') as file:
                for row in spreadsheetData:
                    file.write(';'.join(map(str, row)) + '\n')
        except Exception as e:
            raise SavingSpreadsheetException(str(e))

    def displaySaveConfirmation(self):
        messagebox.showinfo("Success", "File saved successfully.")

    def run_saver(self, spreadsheet):
        file_extension = ".s2v" 
        file_name = self.promptForFileName(file_extension)
        directory_path = self.promptForDirectory()
        coord = sorted(set(coord for coord in spreadsheet.cells.keys()))
        max_row = max(int(coord[1:]) for coord in coord)

        #lista de letras de A a Z
        letras = [chr(letra) for letra in range(ord(coord[0][0]), ord(coord[-1][0]) + 1)]

        spreadsheet_data = []
        spreadsheet_data = [
            [
                str(spreadsheet.cells.get(f"{col}{row}", Cell()).content.getValue()).replace(";", ",") + ";"
                for col in letras
            ]
            for row in range(1, max_row + 1)
        ]

        if file_name and directory_path:
            try:
                self.validateFileName(file_name)
                self.validateDirectory(directory_path)
                self.saveSpreadsheetData(file_name, directory_path, spreadsheet_data)
                self.displaySaveConfirmation()
            except SavingSpreadsheetException as e:
                messagebox.showerror("Error", str(e))



# from tkinter import *
# from tkinter.filedialog import asksaveasfile
# from tkinter import messagebox

# class Saver:
#    def __init__(self):
#        self.win = Tk()
#        self.win.geometry("750x250")

#    def promptForFileName(self):
#        f = asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
#        if f is None:
#            return None
#        else:
#            return f.name

#    def validateFileName(self, fileName):
#        if not os.path.splitext(fileName)[0]:
#            raise InvalidFileNameException("Invalid file name.")

#    def promptForDirectory(self):
#        d = asksaveasfile(initialfile = '', defaultextension="", filetypes=[("All Files","*.*")])
#        if d is None:
#            return None
#        else:
#            return d.name

#    def validateDirectory(self, directoryPath):
#        if not os.path.exists(directoryPath):
#            raise InvalidDirectoryException("Invalid directory path.")

#    def saveSpreadsheetData(self, fileName, directoryPath, spreadsheetData):
#        try:
#            with open(os.path.join(directoryPath, fileName), 'w', newline='') as file:
#                writer = csv.writer(file)
#                writer.writerows(spreadsheetData)
#        except Exception as e:
#            raise SaveOperationException(str(e))

#    def displaySaveConfirmation(self):
#        messagebox.showinfo("Success", "File saved successfully.")

