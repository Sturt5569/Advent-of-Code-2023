file = open('Advent of Code 2023/aoc 18 input.txt')
lines = file.readlines()
file.close()

pos = [1,1]
visited = [(1,1)]
path = 1

def area(coords):
    t = 0
    for count in range(len(coords)-1):
        y = coords[count+1][1] + coords[count][1]
        x = coords[count+1][0] - coords[count][0]
        z = y*x
        t += z
    return abs(t/2)  

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