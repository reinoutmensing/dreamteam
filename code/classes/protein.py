import csv 
from code.classes.aminoacid import Amino
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits import mplot3d
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D


class Protein():
    """
    Protein class that contains all the items and functions of the amino acid chain. 
    """
    
    def __init__(self, string, id):
        self.id = id
        self.string = string
        self.score = 0 
        self.aminochain = []
        self.direction_list = []
        self.make_protein()
        self.aminocoordinates = []
        self.aminocoordinates.append((self.aminochain[0].x, self.aminochain[0].y, self.aminochain[0].z))
        self.collision = False

    def __repr__(self):
        """
        Returns a representation of the protein.
        """
        return f"{self.string}, {self.score}"
    
    def get_unplaced_amino_position(self):

        for index, amino in enumerate(self.aminochain[1:]):
            if amino.x == 0 and amino.y == 0 and amino.z == 0:
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
        # deler = round(len(self.aminochain) / 3)
        
        # if ((len(self.direction_list) + 1 )% deler == 0):
            # newcord = (self.aminochain[position - 1].x, self.aminochain[position - 1].y, self.aminochain[position - 1].z + 1)
            # direction = 5

        if direction == 1 and 1 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x + 1, self.aminochain[position - 1].y, self.aminochain[position -1].z)
            self.aminochain[position].checklist.append(1)
            
        elif direction == -1 and 2 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x - 1, self.aminochain[position - 1].y, self.aminochain[position -1].z)
            self.aminochain[position].checklist.append(2)
            
        elif direction == 2 and 3 not in self.aminochain[position].checklist:
            
            newcord = (self.aminochain[position - 1].x , self.aminochain[position - 1].y + 1, self.aminochain[position -1].z)
            self.aminochain[position].checklist.append(3)
            
        elif direction == -2 and 4 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x, self.aminochain[position - 1].y - 1, self.aminochain[position -1].z)
            self.aminochain[position].checklist.append(4)
        
        elif direction == 3 and 5 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x, self.aminochain[position - 1].y, self.aminochain[position -1].z + 1)
            self.aminochain[position].checklist.append(5)

        elif direction == -3 and 6 not in self.aminochain[position].checklist:

            newcord = (self.aminochain[position - 1].x, self.aminochain[position - 1].y, self.aminochain[position -1].z - 1)
            self.aminochain[position].checklist.append(6)

        if newcord in set(self.aminocoordinates):
            
            if len(self.aminochain[position].checklist) == 6:
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
            self.aminochain[position].z = newcord[2]
            self.aminocoordinates.append((self.aminochain[position].x, self.aminochain[position].y, self.aminochain[position].z))
            self.direction_list.append(direction)
            return False

    def getscore(self):
        """
        Calculates the stability score of the protein. In case of a collision, the score is set to 0. 
        """
        if self.collision == True:
            self.score = 0
        else: 
            self.score = 0
            x_list = [x.x for x in self.aminochain]
            y_list = [x.y for x in self.aminochain]
            z_list = [x.z for x in self.aminochain] 
            for i in range(len(self.string)):
                for j in range(i+1, len(self.string)):
                    if np.sqrt((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2 + (z_list[i]-z_list[j])**2) == 1 and j-i > 1 and repr(self.aminochain[j]) != "(0, 0, 0)":
                        if self.string[i] == 'H' and (self.string[j] == 'H' or self.string[j] == 'C'):
                            self.score = self.score + 1
                        elif (self.string[i] == 'H' or self.string[i] == 'C') and self.string[j] == 'H':
                            self.score = self.score + 1
                        elif self.string[i] == 'C':
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
        z_val = [x.z for x in self.aminochain]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot3D(x_val, y_val, z_val, 'gray')

        # Plot the amino acids
        def init():
            colour = []
            for amino in self.aminochain:
                if amino.acid_type == 'H':
                    colour.append('red')   
                elif amino.acid_type == 'P':
                    colour.append('blue') 
                elif amino.acid_type == 'C':
                    colour.append('green')
            for i in range(len(self.string)):
                ax.scatter3D(self.aminochain[i].x , self.aminochain[i].y, self.aminochain[i].z, c = colour[i], s = 40, zorder=2)
            
            return fig,
            
        # Plot style elements
        fig.suptitle(f'{self.string}')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        red_patch = mpatches.Patch(color='red', label='H')
        blue_patch = mpatches.Patch(color='blue', label='P')
        green_patch = mpatches.Patch(color='green', label='C')
        ax.legend(handles=[red_patch, blue_patch, green_patch])
        plt.title(f"Score: {self.score}")
        init()
        


        # def animate(i):
        #     ax.view_init(elev=10., azim=i)
        #     return fig,

        # Animate
        # anim = animation.FuncAnimation(fig, animate, init_func=init,
        #                             frames=360, interval=5, blit=True)
        # # Save
        # anim.save('basic_animation.gif', fps=10)

        ax.view_init(elev=20, azim=125)
        plt.show()