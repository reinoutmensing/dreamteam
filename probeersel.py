import matplotlib.pyplot as plt
import random
import csv

shortstring = ['H','P','P','H']
string = ['H','P','P','H','H','P','H','H','H','P','P','P','H','H','H']
string_2 = ['H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H','H']

# print(string.find('H'))

x_list = [0]
y_list = [0]
beginpunt_x = 0
beginpunt_y = 0
oorspronkelijkpunt_x = 0
oorspronkelijkpunt_y = 0
bluepoints_x = []
bluepoints_y = []
redpoints_x = []
redpoints_y = []

if shortstring[0] == 'H':
    bluepoints_x.append(0)
    bluepoints_y.append(0)
else :
    redpoints_x.append(0)
    redpoints_y.append(0)
direction_list = []
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['amino-acid', 'direction']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for place in string:
        check = True

        # is nu zo dat x en y alleen maar groter of alleen maar kleiner kunnen worden
        # beginpunt x zit dan al in de list en y ook
        
        while check == True: 
            counter = 0
            replacement = round(4 * random.random())
            beginpunt_x = oorspronkelijkpunt_x
            beginpunt_y = oorspronkelijkpunt_y 

                
                
                # verplaatsing in de x-richting
            if replacement == 1:
                beginpunt_x = beginpunt_x + 1
                
            if replacement == 2:
                beginpunt_y = beginpunt_y + 1
                
            if replacement == 3:
                beginpunt_x = beginpunt_x - 1

            if replacement == 4:
                beginpunt_y = beginpunt_y - 1
        
            for i in range (0, len(x_list)):
                if beginpunt_y != y_list[i]  or beginpunt_x != x_list[i] :
                    counter = counter + 1    
            if counter == len(x_list):
                check = False
        
        x_list.append(beginpunt_x)
        y_list.append(beginpunt_y)
        oorspronkelijkpunt_x = beginpunt_x
        oorspronkelijkpunt_y = beginpunt_y
        
        plt.ylabel('y_waarden')
        plt.xlabel('x_waarden')

        plt.xlim(-15,15)
        plt.ylim(-15,15)

        direction_list.append(replacement)

        if place == 'H':
            bluepoints_x.append(beginpunt_x)
            bluepoints_y.append(beginpunt_y)
            writer.writerow({'amino-acid': 'H', 'direction' : replacement})    
            
        else :
            redpoints_x.append(beginpunt_x)
            redpoints_y.append(beginpunt_y)
            writer.writerow({'amino-acid': 'P', 'direction' : replacement}) 
            
score = 0


x_punt = []
y_punt = []
x = 0
z = 0
score_add = False
for i in range (0, len(string)):
    if string[i] == 'H':
        for y in range (i + 1,len(string)):
            if string[y] == 'H' :

                if x_list[y] - x_list[i] == 1 and y_list[y] - y_list[i] == 0 :
                    score_add = True
                if x_list[y] - x_list[i] == 0 and y_list[y] - y_list[i] == 1 :
                    score_add = True
                

                if score_add == True  and  y - i != 1:
                    
                    print(y - i)
                    
                    
                    x_punt.append(x_list[i])
                    x_punt.append(x_list[y])
                    y_punt.append(y_list[i])
                    y_punt.append(y_list[y])
                    score = score + 1
                    score_add = False
                x = 0
                z = 0

                    
print(score)

plt.plot(bluepoints_x,bluepoints_y, 'bo', redpoints_x, redpoints_y ,'ro' , x_list, y_list , 'b-', x_punt,y_punt, 'r-')
plt.show()
# (block=False)
# plt.pause(10)
# plt.close()

 # for i in range (0, len(x_list)):
        # print('------------------')
        # print(beginpunt_x)
        # coordinates = {
        #     "coordinate_x" : beginpunt_x,
        #     "coordinate_y" : beginpunt_y
        # }
        # print(coordinates)
        

score_x_list = []
    score = 0
    x_punt = []
    y_punt = []
    for i in range(0,len(protein.string)):
        if protein.string[i] == 'H':
            for j in range(i + 1, len(protein.string)):
                if protein.string[j] == 'H' and j - i > 1:
                    if abs(x_list[j] - x_list[i]) == 1 and abs(y_list[j] - y_list[i]) == 0:
                        score = score + 1
                        # score_x_list.append
                        # x_punt.append(x_list[i])
                        # x_punt.append(x_list[j])
                        # y_punt.append(y_list[i])
                        # y_punt.append(y_list[j])
                    
                    if abs(x_list[j] - x_list[i]) == 0 and abs(y_list[j] - y_list[i]) == 1:
                        score = score + 1

                        # x_punt.append(x_list[i])
                        # x_punt.append(x_list[j])
                        # y_punt.append(y_list[i])
                        # y_punt.append(y_list[j])

        if protein.string[i] == 'C':
            for k in range(i,len(protein.string)):
                if protein.string[k] == 'C' and k-i > 1:
                    if abs(x_list[k] - x_list[i]) == 1 and abs(y_list[k] - y_list[i]) == 0:
                        score = score + 5

                        # x_punt.append(x_list[i])
                        # x_punt.append(x_list[j])
                        # y_punt.append(y_list[i])
                        # y_punt.append(y_list[j])

                    if abs(x_list[k] - x_list[i]) == 0 and abs(y_list[k] - y_list[i]) == 1:
                        score = score + 5

                        # x_punt.append(x_list[i])
                        # x_punt.append(x_list[j])
                        # y_punt.append(y_list[i])
                        # y_punt.append(y_list[j])
                    
    print('________score')
    print(score)

    depth = len(protein.string)
    stack = ['']
    while len(stack) > 0:
        state = stack.pop()
        print(state)
        if len(state) < depth:
            for i in []


        
    