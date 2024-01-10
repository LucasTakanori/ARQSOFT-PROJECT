import re
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.function_stack = []  # Stack to track function context

    def next_token(self):
        if self.current_index < len(self.tokens):
            token = self.tokens[self.current_index]
            self.current_index += 1
            return token
        else:
            return None

    def parse(self):
        if not self.tokens:
            raise ValueError("No tokens to parse")

        last_token_type = None
        parenthesis_count = 0
        expecting_range = False  # Flag to track if a colon for a range is expected

        while self.current_index < len(self.tokens):
            token = self.next_token()
            #print('current',token)
            #print('last',last_token_type)
            if self.is_function(token):
                if last_token_type in ['operand', 'closing_round_bracket']:
                    raise SyntaxError("Function name cannot follow an operand or closing bracket directly")
                self.function_stack.append(token)
                last_token_type = 'function'
            elif self.is_coordinate(token):
                # Handle cell coordinates
                if last_token_type == 'operand' and not expecting_range:
                    raise SyntaxError("Two consecutive operands")
                last_token_type = 'operand'
                expecting_range = True  # After a coordinate, a colon for range is valid
            elif token == ';':
                # Handle semicolon as function argument separator
                if not self.function_stack or last_token_type in ['Infix operator', 'Prefix operator', 'opening_round_bracket', ';']:
                    raise SyntaxError("Invalid use of ';' as argument separator")
                last_token_type = ';'
            elif self.is_number(token):
                # Handle numbers (including decimals)
                if last_token_type in ['operand', 'closing_round_bracket']:
                    raise SyntaxError("Invalid syntax: number follows an operand or closing bracket without an operator")
                last_token_type = 'operand'
                expecting_range = False
            elif token == ':':
                # Handle colon for cell ranges
                if not expecting_range or last_token_type != 'operand':
                    raise SyntaxError("Invalid use of ':' for cell range")
                last_token_type = 'range'
                expecting_range = False  # Reset the flag as colon is consumed
            elif token in '*/':
                if last_token_type in [None, 'Infix operator','Prefix operator', '(']:
                    raise SyntaxError("Operator in invalid position")
                last_token_type = 'Infix operator'
            elif token in '+-':
                if last_token_type not in [None, 'operand', '(',')','Infix operator']:
                    raise SyntaxError("Operator in invalid position")
                last_token_type = 'Prefix operator'
            elif token == '(':
                parenthesis_count += 1
                if last_token_type in ['operand', 'closing_round_bracket']:
                    raise SyntaxError("Operand or closing bracket followed directly by '('")
                last_token_type = '('
            elif token == ')':
                parenthesis_count -= 1
                if last_token_type in ['Infix operator', 'Prefix operator', '(']:
                    raise SyntaxError("')' cannot follow an operator or '('")
                last_token_type = ')'
                if self.function_stack:
                    self.function_stack.pop()
            else:
                raise SyntaxError(f"Unknown token: {token}")

            if parenthesis_count < 0:
                raise SyntaxError("Unbalanced parentheses")

        if parenthesis_count != 0:
            raise SyntaxError("Unbalanced parentheses")

        return self.tokens


    def is_coordinate(self, token):
        # A cell coordinate is defined as one or more uppercase letters followed by one or more digits
        coordinate_pattern = r'^[A-Z]+\d+$'
        #print(re.match(coordinate_pattern, token) is not None)
        return re.match(coordinate_pattern, token) is not None

    def is_function(self, token):
        # List of valid function names
        valid_functions = ["SUMA", "PROMEDIO", "MAX", "MIN"]
        return token in valid_functions
    
    def is_number(self, token):
        number_pattern = r'^\d+\.?\d*$'
        return re.match(number_pattern, token) is not None
