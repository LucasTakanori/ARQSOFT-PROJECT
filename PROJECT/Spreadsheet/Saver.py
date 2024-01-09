
import os
import csv

class InvalidFileNameException(Exception):
    pass

class InvalidDirectoryException(Exception):
    pass

class SaveOperationException(Exception):
    pass

class Saver:
    def __init__(self):
        pass

    def validateFileName(self, fileName):
        if not os.path.splitext(fileName)[0]:
            raise InvalidFileNameException("Invalid file name.")

    def validateDirectory(self, directoryPath):
        if not os.path.exists(directoryPath):
            raise InvalidDirectoryException("Invalid directory path.")

    def saveSpreadsheetData(self, fileName, directoryPath, spreadsheetData):
        try:
            with open(os.path.join(directoryPath, fileName), 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(spreadsheetData)
        except Exception as e:
            raise SaveOperationException(str(e))

    def displaySaveConfirmation(self):
        print("File saved successfully.")

    def run(self, fileName, directoryPath, spreadsheetData):
        self.validateFileName(fileName)
        self.validateDirectory(directoryPath)
        self.saveSpreadsheetData(fileName, directoryPath, spreadsheetData)
        self.displaySaveConfirmation()


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

