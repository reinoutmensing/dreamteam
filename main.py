from code.algorithms.random import random_algorithm
from code.classes.protein import Protein
from code.algorithms.depth import DepthFirst
from code.algorithms.breadth import BreadthFirst
from code.algorithms.pruned_breadth import PrunedBreadthFirst

if __name__ == "__main__":

    # Amino acid chain
    string = input("Provide amino acid chain:").upper()

    # Random algorithm
    # try_number = int(input("Provide number of tries:"))
    # algo = random_algorithm(string, try_number)
    # score_list = algo[1]
    # highest_protein = algo[2]
    # # Visualisatie en CSV output random algorithm
    # highest_protein.plot()
    # highest_protein.output()

    # # Depth first algorithm
    # algo = DepthFirst(string)
    # algo.run()
    # # Visualisatie en CSV output random algorithm
    # algo.run().plot()
    # algo.run().output()


    # Breadth first algorithm

    # algo = BreadthFirst(string)
    # algo.run()
    
    # algo.run().plot()
    # algo.run().output()
   


    algo = PrunedBreadthFirst(string)
    algo.run()
    
    algo.run().plot()
    algo.run().output()
   


  
    
  
