from .depth import DepthFirst

class   PrunedBreadthFirst(DepthFirst):
    

    def get_next_protein(self):
        
        return self.proteins.pop(0)


    def run(self):
        """
        Runs the algorithm untill all versions of the protein are created.
        """
        while self.proteins:
            
            protein = self.get_next_protein()
            if len(protein.direction_list) > 4 and protein.getscore() < 1:
                continue
            if len(protein.direction_list) > 6 and protein.getscore() < 2:
                continue
            if len(protein.direction_list) > 8 and protein.getscore() < 3:
                continue
            else: # Get the next amino acid in the chain.
                amino_position = protein.get_unplaced_amino_position()
                if amino_position is not None:
                    self.build_children(protein, amino_position)
                else:
                    self.check_solution(protein)

        # Set's the output to be the protein with the highest score.
        protein = self.best_solution

        return protein    
    