from Formula.Parser import Parser
from Formula.GeneratePostfix import GeneratePostfix
from Formula.Process.Max import Max
from Formula.Process.Min import Min
from Formula.Process.Promedio import Promedio
from Formula.Tokenizer import Tokenizer
from Formula.Process.Suma import  Suma

# from PROJECT.Formula.Parser import Parser
# from PROJECT.Formula.GeneratePostfix import GeneratePostfix
# from PROJECT.Formula.Process.Max import Max
# from PROJECT.Formula.Process.Min import Min
# from PROJECT.Formula.Process.Promedio import Promedio
# from PROJECT.Formula.Tokenizer import Tokenizer
# from PROJECT.Formula.Process.Suma import  Suma


import re

class EvaluatePostfix:
    def __init__(self, formula):
        self.formula = formula
        self.postfix_expression = self.generate_postfix()

    def generate_postfix(self):
        tokenizer = Tokenizer(self.formula)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        tokens = parser.parse()
        postfix_generator = GeneratePostfix(tokens)
        postfix_expression = postfix_generator.generate_postfix()
        #print(postfix_expression)
        return postfix_expression

    def evaluate(self, Spreadsheet):
        stack = []
        function_args = []  # To accumulate arguments for functions
        in_function = False

        for token in self.postfix_expression:
            #print('token',token)
            if self.is_number(token):
                stack.append(float(token))
            elif self.is_coordinate(token):
                #print(token)
                stack.append(self.get_value_from_coordinate(token,Spreadsheet))
            elif self.is_range(token):
                value = Spreadsheet.get_values_from_range(token)
                #print('range cells values', value)
                stack.append(value)
            elif token in ['+', '-', '*', '/','*-', '/-', '*+', '/+']:
                if len(stack) < 2:
                    raise ValueError("Insufficient operands for operator")
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.apply_operator(operand1, operand2, token)
                stack.append(result)
            elif token in ['SUMA', 'PROMEDIO', 'MAX', 'MIN']:
                # Ensure there's at least one argument for the function
                if not function_args: 
                    result=self.apply_function(stack.pop(), token)
                else:
                    result = self.apply_function(function_args, token)
                stack.append(result)
                function_args = []  # Clear arguments after processing
                in_function = False
            elif token == ';':
                if in_function==False:
                    function_args.append(stack.pop())
                    function_args.append(stack.pop())
                    in_function=True
                else:
                    function_args.append(stack.pop())
            else:
                raise ValueError(f"Unrecognized token: {token}")
            #print('stack',stack)
            #print('function args', function_args)
        if len(stack) != 1:
            #print(stack)
            raise ValueError("Invalid Postfix Expression")
        
        return stack.pop()

    def apply_function(self, function_args, function):
        function_args = [item for sublist in function_args for item in (sublist if isinstance(sublist, list) else [sublist])]

        if function == 'SUMA':
            return Suma(function_args).calculate_suma()
        elif function == 'PROMEDIO':
            return Promedio(function_args).calculate_promedio()
        elif function == 'MAX':
            return Max(function_args).calculate_max()
        elif function == 'MIN':
            return Min(function_args).calculate_min()
        else:
            raise ValueError(f"Unrecognized function: {function}")



    def is_number(self, token):
        try:
            float(token)
            return True
        except ValueError:
            return False

    def is_coordinate(self, token):
        return re.match(r'^[A-Z]+\d+$', token) is not None

    def get_value_from_coordinate(self, coordinate, Spreadsheet):
        # Placeholder for getting value from a coordinate like 'A4'
        cell = Spreadsheet.get(coordinate)
        return cell.get_content().get_value()
        

    def apply_operator(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*' or operator == '*+':
            return operand1 * operand2
        elif operator == '/' or operator == '/+':
            return operand1 / operand2
        elif operator == '*-':
            return operand1 * -operand2
        elif operator == '/-':
            return operand1 / -operand2
        else:
            raise ValueError(f"Unrecognized operator: {operator}")

    
    def is_range(self, token):
        # A cell coordinate is defined as one or more uppercase letters followed by one or more digits
        coordinate_pattern = r'[A-Z]+\d+:[A-Z]+\d+'
        return re.match(coordinate_pattern, token) is not None
    

