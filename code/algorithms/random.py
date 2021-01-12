import numpy as np
import random

def random_directionlist(string):
    x_list = [0]
    y_list = [0]
    beginpunt_x = 0
    beginpunt_y = 0
    oorspronkelijkpunt_x = 0
    oorspronkelijkpunt_y = 0
    direction_list = []
    direction_options = [-1, 1, -2, 2]

    for place in string:
        check = True

        while check == True: 
            counter = 0
            replacement = random.choice(direction_options)
            beginpunt_x = oorspronkelijkpunt_x
            beginpunt_y = oorspronkelijkpunt_y
            
            # verplaatsing in de x-richting
            if replacement == 1:
                beginpunt_x = beginpunt_x + 1
            
            if replacement == 2:
                beginpunt_y = beginpunt_y + 1
            
            if replacement == -1:
                beginpunt_x = beginpunt_x - 1
            
            if replacement == -2:
                beginpunt_y = beginpunt_y - 1

            for i in range (0, len(x_list)):
                if beginpunt_y != y_list[i]  or beginpunt_x != x_list[i] :
                    counter = counter + 1    
            if counter == len(x_list):
                check = False
        
        x_list.append(beginpunt_x)
        y_list.append(beginpunt_y)
        oorspronkelijkpunt_x = beginpunt_x
        oorspronkelijkpunt_y = beginpunt_y
        direction_list.append(replacement) 
    direction_list[-1] = 0
        
    return direction_list, x_list, y_list