file = open('Advent of Code 2023/aoc 11 input.txt')
lines = file.readlines()

## ------ Add extra rows where no galaxies exist ------ ## 
blankrows = []
for i in range(len(lines)):
    if "#" not in lines[i]:
        blankrows.append(i)
blankrows = blankrows[::-1]

for i in range(len(blankrows)):
    addline = lines[blankrows[i]]
    lines.insert(blankrows[i],lines[blankrows[i]])

## ------ Add extra columns where no galaxies exist ------ ##
blankcolumns = []
for i in range(len(lines[0])):
    blank = True
    for line in lines:
        if line[i] == "#":
            blank = False
    if blank:
        blankcolumns.append(i)

blankcolumns = blankcolumns[::-1]
for i in range(len(lines)):
    for j in blankcolumns:
        lstart = lines[i][:j]
        lend = lines[i][j:]
        newline = lstart + "." + lend
        lines[i] = newline

## ------ Get node position and determine distances ------ ##
nodes = []

ref = len(lines[0])

for i in range(len(lines)):
    for j in range(ref):
        if lines[i][j] == "#":
            nodes.append((i,j))

totalsteps = 0

for start in nodes:
    for end in nodes:
        if start == end:
            continue
        else:
            x1,y1 = start
            x2,y2 = end
            xshift = abs(x2-x1)
            yshift = abs(y2-y1)
            path = xshift + yshift

        totalsteps += path

print(totalsteps/2)



file.close()