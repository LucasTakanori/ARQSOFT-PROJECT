
class MaxOperand():
    
    def __init__(self, args):
        self.args = args

    def getValue(self):
        operands = [arg.getValue() for arg in self.args]
        max_value = max(operands) if operands else 0
        print(f"Max result: {max_value}")
        return max_value