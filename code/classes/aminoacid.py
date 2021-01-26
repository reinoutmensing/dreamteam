

class Amino():
    """
    Amino class that contains the acid type and the coordinates of the amino acid. 
    """

    def __init__(self, acid_type):
        self.acid_type = acid_type
        self.x = 0 
        self.y = 0
        self.z = 0
        self.checklist = []

    def __repr__(self):
        return f"{(self.x, self.y, self.z)}"