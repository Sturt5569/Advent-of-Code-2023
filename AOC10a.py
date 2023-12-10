file = open('Advent of Code 2023/aoc 10 input.txt')
animal = None
map = []

for line in file:
    splitline = []
    for char in line:
        if char == "\n":
            continue
        splitline.append(char)
    map.append(splitline)
    
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            animal = (i,j)


location = animal

visited = []
pending = [location]

steps = 0

while True:
    i, j  = pending.pop()
    if map[i][j] != "S":
        visited.append((i,j))
    steps+= 1
    if map[i][j] == "S" and steps == 1:
        if map[i][j-1] in ("-", "F", "L"):
            pending.append((i,j-1))
        if map[i][j+1] in ("-", "J", "7"):
            pending.append((i,j+1))
        if map[i-1][j] in ("|", "F", "7"):
            pending.append((i-1,j))
        if map[i+1][j] in ("|", "J", "L"):
            pending.append((i+1,j))

    if map[i][j] == "S" and steps > 2:
        print((steps-1)/2)
        break       
    if map[i][j] == "|":
        if (i+1,j) not in visited:
            pending.append((i+1,j))
        if (i-1,j) not in visited:
            pending.append((i-1,j))
    if map[i][j] == "-":
        if (i,j+1) not in visited:
            pending.append((i,j+1))
        if (i,j-1) not in visited:
            pending.append((i,j-1))
    if map[i][j] == "F":
        if (i+1,j) not in visited:
            pending.append((i+1,j))
        if (i,j+1) not in visited:
            pending.append((i,j+1))
    if map[i][j] == "J":
        if (i-1,j) not in visited:
            pending.append((i-1,j))
        if (i,j-1) not in visited:
            pending.append((i,j-1))
    if map[i][j] == "L":
        if (i-1,j) not in visited:
            pending.append((i-1,j))
        if (i,j+1) not in visited:
            pending.append((i,j+1))
    if map[i][j] == "7":
        if (i+1,j) not in visited:
            pending.append((i+1,j))
        if (i,j-1) not in visited:
            pending.append((i,j-1))

    
file.close()