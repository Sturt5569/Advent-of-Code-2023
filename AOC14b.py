file = open('Advent of Code 2023/aoc 14 input.txt')
pattern = file.readlines()
file.close()

def orient(pattern):
    conv_pattern = []
    for i in range(len(pattern[0])-1,-1,-1):
        newrow = ""
        for row in pattern:
            newrow += row[i]
        conv_pattern.append(newrow)
    del conv_pattern[0]
    return conv_pattern

def rotate(pattern):
    conv_pattern = []
    for i in range(len(pattern[0])):
        newrow = ""
        for row in pattern:
            newrow = row[i] + newrow
        conv_pattern.append(newrow)
    return conv_pattern

def roll_rocks(pattern):
    rockload = 0
    rolled_pattern = []
    for line in pattern:
        row = []
        for ch in line:
            row.append(ch)
        
        for i in range(len(line)):
            if row[i] == "O":
                val = i
                while True:
                    val -= 1
                    if val < 0 or row[val] == "#" or row[val] == "O":
                        row[i], row[val+1] = row[val+1],row[i]
                        break
        rolled_pattern.append(row)
 
    return rolled_pattern

def get_loading(pattern):
    rockload = 0
    for line in pattern:
        row = []
        for ch in line:
            row.append(ch)
        row = row[::-1]
        for i in range(len(row)):
            if row[i] == "O":
                rockload += (i+1)
    return rockload

northload = 0
count = 0
counts = []
doubles = []
for i in range(1600):
    count += 1
    if i == 0:
        pattern = orient(pattern)
    else:
        pattern = rotate(pattern) 
    pattern = roll_rocks(pattern)

    if count == 4:
        subpattern = pattern[:]
        subpattern = rotate(subpattern)
        value = get_loading(subpattern)
        if value not in counts:
            counts.append(value)
        else:
            doubles.append((int((i+1)/4),value))
        
        count = 0

doubles = doubles[100:]
seq = []
for double in doubles:
    seq.append(double[1])

for x in range(2,len(seq)):
    if seq[0:x] == seq[x:2*x]:
        seq_len = x

start_pos = doubles[0][0]
remain = (1000000000 - start_pos) % seq_len
print(doubles[remain][1])