file = open('Advent of Code 2023/aoc 11 input.txt')
lines = file.readlines()

blankrows = []

for i in range(len(lines)):
    if "#" not in lines[i]:
        blankrows.append(i)
blankrows = blankrows[::-1]

blankline = ""
for i in range(len(lines[0])):
    blankline += "X"

for i in range(len(blankrows)):
    lines[blankrows[i]] = blankline

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
        lend = lines[i][j+1:]
        newline = lstart + "X" + lend
        lines[i] = newline

nodes = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            nodes.append((i,j))

totalsteps = 0
m = 999999 #number of additional steps per "x"
for start in nodes:
    for end in nodes:
        if start == end:
            continue
        else:
            xsteps = 0
            x1,y1 = start
            x2,y2 = end
            xshift = abs(x2-x1)
            yshift = abs(y2-y1)
            if x1>x2:
                s,e = x2,x1
            else:
                s,e = x1,x2
            for i in range(s,e+1):
                if lines[i][y1] == "X":
                    xsteps += m

            if y1>y2:
                s,e = y2,y1
            else:
                s,e = y1,y2
            for i in range(s,e+1):
                if lines[x2][i] == "X":
                    xsteps += m
            path = yshift + xshift + xsteps
        totalsteps += path

print(totalsteps/2)
