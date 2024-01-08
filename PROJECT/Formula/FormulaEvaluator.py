import re

class FormulaEvaluator:
    @staticmethod
    def evaluate_max_operand(formula):
        operands = [float(operand) for operand in re.findall(r'\b\d+\b', formula)]
        return max(operands) if operands else 0

    @staticmethod
    def evaluate_min_operand(formula):
        operands = [float(operand) for operand in re.findall(r'\b\d+\b', formula)]
        return min(operands) if operands else 0