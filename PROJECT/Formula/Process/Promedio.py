class Promedio():
    
    def __init__(self, args):
        self.args = args
        
    def calculate_promedio(self):
        return sum(self.args) / len(self.args)
