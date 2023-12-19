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
    dir = line[2][-2]
    hex = int(line[2][2:-2],16)

    if dir == "3":
        pos[0] -= hex
        visited.append((pos[0],pos[1])) 
    if dir == "1":
        path += hex
        pos[0] += hex
        visited.append((pos[0],pos[1]))
    if dir == "0":
        path += hex
        pos[1] += hex
        visited.append((pos[0],pos[1])) 
    if dir == "2":
        pos[1] -= hex
        visited.append((pos[0],pos[1]))  

print(int(area(visited)) + path)