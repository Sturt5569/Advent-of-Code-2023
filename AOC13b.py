file = open('Advent of Code 2023/aoc 13 input.txt')

total = 0

def find_hor_smudge(pattern):
    global total
    maxrow = len(pattern)
    maxcol = len(pattern[0])
    row_singles = []
    for rnum, row in enumerate(pattern):
        row_errors = []
        if rnum == 0:
            continue
        elif rnum <= maxrow/2:
            for i in range(rnum):
                pair_errors = []
                for j in range(maxcol):
                    if pattern[rnum+i][j] == pattern[rnum-i-1][j]:
                        continue
                    else:
                        pair_errors.append((i,j))
                if len(pair_errors) > 0:
                    for pair in pair_errors:
                        row_errors.append(pair)
        elif rnum > maxrow/2:
            for i in range(maxrow-rnum):
                pair_errors = []
                for j in range(maxcol):
                    if pattern[rnum+i][j] == pattern[rnum-i-1][j]:
                        continue
                    else:
                        pair_errors.append((i,j))
                if len(pair_errors) > 0:
                    for pair in pair_errors:
                        row_errors.append(pair)
        if len(row_errors) == 1:
            row_singles.append((rnum,row_errors))
    if len(row_singles) == 1:
        total += row_singles[0][0] * 100
    else:
        find_vert_smudge(pattern)

def find_vert_smudge(pattern):
    global total
    conv_pattern = []
    for i in range(len(pattern[0])):
        newrow = ""
        for row in pattern:
            newrow += row[i]
        conv_pattern.append(newrow)
    pattern = conv_pattern
    maxrow = len(pattern)
    maxcol = len(pattern[0])
    row_singles = []
    for rnum, row in enumerate(pattern):
        row_errors = []
        if rnum == 0:
            continue
        elif rnum <= maxrow/2:
            for i in range(rnum):
                pair_errors = []
                for j in range(maxcol):
                    if pattern[rnum+i][j] == pattern[rnum-i-1][j]:
                        continue
                    else:
                        pair_errors.append((i,j))
                if len(pair_errors) > 0:
                    for pair in pair_errors:
                        row_errors.append(pair)
        elif rnum > maxrow/2:
            for i in range(maxrow-rnum):
                pair_errors = []
                for j in range(maxcol):
                    if pattern[rnum+i][j] == pattern[rnum-i-1][j]:
                        continue
                    else:
                        pair_errors.append((i,j))
                if len(pair_errors) > 0:
                    for pair in pair_errors:
                        row_errors.append(pair)
        if len(row_errors) == 1:
            row_singles.append((rnum,row_errors))
    if len(row_singles) == 1:
        total += row_singles[0][0]
    else:
        print("Unhandled Set")


pattern = []
for line in file:
    if line != "\n":
        pattern.append(line[:-1])
    else:
        find_hor_smudge(pattern)
        pattern = []
print(total)
file.close()
