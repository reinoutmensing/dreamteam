from protein import Protein
import matplotlib.pyplot as plt
import random
import csv


if __name__ == "__main__":
            
    string = input("Provide amino acid chain:")

    # algoritme
    x_list = [0]
    y_list = [0]
    beginpunt_x = 0
    beginpunt_y = 0
    oorspronkelijkpunt_x = 0
    oorspronkelijkpunt_y = 0
    direction_list = []
    for place in string:

        while beginpunt_x in x_list and beginpunt_y in y_list:
            replacement = round(4 * random.random())
            beginpunt_x = oorspronkelijkpunt_x
            beginpunt_y = oorspronkelijkpunt_y
            
            # verplaatsing in de x-richting
            if replacement == 1:
                beginpunt_x = beginpunt_x + 1
            
            if replacement == 2:
                beginpunt_y = beginpunt_y + 1
            
            if replacement == 3:
                beginpunt_x = beginpunt_x - 1
            
            if replacement == 4:
                beginpunt_y = beginpunt_y - 1
        
        x_list.append(beginpunt_x)
        y_list.append(beginpunt_y)
        oorspronkelijkpunt_x = beginpunt_x
        oorspronkelijkpunt_y = beginpunt_y
        direction_list.append(replacement)

    # create a protein object
    protein = Protein(x_list,y_list, string, direction_list)
    print(protein.string, protein.x_list, protein.y_list, protein.direction_list)

    # output csv:
    protein.output()

    # visualisatie
    plt.ylabel('y_waarden')
    plt.xlabel('x_waarden')
    plt.xlim(-15,15)
    plt.ylim(-15,15)

    colour = []
    for amino in protein.string:
        if amino == 'H':
            colour.append('blue')   
        elif amino == 'P':
            colour.append('red')   

    for i in range(len(protein.string)):
        plt.scatter(protein.x_list[i], protein.y_list[i], c = colour[i], s = 20)

    plt.show()