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
currs = []
for key in locs:
    if key[2] == "A":
        currs.append(key)
print(currs)
count,count2 = 0,0

search = True
results = []
while search:
    for turn in turns:
        for i in range(len(currs)):
            next = locs.get(currs[i])
            if turn == "L":
                currs[i] = next[0]
            if turn == "R":
                currs[i] = next[1]
            if turn == "\n":
                continue
            count += 1
            
            if currs[i][2] == "Z":
                results.append(count-count2)
                count2 = count
                if len(results) == 10:
                    search = False
                    break


            
            

file.close()