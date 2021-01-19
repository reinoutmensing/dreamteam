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
    
    def get_unplaced_amino_position(self):

        for index, amino in enumerate(self.aminochain[1:]):
            if amino.x == 0 and amino.y == 0:
                return index + 1
        
        return None

        
            



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

        newcord = None
        if direction == 1 and 1 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x + 1, self.aminochain[position - 1].y)
            self.aminochain[position].checklist.append(1)
            

        elif direction == -1 and 2 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x - 1, self.aminochain[position - 1].y)
            self.aminochain[position].checklist.append(2)
            
        elif direction == 2 and 3 not in self.aminochain[position].checklist:
            
            newcord = (self.aminochain[position - 1].x , self.aminochain[position - 1].y + 1)
            self.aminochain[position].checklist.append(3)
            
        elif direction == -2 and 4 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x, self.aminochain[position - 1].y - 1)
            self.aminochain[position].checklist.append(4)
            
        
        if newcord in set(self.aminocoordinates):
            
            # Code is build in
            if len(self.aminochain[position].checklist) == 4:
                self.collision = True
                return False
            

            else:
                # and checklist
                return True
        elif newcord == None:
            # and checklist
            return True 


        else :
            self.aminochain[position].x = newcord[0]
            self.aminochain[position].y = newcord[1]

        # Checks if a collision has occured by verifiying the uniqueness of all the amino acid coordinates. 
            self.aminocoordinates.append((self.aminochain[position].x, self.aminochain[position].y))
            self.direction_list.append(direction)
            return False
        
        # wat je kan doen is de directions per coor bijhouden en zorgen dat hij niet twee keer dezelfde directie op kan gaan
        # dan een counter bijhouden en als de counter op vier staat zorgen dat de functie breakt en de volgende string bekeken wordt.
       

  
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
