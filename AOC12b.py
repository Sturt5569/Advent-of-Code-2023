file = open('Advent of Code 2023/aoc 12 input.txt')

def validate(point,dep):
    valid = False
    global line
    start,end = point
    if "." in line[0][start:end+1]:
        return False
    try:
        if line[0][start-1] == "#" and start != 0:
            return False
    except IndexError:
        pass
    try:
        if line[0][end+1] == "#":
            return False
    except IndexError:
        pass

    if dep == 0:
        if "#" in line[0][:start]:
            return False

    if points[dep+1] == []:
        gap_end = len(line[0])
        if "#" in line[0][end+1:gap_end]:
            return False

        else:
            dicts[dep].update({start:1})
            return True

    else:
        for p in points[dep+1]:
            gap_end = p[0]
            if "#" in line[0][end+1:gap_end]:
                continue   
            elif end > gap_end-2:
                continue
            else:
                valid = True
    value = 0            
    if valid:
        for key in dicts[dep+1]:
            if key > end+1:
                if "#" not in line[0][end+1:key]:
                    num = dicts[dep+1].get(key)
                    value += num
        dicts[dep].update({start:value})
    
    return valid

def combinations(groups,length,dep,att=""):
    global line
    global points
    global rem_grp_total
    positions = len(line[0])-length-dep

    if dep < len(groups)-1:
        combinations(groups,length,dep+1,att="")
        rem_grp_total += len(groups[dep+1])
        length = length - rem_grp_total
        positions = len(line[0])-length-dep

        for i in range(0,positions+1):    
            start = length + dep - len(groups[dep]) + i
            end = start + len(groups[dep])-1
            point = (start,end)
            if validate(point,dep):
                points[dep].append(point)

    else:
        for i in range(0,positions+1):
            start = length + dep - len(groups[dep]) + i
            end = start + len(groups[dep])-1
            point = (start,end)
            if validate(point,dep):
                points[dep].append(point)

total = 0
for line in file:
    dicts = [{},{},{},{},{},{},{},{},{},{},
         {},{},{},{},{},{},{},{},{},{},
         {},{},{},{},{},{},{},{},{},{},
         {}]

    points = [[],[],[],[],[],[],[],[],[],[],
            [],[],[],[],[],[],[],[],[],[],
            [],[],[],[],[],[],[],[],[],[],
            []]

    rem_grp_total = 0
    linetotal = 0
    number = ""
    line = line.split()
    start = line[0]
    end = line[1]

    for i in range(4):
        line[0] = line[0] + "?" + start
        line[1] = line[1] + "," + end

    groups = []

    for i in range(len(line[1])):
        if line[1][i].isdigit():
            number += line[1][i]
        if line[1][i]== ",":
            groups.append(int(number)*"#")
            number = ""
        if i == len(line[1])-1:
            groups.append(int(number)*"#")

    gs_len = 0
    for group in groups:
        gs_len += len(group)

    broken = []
    gaps = []

    for i in range(len(line[0])):

        if line[0][i] == "#":
            broken.append(i)
        if line[0][i] != ".":
            gaps.append(i)
    combinations(groups,gs_len,0)

    for key in dicts[0]:
        try:
            value = dicts[0].get(key)
            linetotal += value
        except:
            continue
    total += linetotal

print(total)

file.close()
