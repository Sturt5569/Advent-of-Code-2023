file = open('Advent of Code 2023/aoc 3 input.txt')
line_1 = ""
line_2 = ""
line_3 = ""
symbol = ["%","*","$","@","+","=","/","#","-","&"]
total = 0
linenum = 0
for line in file:
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
        for key in line_2_numbers:
            digs = len(line_2_numbers.get(key))           
            if line_2[key-1] in symbol:
                total += int(line_2_numbers.get(key))      
            if line_2[key+digs] in symbol:
                total += int(line_2_numbers.get(key))
            for sym in symbol:
                pos = line_3[key-1:key+digs+1].find(sym)
                if pos != -1:
                    total += int(line_2_numbers.get(key))
                pos = line_1[key-1:key+digs+1].find(sym)
                if pos != -1:
                    total += int(line_2_numbers.get(key))
    linenum += 1

for key in line_1_numbers:
    digs = len(line_1_numbers.get(key))
    if line_1[key-1] in symbol:
        total += int(line_1_numbers.get(key))
    if line_1[key+digs+1] in symbol:
        total += int(line_1_numbers.get(key))
    for key in line_1_numbers:
        digs = len(line_1_numbers.get(key))
        for sym in symbol:
            pos = line_2[key-1:key+digs].find(sym)
            if pos != -1:
                total += int(line_1_numbers.get(key))

print(total)
file.close()