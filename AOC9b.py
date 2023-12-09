import math
file = open('Advent of Code 2023/aoc 9 input.txt')

def differences(set):
    newset = []
    for i in range(len(set)-1):
        num = set[i+1] - set[i]
        newset.append(num)
    zero = True
    for num in newset:
        if num != 0:
            zero = False       
    if zero == True:
        return newset[-1]+set[-1]      
    else:
        return differences(newset)+ set[-1]
    
total = 0   
for line in file:
    line = line.split()[::-1]
    
    for i in range(len(line)):
        line[i] = int(line[i])
    
    next_in_line = differences(line)
    total += next_in_line
    
print(total)

file.close()