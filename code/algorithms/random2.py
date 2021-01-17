import numpy as np
import random
from code.classes.protein import Protein
from tqdm import tqdm


def random_algorithm(string, try_number):
    direction_options = [-1, 1, -2, 2]
    direction_list = []
    direction_list.append(0)
    protein_list = []
    score_list = []
    highscore = 0
    counter = 0

    for j in tqdm(range(0, try_number)):
        a = Protein(string, j)
        for i in range(1, len(string)):
            direction = random.choice(direction_options)
        
            while direction_list[i-1] == (-1 * direction):
                direction = random.choice(direction_options)
            
            direction_list.append(direction)
            a.fold_next_amino(i, direction)  
        a.getscore()
        score = a.score
        score_list.append(score)
        protein_list.append(a)
        if score > highscore:
            highscore = score
            counter = j

    highest_protein = protein_list[counter]       
    return protein_list, score_list, highest_protein