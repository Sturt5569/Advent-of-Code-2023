file = open('Advent of Code 2023/aoc 8 input.txt')

linenum = 0
turns = []
locs = {}
for line in file:
    linenum += 1
    if linenum == 1:
        for ch in line:
            turns.append(ch)
    elif linenum > 2:
        code = []
        letts = ""
        for ch in line:
            if ch.isalpha():
                letts += ch
            else:
                code.append(letts)
                letts = ""
        locs.update({code[0]:(code[4],code[6])})

curr = "AAA"
dest = "ZZZ" 
count = 0
search = True

while search:
    for turn in turns:
        next = locs.get(curr)
        if turn == "L":
            curr = next[0]
        if turn == "R":
            curr = next[1]
        if turn == "\n":
            continue
        count += 1
        
        if curr == "ZZZ":
            print(count)
            search = False
            break


file.close()