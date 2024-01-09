import re
class GeneratePostfix:
    def __init__(self, tokens):
        self.tokens = tokens
        self.output_queue = []
        self.operator_stack = []
        # Update the precedence for ':' and ';'
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2, ':': 10, ';': 1}
        self.functions = {'SUMA', 'PROMEDIO', 'MAX', 'MIN'}

    def precedence(self, op):
        return self.operators.get(op, 0)

    def generate_postfix(self):
        for token in self.tokens:
            if self.is_number(token) or self.is_coordinate(token):
                self.output_queue.append(token)
            elif token in self.operators:
                while self.operator_stack and self.operator_stack[-1] != '(' and \
                      self.precedence(self.operator_stack[-1]) >= self.precedence(token):
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.append(token)
            elif token in self.functions:
                self.operator_stack.append(token)
            elif token == '(':
                self.operator_stack.append(token)
            elif token == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.pop()  # Pop '(' from stack
                if self.operator_stack and self.operator_stack[-1] in self.functions:
                    self.output_queue.append(self.operator_stack.pop())

        while self.operator_stack:
            self.output_queue.append(self.operator_stack.pop())

        return self.output_queue

    def is_coordinate(self, token):
        # A cell coordinate is defined as one or more uppercase letters followed by one or more digits
        coordinate_pattern = r'^[A-Z]+\d+$'
        #print(re.match(coordinate_pattern, token) is not None)
        return re.match(coordinate_pattern, token) is not None
    
    def is_number(self, token):
        number_pattern = r'^\d+\.?\d*$'
        return re.match(number_pattern, token) is not None