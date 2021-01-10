import csv 

class Protein():
    
    def __init__(self, x_list, y_list, string, direction_list):
        self.x_list = x_list
        self.y_list = y_list
        self.string = string
        self.direction_list = direction_list

    def score(self):
        pass

    def output(self):
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['amino', 'fold']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for amino, direction in zip(self.string, self.direction_list):
                writer.writerow({'amino': amino, 'fold' : direction})    
                        
                  
