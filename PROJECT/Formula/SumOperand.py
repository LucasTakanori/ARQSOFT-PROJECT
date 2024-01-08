class SumOperand():
    
    def __init__(self, args):
        self.args = args

    def getValue(self):
        operands = [arg.getValue() for arg in self.args]
        sum_value = sum(operands) if operands else 0
        print(f"Sum result: {sum_value}")
        return sum_value