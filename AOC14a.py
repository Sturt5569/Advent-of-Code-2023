file = open('Advent of Code 2023/aoc 14 input.txt')
pattern = file.readlines()
file.close()

conv_pattern = []
for i in range(len(pattern[0])):
    newrow = ""
    for row in pattern:
        newrow += row[i]
    conv_pattern.append(newrow)

rockload = 0
for line in conv_pattern:
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
    
    row = row[::-1]
    for i in range(len(row)):
        if row[i] == "O":
            rockload += (i+1) 
    
print(rockload)
