class MinOperand():
    
    def __init__(self, args):
        self.args = args

    def getValue(self):
        operands = [arg.getValue() for arg in self.args]
        sum_value = min(operands) if operands else 0
        print(f"Min result: {sum_value}")
        return sum_value