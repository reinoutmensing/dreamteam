import csv 
from code.classes.aminoacid import Amino
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

class Protein():
    
    def __init__(self, string, id):
        self.id = id
        self.string = string
        self.score = 0 
        self.aminochain = []
        self.direction_list = []
        self.make_protein()
        self.aminocoordinates = []
        self.aminocoordinates.append((self.aminochain[0].x, self.aminochain[0].y))
        self.collision = False

    def __repr__(self):
        """
        Returns a representation of the protein.
        """
        return f"{self.string}, {self.score}"
        

    def make_protein(self):
        """
        Initiates the protein structure from the provided string.
        """
        for c in self.string:
            a = Amino(c)
            self.aminochain.append(a)
            
            
    def fold_next_amino(self, position, direction):
        """
        Folds the amino acid at the specified position in the chain, in the given direction.
        """
        self.direction_list.append(direction)
        if direction == 1:
            self.aminochain[position].x = self.aminochain[position - 1].x + 1
            self.aminochain[position].y = self.aminochain[position - 1].y
        if direction == -1:
            self.aminochain[position].x = self.aminochain[position - 1].x - 1
            self.aminochain[position].y = self.aminochain[position - 1].y
        if direction == 2:
            self.aminochain[position].y = self.aminochain[position - 1].y + 1
            self.aminochain[position].x = self.aminochain[position - 1].x
        if direction == -2:
            self.aminochain[position].y = self.aminochain[position - 1].y - 1
            self.aminochain[position].x = self.aminochain[position - 1].x
        
        # Checks if a collision has occured by verifiying the uniqueness of all the amino acid coordinates. 
        self.aminocoordinates.append((self.aminochain[position].x, self.aminochain[position].y))
        if len(self.aminocoordinates) != len(set(self.aminocoordinates)):
            self.collision = True
            

  
    def getscore(self):
        """
        Calculates the stability score of the protein. In case of a collision, the score is set to 0. 
        """
        if self.collision == True:
            self.score = 0
        else: 
            x_list = [x.x for x in self.aminochain]
            y_list = [x.y for x in self.aminochain]
            for i in range(0,len(self.string)):
                if self.string[i] == 'H':
                    for j in range(i + 1, len(self.string)):
                        if self.string[j] == 'H' and j - i > 1:
                            if abs(x_list[j] - x_list[i]) == 1 and abs(y_list[j] - y_list[i]) == 0:
                                self.score = self.score + 1
                            
                            if abs(x_list[j] - x_list[i]) == 0 and abs(y_list[j] - y_list[i]) == 1:
                                self.score = self.score + 1

                if self.string[i] == 'C':
                    for k in range(i,len(self.string)):
                        if self.string[k] == 'C' and k-i > 1:
                            if abs(x_list[k] - x_list[i]) == 1 and abs(y_list[k] - y_list[i]) == 0:
                                self.score = self.score + 5

                            if abs(x_list[k] - x_list[i]) == 0 and abs(y_list[k] - y_list[i]) == 1:
                                self.score = self.score + 5
            return self.score
    

    def output(self):
        """
        Creates a CSV representation of the protein, with it's folding directions and score. 
        """
        self.direction_list[-1] = 0
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['amino', 'fold']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for amino, direction in zip(self.string, self.direction_list):
                writer.writerow({'amino': amino, 'fold' : direction})   
            writer.writerow({'amino': 'score', 'fold' : self.score}) 
                        

    def plot(self):
        """
        Visualises the protein in the form of a plot. 
        """
        # Plot the connections between the acids
        x_val = [x.x for x in self.aminochain]
        y_val = [x.y for x in self.aminochain]
        plt.plot(x_val, y_val, 'k', zorder= 1)

        # Plot the amino acids
        colour = []
        for amino in self.aminochain:
            if amino.acid_type == 'H':
                colour.append('red')   
            elif amino.acid_type == 'P':
                colour.append('blue') 
            elif amino.acid_type == 'C':
                colour.append('green')
        for i in range(len(self.string)):
            plt.scatter(self.aminochain[i].x , self.aminochain[i].y, c = colour[i], s = 40, zorder=2)


        # Layout of the plot
        plt.xticks(np.arange(min(x_val) - 4, max(x_val) + 5))
        plt.yticks(np.arange(min(y_val) - 4, max(y_val) + 5))
        plt.ylabel('y_waarden')
        plt.xlabel('x_waarden')
        red_patch = mpatches.Patch(color='red', label='H')
        blue_patch = mpatches.Patch(color='blue', label='P')
        green_patch = mpatches.Patch(color='green', label='C')
        plt.legend(handles=[red_patch, blue_patch, green_patch])
        plt.title(f"{self.string}, Score: {self.score}")
        plt.rc('axes', axisbelow=True)
        plt.show()
