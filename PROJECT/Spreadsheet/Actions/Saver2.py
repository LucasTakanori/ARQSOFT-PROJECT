import os
from PROJECT.Spreadsheet.Content.FormulaContent import FormulaContent

class Saver:
    def __init__(self):
        pass

    def retrieve_data_from_spreadsheet(spreadsheet):
        result = {}
        for coord in spreadsheet.cells:
            if isinstance(spreadsheet.cells.get(coord).get_content(), FormulaContent): 
                cell_content = spreadsheet.get_cell_formula_expression(coord)
            else:
                cell_content = spreadsheet.cells.get(coord).get_content().get_value()
            cell_content = str(cell_content).replace(';', ',')    
            result[coord] = cell_content
        return result

    def save_dict_to_s2v(filename, data_dict):
        with open(filename, 'w') as file:
            for coord, cell_value in data_dict.items():
                file.write(f'{cell_value};')
            file.write('\n')

    def save_spreadsheet_to_file(self, filename, spreadsheet):
        data_dict = Saver.retrieve_data_from_spreadsheet(spreadsheet)
        Saver.save_dict_to_s2v(filename, data_dict)
