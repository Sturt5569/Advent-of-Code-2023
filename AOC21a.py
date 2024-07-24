file = open('Advent of Code 2023/aoc 21 input.txt')
lines = file.readlines()
file.close()

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == "S":
            pos = [i,j]
next_step = [[pos]]
max_i = len(lines)-1
max_j = len(lines[0]) - 1

for x in range(64):
    set = next_step.pop(0)
    newset = []
    for node in set:
        i,j = node
        if lines[i+1][j] != "#" and i+1 < max_i:
            if [i+1,j] not in newset:
                newset.append([i+1,j])
        if lines[i-1][j] != "#" and i > 0:
            if [i-1,j] not in newset:
                newset.append([i-1,j])
        if lines[i][j+1] != "#" and j+1 < max_j:
            if [i,j+1] not in newset:
                newset.append([i,j+1])
        if lines[i][j-1] != "#" and j > 0:
            if [i,j-1] not in newset:
                newset.append([i,j-1])
    next_step.append(newset)
    print(len(newset))