from .depth import DepthFirst


class BreadthFirst(DepthFirst):
    

    def get_next_protein(self):
        
        return self.proteins.pop(0)