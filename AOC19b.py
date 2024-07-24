
rules = {}

file = open('Advent of Code 2023/aoc 19 input.txt')

for line in file:
    if line == "\n":
        break
    loc = line.find("{")
    rule_set = line[loc+1:-2].split(",")
    res = []
    for i in range(len(rule_set)-1):
        qual = rule_set[i][0]
        op = rule_set[i][1]
        pos = rule_set[i].find(":")
        val = rule_set[i][2:pos]
        next = rule_set[i][pos+1:]
        res.append([qual,op,int(val),next])
    res.append([rule_set[-1]])
    rules.update({line[:loc]:res})

file.close()
def calc_res(x1,x2,m1,m2,a1,a2,s1,s2):
    global total
    x = x2 + 1 -x1
    m = m2 + 1-m1
    a = a2 + 1-a1
    s = s2 + 1-s1
    total += x*m*a*s

def eval(x1,x2,m1,m2,a1,a2,s1,s2,key):
    
    global rules
    set = rules.get(key)
    for i in range(len(set)):
        x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b = x1,x2,m1,m2,a1,a2,s1,s2
        if len(set[i]) == 1:
            key = set[i][0]
            if key == "R":
                continue
            if key == "A":
                calc_res(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b)
                continue
            else:
                eval(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b,key)

        elif set[i][1] == "<":
            if set[i][0] == "x":
                if x2 > set[i][2]:
                    x2b = set[i][2] -1
                    x1 = set[i][2]
            if set[i][0] == "m":
                if m2 > set[i][2]:
                    m2b = set[i][2]-1
                    m1 = set[i][2]
            if set[i][0] == "a":
                if a2 > set[i][2]:
                    a2b = set[i][2]-1
                    a1 = set[i][2]
            if set[i][0] == "s":
                if s2 > set[i][2]:
                    s2b = set[i][2]-1
                    s1 = set[i][2]
            key = set[i][3]
            if key == "R":
                continue
            elif key == "A":
                calc_res(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b)
                continue
            else:
                eval(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b,key)
        elif set[i][1] == ">":
            if set[i][0] == "x":
                if x1 < set[i][2]:
                    x1b = set[i][2] + 1
                    x2 = set[i][2]
            if set[i][0] == "m":
                if m1 < set[i][2]:
                    m1b = set[i][2] + 1
                    m2 = set[i][2]
            if set[i][0] == "a":
                if a1 < set[i][2]:
                    a1b = set[i][2] + 1
                    a2 = set[i][2]
            if set[i][0] == "s":
                if s1 < set[i][2]:
                    s1b = set[i][2] + 1
                    s2 = set[i][2]
            key = set[i][3]
            if key == "R":
                continue
            elif key == "A":
                calc_res(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b)
                continue
            else:
                eval(x1b,x2b,m1b,m2b,a1b,a2b,s1b,s2b,key)

total = 0

key = "in"

x1,x2 = 1, 4000
m1,m2 = 1, 4000
a1,a2 = 1, 4000
s1,s2 = 1, 4000
eval(x1,x2,m1,m2,a1,a2,s1,s2,key)
print(total)