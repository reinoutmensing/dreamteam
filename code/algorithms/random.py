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
        self.direction_options = [-1, 1, -2, 2]
        self.protein_list = []
        self.direction_list = []
        self.score_list = []
        self.highscore = 0
        self.counter = 0
        self.best_solution = None

    def run(self):

        for j in tqdm(range(0, self.try_number)):
            a = Protein(copy.deepcopy(self.string), j)

            self.direction_list.append(0)

            for i in range(1, len(self.string)):
                check = True 
                while check :
                    direction = random.choice(self.direction_options)
                    check = a.fold_next_amino(i, direction)
                    
                self.direction_list.append(direction) # output z klopt hierdoor niet
                
            a.getscore()
            score = a.score
            self.score_list.append(score)
            self.protein_list.append(a)
            if score > self.highscore:
                self.highscore = score
                self.counter = j

        self.best_solution = self.protein_list[self.counter] 
        return self.best_solution


        


# def random_algorithm(string, try_number):
#     direction_options = [-1, 1, -2, 2]

#     protein_list = []
#     score_list = []
#     highscore = 0
#     counter = 0

#     for j in tqdm(range(0, try_number)):
#         a = Protein(copy.deepcopy(string), j)

#         direction_list = []
#         direction_list.append(0)

#         for i in range(1, len(string)):
#             check = True 
#             while check :
#                 direction = random.choice(direction_options)

#     #             #dit kan nog in het algemene algorithme staan door de list mee te geven en options
#                 # while direction_list[i-1] == (-1 * direction):
#                 #     direction = random.choice(direction_options)
                
#                 check = a.fold_next_amino(i, direction)
#                 # a.fold_next_amino(i,direction)
    
#             direction_list.append(direction) # output z klopt hierdoor niet
            
        
#         a.getscore()
#         score = a.score
#         score_list.append(score)
#         protein_list.append(a)
#         if score > highscore:
#             highscore = score
#             counter = j

#     highest_protein = protein_list[counter]       
#     return protein_list, score_list, highest_protein

