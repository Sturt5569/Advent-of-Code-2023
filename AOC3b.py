file = open('Advent of Code 2023/aoc 3 input.txt')
line_1 = ""
line_2 = ""
line_3 = ""
total = 0
linenum = 0

def find_gear(index):
    global total
    i = index
    cogs = []
    for key in line_1_numbers:
        num_start = key-1
        num_end = key+len(line_1_numbers.get(key))
        if num_start <= i and num_end >= i:
            cogs.append(line_1_numbers.get(key))
    if linenum > 1:
        for key in line_3_numbers:
            num_start = key-1
            num_end = key+len(line_3_numbers.get(key))
            if num_start <= i and num_end >= i:
                cogs.append(line_3_numbers.get(key))
    for key in line_2_numbers:
        if key-1 == i:
            cogs.append(line_2_numbers.get(key))
        if key+len(line_2_numbers.get(key)) == i:
            cogs.append(line_2_numbers.get(key))
    print(cogs)
    if len(cogs) == 2:
        output = int(cogs[0]) * int(cogs[1])
        print(output)
        total += output
            
for line in file:
    print(linenum)
    if linenum > 1:
        line_3 = line_2
        line_3_numbers = line_2_numbers
    if linenum > 0:
        line_2 = line_1
        line_2_numbers = line_1_numbers

    line_1 = line 
    line_1_numbers = {}

    number=""
    for i in range(len(line_1)):
        if line_1[i].isdigit():
            number += line_1[i]
        if number != "" and not line_1[i].isdigit():
            line_1_numbers.update({i-len(number):number})
            number = ""

    if linenum > 0:
        for i in range(len(line_2)):
            if line_2[i] == "*":
                find_gear(i)
                
    linenum += 1



print(total)
file.close()