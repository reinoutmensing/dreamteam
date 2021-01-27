from .depth import DepthFirst

class   BeamBreadth(DepthFirst):
    

    def get_next_protein(self):
        """
        Get's the first element of the list of proteins that are being build. 
        """
        
        return self.proteins.pop(0)


    def run(self):
        """
        Runs a version of the breadth first algorithm, 
        while only building further on the 20 proteins with the highest scores.
        """

        scores_list = []
        while self.proteins:
            protein = self.get_next_protein()
            score = protein.getscore()   
            if len(scores_list) > 19 and score < min(scores_list):
                continue
            else: # Get the next amino acid in the chain.
                scores_list.append(protein.getscore())
                amino_position = protein.get_unplaced_amino_position()
                if len(scores_list) > 20:
                    scores_list.remove(min(scores_list))
                if amino_position is not None:
                    self.build_children(protein, amino_position)
                else:
                    self.check_solution(protein)

        # Set's the output to be the protein with the highest score.
        protein = self.best_solution
        return self.best_solution    