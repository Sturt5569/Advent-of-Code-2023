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