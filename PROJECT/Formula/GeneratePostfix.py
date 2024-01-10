import re
class GeneratePostfix:
    def __init__(self, tokens):
        self.tokens = tokens
        self.merge_tokens()
        self.output_queue = []
        self.operator_stack = []
        # Update the precedence for ':' and ';'
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.functions = {'SUMA', 'PROMEDIO', 'MAX', 'MIN'}

    def precedence(self, op):
        return self.operators.get(op, 0)

    def merge_tokens(self):
        merged_tokens = []
        i = 0
        while i < len(self.tokens):
            # Case 1: Merge coordinate range
            if i + 2 < len(self.tokens) and self.is_coordinate(self.tokens[i]) and self.tokens[i + 1] == ':' and self.is_coordinate(self.tokens[i + 2]):
                merged_tokens.append(self.tokens[i] + self.tokens[i + 1] + self.tokens[i + 2])
                i += 3  # Skip the next two tokens as they have been merged
            # Case 2: Merge '*/' with '-/+'
            elif i + 1 < len(self.tokens) and self.tokens[i] in ['*', '/'] and self.tokens[i + 1] in ['-', '+']:
                merged_tokens.append(self.tokens[i] + self.tokens[i + 1])
                i += 2  # Skip the next token as it has been merged
            else:
                # If no merging conditions are met, add the token as is
                merged_tokens.append(self.tokens[i])
                i += 1
        self.tokens = merged_tokens

    def generate_postfix(self):
        for token in self.tokens:
            if self.is_number(token) or self.is_coordinate(token) or self.is_range(token): 
                self.output_queue.append(token)
            elif token in self.operators:
                while self.operator_stack and self.operator_stack[-1] != '(' and \
                    self.precedence(self.operator_stack[-1]) >= self.precedence(token):
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.append(token)
            elif token in self.functions:
                self.operator_stack.append(token)
            elif token == ';':
                self.operator_stack.append(token)
            elif token == '(':
                self.operator_stack.append(token)
            elif token == ')':
                while self.operator_stack and self.operator_stack[-1] != '(':
                    self.output_queue.append(self.operator_stack.pop())
                self.operator_stack.pop()  # Pop '(' from stack
                if self.operator_stack and self.operator_stack[-1] in self.functions:
                    self.output_queue.append(self.operator_stack.pop())
            elif token == ';':
                # Pop operators until the top of the stack is another ';'
                # or a function name, then push this ';' onto the stack
                while self.operator_stack and self.operator_stack[-1] not in self.functions:
                    self.output_queue.append(self.operator_stack.pop())
                self.output_queue.append(token)

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
    
    def is_range(self, token):
        # A cell coordinate is defined as one or more uppercase letters followed by one or more digits
        coordinate_pattern = r'[A-Z]+\d+:[A-Z]+\d+'
        return re.match(coordinate_pattern, token) is not None



