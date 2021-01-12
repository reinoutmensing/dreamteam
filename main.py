from code.classes.protein import Protein
from code.algorithms.random import random_directionlist
import matplotlib.pyplot as plt
import numpy as np
import random
import csv


if __name__ == "__main__":

    score_list = []
    best_score = 0
            
    string = input("Provide amino acid chain:").upper()

    # algoritme
    for i in range (0,10):
        random = random_directionlist(string)
        
        


        # create a protein object
        direction_list = random[0]
        x_list = random[1]
        y_list = random[2]
        protein = Protein(x_list,y_list, string, direction_list)
        # print(protein.string, protein.x_list, protein.y_list, protein.direction_list)

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
        print("frots")
        score = protein.score()
        print("-------------i")
        print(i)
        print(score)
        score_list.append(score)
        print("afterscore")
        if score >= best_score:
            best_score = score
            best_string = protein.string
            best_colour = colour
            best_x_list = x_list
            best_y_list = y_list
    print("penisdenis")
    print(score_list)
    
    for i in range(len(protein.string)):
        plt.scatter(best_x_list[i], best_y_list[i], c = colour[i], s = 40, zorder=3)
    
    


    plt.xticks(np.arange(min(best_x_list)-5, max(best_x_list )+6, 1.0))
    plt.yticks(np.arange(min(best_y_list)-5, max(best_y_list )+6, 1.0))
    plt.ylabel('y_waarden')
    plt.xlabel('x_waarden')
    plt.plot(best_x_list, best_y_list, '-', zorder= 2)
    plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha= 1.0, zorder=1)
    plt.rc('axes', axisbelow=True)
    plt.show()
        
        




    # for i in range(len(protein.string)):
    #     plt.scatter(protein.x_list[i], protein.y_list[i], c = colour[i], s = 40, zorder=3)
    
    


    # plt.xticks(np.arange(min(protein.x_list)-5, max(protein.x_list )+6, 1.0))
    # plt.yticks(np.arange(min(protein.y_list)-5, max(protein.y_list )+6, 1.0))
    # plt.ylabel('y_waarden')
    # plt.xlabel('x_waarden')
    # plt.plot(protein.x_list, protein.y_list, '-', zorder= 2)
    # plt.grid(b=True, which='major', color='#666666', linestyle='-', alpha= 1.0, zorder=1)
    # plt.rc('axes', axisbelow=True)
    # plt.show()

# for j in range(len(x_punt)):
    #     if j % 2 != 0:
    #         plt.plot(x_punt[j], y_punt[j],'b-')
        # counter = counter + 1

    