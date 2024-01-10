import re

class Tokenizer:
    def __init__(self, formula):
        self.formula = formula

    def tokenize(self):
        # Regular expression patterns for different token types
        pattern = {
            'operator': r'\+|-|\*|/',
            'coordinate': r'[A-Z]+\d+',
            'number': r'\d+\.?\d*',
            'opening_round_bracket': r'\(',
            'closing_round_bracket': r'\)',
            'colon': r':',
            'semi_colon': r';',
            'function': r'SUMA|PROMEDIO|MAX|MIN',  # Additional functions can be added as necessary
            'range': r'[A-Z]+\d+:[A-Z]+\d+'  # For example, A1:B3
        }

        # Combine the patterns into a single regular expression
        combined_pattern = '|'.join(f'({p})' for p in pattern.values())
        
        # Find all matches of the pattern in the formula
        tokens = re.findall(combined_pattern, self.formula)
        
        # Flatten the list of tuples and filter out empty strings
        tokens = [token for token in sum(tokens, ()) if token != '']

        return tokens