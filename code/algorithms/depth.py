import numpy as np
import random
from code.classes.protein import Protein
from tqdm import tqdm


direction_options = [-1, 1, -2, 2]
direction_list = []
direction_list.append(0)
protein_list = []
score_list = []
highscore = 0
counter = 0
checker = 0

def depth(step, direction):
    for j in tqdm(range(0, try_number)):
        a = Protein(string, j)
        # create the first string consisting of random
        if j == 0:
            for step in range(1,len(string)):
                direction = random.choice(direction)
                while direction_list[i-1] == (-1 * direction):
                    direction = random.choice(direction_options)

                direction_list.append(direction)
                a.fold_next_amino(i, direction)
                print(a.fold_next_amino)
    
        if checker % 3 == 0:
            binnenchecker = binnerchecker + 1
            pass
        # voor beide 1 en 2 wil je slechts een laatste plek in de lijst teruggaan
        if checker % 3 == 1:

            
        if checker % 3 == 2:
            pass
        
        checker = checker + 1
        a.getscore()
        score = a.score
        score_list.append(score)
        protein_list.append(a)
        if score > highscore:
            highscore = score
            counter = j

        

