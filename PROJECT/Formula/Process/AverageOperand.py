class AverageOperand:

    def __init__(self, args):
        self.args = args

    def getValue(self):
        operands = [arg.getValue() for arg in self.args]
        average_value = sum(operands) / len(operands) if operands else 0
        print(f"Average  result: {average_value}")
        return average_value