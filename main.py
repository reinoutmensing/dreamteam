from protein import Protein
import matplotlib.pyplot as plt
import numpy as np
import random
import csv


if __name__ == "__main__":
            
    string = input("Provide amino acid chain:").upper()

    # algoritme
    x_list = [0]
    y_list = [0]
    beginpunt_x = 0
    beginpunt_y = 0
    oorspronkelijkpunt_x = 0
    oorspronkelijkpunt_y = 0
    direction_list = []
    direction_options = [-1, 1, -2, 2]

    for place in string:

        while beginpunt_x in x_list and beginpunt_y in y_list:
            replacement = rep = random.choice(direction_options)
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
        
        x_list.append(beginpunt_x)
        y_list.append(beginpunt_y)
        oorspronkelijkpunt_x = beginpunt_x
        oorspronkelijkpunt_y = beginpunt_y
        direction_list.append(replacement)
    
    direction_list[-1] = 0

    # create a protein object
    protein = Protein(x_list,y_list, string, direction_list)
    print(protein.string, protein.x_list, protein.y_list, protein.direction_list)

    # output csv:
    protein.output()

    # visualisatie
    plt.ylabel('y_waarden')
    plt.xlabel('x_waarden')
   

    colour = []
    for amino in protein.string:
        if amino == 'H':
            colour.append('red')   
        elif amino == 'P':
            colour.append('blue') 
        elif amino == 'C':
            colour.append('green')  
        else:
            colour.append('black')


    for i in range(len(protein.string)):
        plt.scatter(protein.x_list[i], protein.y_list[i], c = colour[i], s = 40, zorder=2)
    
    plt.xticks(np.arange(min(protein.x_list)-5, max(protein.x_list )+6, 1.0))
    plt.yticks(np.arange(min(protein.y_list)-5, max(protein.y_list )+6, 1.0))
    
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha= 1.0, zorder=1)
    plt.rc('axes', axisbelow=True)
    plt.show()