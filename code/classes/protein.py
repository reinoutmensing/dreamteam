import csv 

class Protein():
    
    def __init__(self, x_list, y_list, string, direction_list):
        self.x_list = x_list
        self.y_list = y_list
        self.string = string
        self.direction_list = direction_list

    def score(self):
        score = 0
       
        for i in range(0,len(self.string)):
            if self.string[i] == 'H':
                for j in range(i + 1, len(self.string)):
                    if self.string[j] == 'H' and j - i > 1:
                        if abs(self.x_list[j] - self.x_list[i]) == 1 and abs(self.y_list[j] - self.y_list[i]) == 0:
                            score = score + 1
                        
                        if abs(self.x_list[j] - self.x_list[i]) == 0 and abs(self.y_list[j] - self.y_list[i]) == 1:
                            score = score + 1

            if self.string[i] == 'C':
                for k in range(i,len(self.string)):
                    if self.string[k] == 'C' and k-i > 1:
                        if abs(self.x_list[k] - self.x_list[i]) == 1 and abs(self.y_list[k] - self.y_list[i]) == 0:
                            score = score + 5

                        if abs(self.x_list[k] - self.x_list[i]) == 0 and abs(self.y_list[k] - self.y_list[i]) == 1:
                            score = score + 5
        print(score)
        return score
        

    def output(self):
        with open('output.csv', 'w', newline='') as csvfile:
            fieldnames = ['amino', 'fold']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for amino, direction in zip(self.string, self.direction_list):
                writer.writerow({'amino': amino, 'fold' : direction})    
                        
                  
