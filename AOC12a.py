file = open('Advent of Code 2023/aoc 12 input.txt')
total = 0

def validate(att, ref):
    global total
    valid = True
    for i in range(len(att)):
        if ref[i] == "#" and att[i] != "#":
            valid = False
        if ref[i] == "." and att[i] != ".":
            valid = False
    if valid:
        total += 1

def combinations(keys,reference,length,dep,att=""):
    
    if dep == 0:
        positions = len(reference)-length
        for i in range(0,positions+1):
            attempt = att
            attempt += "."*i + keys[dep]
            combinations(keys,reference,length+i,dep+1,attempt)  

    elif dep < len(keys)-1 and dep > 0:
        positions = len(reference)-length
        for i in range(1,positions+1):
            attempt = att
            attempt += "."*i + keys[dep]
            combinations(keys,reference,length+i,dep+1,attempt)
    else:
        positions = len(reference)-length
        for i in range(1,positions+1):
            attempt = att
            attempt += "."*i + keys[dep]
            while len(attempt) < len(reference):
                attempt += "."
            validate(attempt,reference)
            
for line in file:
    number = ""
    line = line.split()

    groups = []
    for i in range(len(line[1])):
        if line[1][i].isdigit():
            number += line[1][i]
        if line[1][i]== ",":
            groups.append(int(number)*"#")
            number = ""
        if i == len(line[1])-1:
            groups.append(int(number)*"#")
    grouptotal = 0
    for group in groups:
        grouptotal += len(group)
        
    combinations(groups,line[0],grouptotal,0)
    
print(total)
file.close()
