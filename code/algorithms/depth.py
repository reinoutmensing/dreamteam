import numpy as np
import random
from code.classes.protein import Protein
from tqdm import tqdm
import copy
import uuid

direction_options = [-1, 1, -2, 2]

class DepthFirst:
    """
    A Depth First algorithm that builds a stack of graphs with a unique assignment of nodes for each instance.
    """
    def __init__(self, string):
        
        self.string = string
        self.states = [Protein(string, uuid.uuid4())]
        self.best_solution = None
        self.best_value = - float('inf')


    def get_next_state(self):
        """
        Method that gets the next state from the list of states.
        """
        return self.states.pop()

    def build_children(self, protein,amino_position):
        """
        Creates all possible child-states and adds them to the list of states.
        """
    

        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        for direction in direction_options:
            new_protein = copy.deepcopy(protein)
            if new_protein.fold_next_amino(amino_position,direction) == False:
                self.states.append(new_protein)

    def check_solution(self, new_protein):
        """
        Checks and accepts better solutions than the current solution.
        """

        new_score = new_protein.getscore()
        old_value = self.best_value

        # 
        if new_score >= old_value:
            self.best_solution = new_protein
            self.best_value = new_score
            print(f"New best value: {self.best_value}")
            # new_protein.plot()

    def run(self):
        """
        Runs the algorithm untill all possible states are visited.
        """
        while self.states:
            
            protein = self.get_next_state()

            # Retrieve the next empty node.
            amino_position = protein.get_unplaced_amino_position()
            if amino_position is not None:
                self.build_children(protein, amino_position)
            else:
                
                # Stop if we find a solution
                # break

                # or ontinue looking for better graph
                self.check_solution(protein)

        # Update the input graph with the best result found.
        self.protein = self.best_solution

        

