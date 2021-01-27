# dreamteam

### In order to see progress of program
pip instal tqdm 

# Case protein pow(d)er

Proteins are long strings of amino-acids that regulate certain processes in the human body. Proteins consist of strings of different amino-acids that are folded one after another. The way the protein is folded is important for the stabilization of the protein. If the protein is folded incorrectly the protein will not be stable which is the cause of a variety of sicknesses. 
Thus it is necissary to being able to create stable representations of the protein.

Hydrophobic amino acids can form an H-bond between one another which results in extra stabilization for the protein.
our goal was to make a model based on three different amino-acids, H(histidine), C(cysteine) and P(proline), that are as stable as possible.
The stabilization is measured by a score that has certain conditions : 

-- An H amino-acid can form a bond with another H or C amino-acid which adds one point to the score.

--A C amino-acid can form a bond with another C-amino acids which adds five points to the score. 

--A bond can only be formed when the amino-acids are not further than one length apart.

-- A bond will only be formed if amino-acids are directly connected in the given protein string : The amino acids have to form an angle between one another.

With this knowledge we were handed different protein strings. To find the best possible answer we implemented five different algorithms in a 3D-space.


# Algorithms

-- Random algorithm

In the random algorithm a list is made consisting of the 6 possible directions of the system. The first amino-acid initially starts at the point (0,0,0). A random choice is made between the 6 possible directions of the system. This is done for the entire protein string. If the direction that is given ends up in a point it has already been, another random direction is chosen. If the string is build in and thus has zero options to go to, the score is discarded. 

-- Depth-first algorithm

Our depth first algorithm checks the entire state-space for the best solution. This is done by starting at the root of the first amino-acid and going through every option of the string before backtracking. 
The downside of this algorithm is that it takes a long time to form all the possibilities. 


-- Breadth first algorithm

The breadth first algorithm checks the entire state space but does this in a different way than the depth-first. It checks all possible directions for each node before continuing to the next node.
It also takes a long time to finish.

-- Breadth first with pruning

The breadth-firsth with pruning is similar to the normal breadth first but has a couple of additional conditions that make the algorithm run faster. 
If the first couple of amino-acids in the protein string don't form a good enough score the branch is discarded and cut of. This is done for variety of lengths and scores. By doing so the total time is decreased.

-- Beam breadth

The Beam breadth algorithm is also similar to the bread-first algorithm but with a different kind of pruning.
This pruning method creates a list of scores untill it consists of 29 scores. If the next checked score is higher than the minimum of the list it is added to the list and the by then minimum score is cut of the list. If it's lower than the minimum the score is not added to the list and the branch is cut of. 

The best score of all algorithms are kept and visualised in a 3D-plot with an additional output CSV-file that shows all the directions the amino-acids have followed to get from the beginning to the end of the protein string.

# How to run

To run our model the python main.py has to be runned.

python main.py

Then a string is asked for.

possible strings :

CCHHHPCCH

CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC

HCPHPCPHPCHCHPHPPPHPPPHPPPPHPCPHPPPHPHHHCCHCHCHCHH

or any other string that consists of P/H/C.

then the command a/b/c/d/e is asked for which algorithm to run :

a) Random algorithm
b) Depth first algorithm
c) Breadth first algorithm
d) Breadth-first with pruning
e) Beam breadth.

If the option a) for random algorithms is choosen the additional question of how many tries you'd like is asked.
