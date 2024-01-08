import tkinter as tk
from tkinter import messagebox
from PROJECT.Spreadsheet.Content.TextContent import TextContent
from Spreadsheet.Content.NumberContent import NumberContent
from Spreadsheet.Content.FormulaContent import FormulaContent
from PROJECT.Formula.FormulaEvaluator import FormulaEvaluator
from Spreadsheet import Spreadsheet

class SpreadsheetUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Spreadsheet UI")

        self.spreadsheet = Spreadsheet(rows=5, cols=5)

        self.create_widgets()

    def create_widgets(self):
        self.cells = [[None for _ in range(self.spreadsheet.cols)] for _ in range(self.spreadsheet.rows)]

        for i in range(self.spreadsheet.rows):
            for j in range(self.spreadsheet.cols):
                cell_frame = tk.Frame(self.root, borderwidth=1, relief="solid")
                cell_frame.grid(row=i, column=j, padx=5, pady=5)

                cell_content = tk.Entry(cell_frame, width=15)
                cell_content.grid(row=0, column=0)

                set_button = tk.Button(cell_frame, text="Set", command=lambda i=i, j=j: self.set_cell_value(i, j, cell_content.get()))
                set_button.grid(row=0, column=1)

                self.cells[i][j] = cell_content

        calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_spreadsheet)
        calculate_button.grid(row=self.spreadsheet.rows, columnspan=self.spreadsheet.cols, pady=10)

    def set_cell_value(self, row, col, content):
        try:
            if "=" in content:
                self.spreadsheet.set_cell(row, col, "formula", FormulaContent(content[1:]))
            elif content.isdigit():
                self.spreadsheet.set_cell(row, col, "number", NumberContent(float(content)))
            else:
                self.spreadsheet.set_cell(row, col, "text", TextContent(content))

            messagebox.showinfo("Success", f"Cell ({row}, {col}) set successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error setting cell ({row}, {col}): {e}")

    def calculate_spreadsheet(self):
        for i in range(self.spreadsheet.rows):
            for j in range(self.spreadsheet.cols):
                cell_content = self.cells[i][j].get()
                self.set_cell_value(i, j, cell_content)

        for i in range(self.spreadsheet.rows):
            for j in range(self.spreadsheet.cols):
                cell_content = self.spreadsheet.get_cell_content(i, j)
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, cell_content)


if __name__ == "__main__":
    root = tk.Tk()
    app = SpreadsheetUI(root)
    root.mainloop()
