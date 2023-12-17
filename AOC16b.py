file = open('Advent of Code 2023/aoc 16 input.txt')

pattern = []
for line in file:
    pattern.append(line[:-1])
file.close()

visited = []
pending = [("east",0,0)]
    
def dfs(point):
    global visited
    pending = [point]
    while True:
        if pending == []:
            return
        next = pending.pop()
        dir,i, j = next
        if i not in range(0,len(pattern)) or j not in range(0,len(pattern[0])):
            return
        if next not in visited:
            visited.append(next)
            if pattern[i][j] == ".":
                if dir == "east":
                    pending.append(("east",i,j+1))
                elif dir == "west":
                    pending.append(("west",i,j-1))
                elif dir == "south":
                    pending.append(("south",i+1,j))
                elif dir == "north":
                    pending.append(("north",i-1,j))

            if pattern[i][j] == "|":
                if dir == "east" or dir == "west":
                    dfs(("north",i-1,j))
                    dfs(("south",i+1,j))
                elif dir == "south":
                    pending.append(("south",i+1,j))
                elif dir == "north":
                    pending.append(("north",i-1,j))

            if pattern[i][j] == "-":
                if dir == "east":
                    pending.append(("east",i,j+1))
                if dir == "west":
                    pending.append(("west",i,j-1))
                elif dir == "south" or dir == "north":
                    dfs(("east",i,j+1))
                    dfs(("west",i,j-1))

            if pattern[i][j] == "/":
                if dir == "east":
                    pending.append(("north",i-1,j))
                elif dir == "west":
                    pending.append(("south",i+1,j))
                elif dir == "south":
                    pending.append(("west",i,j-1))
                elif dir == "north":
                    pending.append(("east",i,j+1))

            if pattern[i][j] == "M":
                if dir == "east":
                    pending.append(("south",i+1,j))
                elif dir == "west":
                    pending.append(("north",i-1,j))
                elif dir == "south":
                    pending.append(("east",i,j+1))
                elif dir == "north":
                    pending.append(("west",i,j-1))

longest = 0
print("Searching East...")
for i in range(len(pattern)):
    dfs(("east",i,0))
    output = []
    for visit in visited:
        output.append((visit[-2],visit[-1]))
    output = set(output)
    if len(output) > longest:
        longest = len(output)
    visited = []
    print(longest)

print("Searching West...")
for i in range(len(pattern)):
    dfs(("west",i,len(pattern[0])-1))
    output = []
    for visit in visited:
        output.append((visit[-2],visit[-1]))
    output = set(output)
    if len(output) > longest:
        longest = len(output)
    visited = []

print("Searching South...")
for i in range(len(pattern[0])):
    dfs(("south",0,i))
    output = []
    for visit in visited:
        output.append((visit[-2],visit[-1]))
    output = set(output)
    if len(output) > longest:
        longest = len(output)
    visited = []

print("Searching North...")
for i in range(len(pattern[0])):
    dfs(("north",0,len(pattern)-2))
    output = []
    for visit in visited:
        output.append((visit[-2],visit[-1]))
    output = set(output)
    if len(output) > longest:
        longest = len(output)
    visited = []

print(longest)