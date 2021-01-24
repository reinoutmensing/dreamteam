import numpy as np
import random
from code.classes.protein import Protein
from tqdm import tqdm
import copy
import uuid

direction_options = [-1, 1, -2, 2]

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of proteins.
    """
    def __init__(self, string):
        
        self.string = string
        self.proteins = [Protein(string, uuid.uuid4())]
        self.best_solution = None
        self.best_value = - float('inf')


    def get_next_protein(self):
        """
        Returns the next protein from the protein list.
        """
        print('rastagotsoul')
        return self.proteins.pop()

    def build_children(self, protein,amino_position):
        """
        Creates all possible child-proteins.
        """
        # Add a new state of the protein to the list of proteins.
        for direction in direction_options:
            new_protein = copy.deepcopy(protein)
            if new_protein.fold_next_amino(amino_position,direction) == False:
                self.proteins.append(new_protein)

    def check_solution(self, new_protein):
        """
        Checks and updates the highest score.
        """
        new_score = new_protein.getscore()
        old_value = self.best_value

        if new_score >= old_value:
            self.best_solution = new_protein
            self.best_value = new_score


    def run(self):
        """
        Runs the algorithm untill all versions of the protein are created.
        """
        while self.proteins:
            
            print('prot')
            print(self.proteins)
            protein = self.get_next_protein()
            print(self.proteins)
            # Get the next amino acid in the chain.
            amino_position = protein.get_unplaced_amino_position()
            if amino_position is not None:
                self.build_children(protein, amino_position)
            else:
                self.check_solution(protein)

        # Set's the output to be the protein with the highest score.
        protein = self.best_solution

        return protein

        

