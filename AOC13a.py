file = open('Advent of Code 2023/aoc 13 input.txt')

total = 0

def matchrows(pattern):
    global total
    maxrow = len(pattern)
    for rnum, row in enumerate(pattern):
        mirror = True
        matchpos = 0
        if rnum == 0:
            continue
        elif rnum <= maxrow/2:
            for i in range(rnum):
                if pattern[rnum+i] == pattern[rnum-i-1]:
                    matchpos = rnum
                    continue
                else:
                    mirror = False
                    break
        elif rnum > maxrow/2:
            for i in range(maxrow-rnum):
                if pattern[rnum+i] == pattern[rnum-i-1]:
                    matchpos = rnum
                    continue
                else:
                    mirror = False
                    break
        if mirror:
            total += (matchpos*100)
            print(total)
            return
    
    matchcols(pattern)
            
def matchcols(pattern):
    global total
    conv_pattern = []
    for i in range(len(pattern[0])):
        newrow = ""
        for row in pattern:
            newrow += row[i]
        conv_pattern.append(newrow)
    pattern = conv_pattern
    maxrow = len(pattern)
    for rnum, row in enumerate(pattern):
        mirror = True
        matchpos = 0
        if rnum == 0:
            continue
        elif rnum <= maxrow/2:
            for i in range(rnum):
                if pattern[rnum+i] == pattern[rnum-i-1]:
                    matchpos = rnum
                    continue
                else:
                    mirror = False
                    break
        elif rnum > maxrow/2:
            for i in range(maxrow-rnum):
                if pattern[rnum+i] == pattern[rnum-i-1]:
                    matchpos = rnum
                    continue
                else:
                    mirror = False
                    break
        if mirror:
            total += (matchpos)
            print(total)
            return



pattern = []
for line in file:
    if line != "\n":
        pattern.append(line[:-1])
    else:
        matchrows(pattern)
        pattern = []

file.close()
