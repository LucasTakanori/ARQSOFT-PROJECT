class Min():
    
    def __init__(self, args):
        self.args = args
        
    def calculate_min(self):
        try:
            return min(self.args)
        except:
            return 0
    