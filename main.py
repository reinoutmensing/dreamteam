from code.classes.protein import Protein
from code.algorithms.random import random_directionlist
import matplotlib.pyplot as plt
import numpy as np
import random
import csv


if __name__ == "__main__":
            
    string = input("Provide amino acid chain:").upper()

    # algoritme
    random = random_directionlist(string)

    # create a protein object
    direction_list = random[0]
    x_list = random[1]
    y_list = random[2]
    protein = Protein(x_list,y_list, string, direction_list)
    print(protein.string, protein.x_list, protein.y_list, protein.direction_list)

    # output csv:
    protein.output()

    # visualisatie
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
        plt.scatter(protein.x_list[i], protein.y_list[i], c = colour[i], s = 40, zorder=3)
    
    plt.xticks(np.arange(min(protein.x_list)-5, max(protein.x_list )+6, 1.0))
    plt.yticks(np.arange(min(protein.y_list)-5, max(protein.y_list )+6, 1.0))
    plt.ylabel('y_waarden')
    plt.xlabel('x_waarden')
    plt.plot(protein.x_list, protein.y_list, '-', zorder= 2)
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha= 1.0, zorder=1)
    plt.rc('axes', axisbelow=True)
    plt.show()