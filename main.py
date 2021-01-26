from code.algorithms.random import RandomAlgorithm
from code.classes.protein import Protein
from code.algorithms.depth import DepthFirst
from code.algorithms.breadth import BreadthFirst
from code.algorithms.pruned_breadth import PrunedBreadthFirst
from code.algorithms.beambreadth import BeamBreadth
import re

if __name__ == "__main__":

    # Let's the user provide an amino acid chain and validates the input
    while True:
        string = input("Provide amino acid chain:").upper()
        if not bool(re.match('^[HCP]+$', string)):
            print("Please provide a valid amino acid chain")
            continue
        else:
            # Valid string was provided
            break
    
    # Let's the user select the algorithm and validates the choice
    while True:
        algorithm = input("Select algorithm: A for Random, B for BreadthFirst, \
C for DepthFirst, D for PrunedBreadthFirst or E for BeamBreadth:").upper()
        if algorithm not in ('A', 'B', 'C', 'D', 'E'):
            print("Not an appropriate choice.")
        else:
            break

    # Algorithms
    print(algorithm)
    if algorithm == 'A':
        try_number = int(input("Provide number of proteins the algorithm has to produce:"))
        algo = RandomAlgorithm(string, try_number)
    if algorithm == 'B':
        algo = BreadthFirst(string)
    if algorithm == 'C':
        algo = DepthFirst(string)
    if algorithm == 'D':
        algo = PrunedBreadthFirst(string)
    if algorithm == 'E':
        algo = BeamBreadth(string)
    
    # Run algorithm, visualisation and CSV output
    algo.run()
    algo.best_solution.plot()
    algo.best_solution.output()
  
    
  
