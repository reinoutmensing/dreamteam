import numpy as np
import random
from code.classes.protein import Protein
from tqdm import tqdm
import copy
import uuid

class RandomAlgorithm:

    def __init__(self, string, try_number):
        self.try_number = try_number
        self.string = string
        self.direction_options = [-1, 1, -2, 2, -3, 3]
        self.protein_list = []
        self.score_list = []
        self.highscore = 0
        self.counter = 0
        self.best_solution = None

    def run(self):

        for j in tqdm(range(0, self.try_number)):
            a = Protein(copy.deepcopy(self.string), j)

            for i in range(1, len(self.string)):
                check = True 
                while check :
                    direction = random.choice(self.direction_options)
                    check = a.fold_next_amino(i, direction)
                     
            a.getscore()
            score = a.score
            self.score_list.append(score)
            self.protein_list.append(a)
            if score > self.highscore:
                self.highscore = score
                self.counter = j

        self.best_solution = self.protein_list[self.counter] 
        return self.best_solution



