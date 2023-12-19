file = open('Advent of Code 2023/aoc 18 input.txt')
lines = file.readlines()
file.close()

pos = [1,1]
visited = [(1,1)]
path = 1

def area(nodes):
    total = 0
    for node in range(len(nodes)-1):
        x = nodes[node+1][0] - nodes[node][0]
        y = nodes[node+1][1] + nodes[node][1]
        z = y*x
        total += z
    return abs(total/2)   

for li in lines:
    line = li.split()
    line[1] = int(line[1])
    if line[0] == "U":
        pos[0] -= line[1]
        visited.append((pos[0],pos[1])) 
    if line[0] == "D":
        path += line[1]
        pos[0] += line[1]
        visited.append((pos[0],pos[1]))
    if line[0] == "R":
        path += line[1]
        pos[1] += line[1]
        visited.append((pos[0],pos[1])) 
    if line[0] == "L":
        pos[1] -= line[1]
        visited.append((pos[0],pos[1]))  

print(int(area(visited)) + path)