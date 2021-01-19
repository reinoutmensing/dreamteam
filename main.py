from code.algorithms.random2 import random_algorithm
from code.classes.protein import Protein
from code.algorithms.depth import DepthFirst

if __name__ == "__main__":

    # Amino acid chain
    string = input("Provide amino acid chain:").upper()

    # Number of tries
    try_number = int(input("Provide number of tries:"))

    # Folding algorithm

    algo = DepthFirst(string)
    algo.run()

    # score_list = algo[1]
    # highest_protein = algo[2]

    # # CSV output
    algo.protein.output()
    algo.protein.getscore()

    # # Visualisatie
    algo.protein.plot()
