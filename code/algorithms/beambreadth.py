from .depth import DepthFirst

class   BeamBreadth(DepthFirst):
    

    def get_next_protein(self):
        
        return self.proteins.pop(0)


    def run(self):
        """
        Runs the algorithm untill all versions of the protein are created.
        """
        scores_list = []
        while self.proteins:
            
            protein = self.get_next_protein()
            score = protein.getscore()   
            if len(scores_list) > 3 and score < min(scores_list)-3:
                continue
            else: # Get the next amino acid in the chain.
                scores_list.append(protein.getscore())
                print(f"{len(scores_list)}, {max(scores_list)}, {self.best_solution}")
                amino_position = protein.get_unplaced_amino_position()
                if len(scores_list) > 200:
                    scores_list.remove(min(scores_list))
                if amino_position is not None:
                    self.build_children(protein, amino_position)
                else:
                    self.check_solution(protein)

        # Set's the output to be the protein with the highest score.
        

        return self.best_solution    