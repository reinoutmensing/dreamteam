

class Amino():

    def __init__(self, acid_type):
        self.acid_type = acid_type
        self.x = 0 
        self.y = 0

    
    def __repr__(self):
        return f"{self.acid_type, (self.x, self.y)}"