from code.algorithms.random2 import random_algorithm



if __name__ == "__main__":

    # Amino acid chain
    string = input("Provide amino acid chain:").upper()

    # Number of tries
    try_number = int(input("Provide number of tries:"))

    # Folding algorithm
    algo = random_algorithm(string, try_number)
    score_list = algo[1]
    highest_protein = algo[2]

    # CSV output
    highest_protein.output()

    # Visualisatie
    highest_protein.plot()
