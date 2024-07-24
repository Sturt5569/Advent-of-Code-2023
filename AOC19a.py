rules = {}
metals = []
file = open('Advent of Code 2023/aoc 19 input.txt')

sec = "R"
for line in file:
    if line == "\n":
        sec = "M"
        continue
    if sec == "R":
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
    else:
        line = line[1:-2].split(",")
        metals.append(line)
file.close()

total = 0

for metal in metals:
    ref = { "x":int(metal[0][2:]),
            "m":int(metal[1][2:]),
            "a":int(metal[2][2:]),
            "s":int(metal[3][2:])
    }
    rule_key = "in"
    while True:
        rule_set = rules.get(rule_key)
        for i in range(len(rule_set)):
            quality = rule_set[i][0]
            value = ref.get(quality)

            if i == len(rule_set)-1:
                rule_key = rule_set[-1][0]
                break
            elif rule_set[i][1] == "<":
                if value < rule_set[i][2]:
                    rule_key = rule_set[i][3]
                    break
            elif rule_set[i][1] == ">":
                if value > rule_set[i][2]:
                    rule_key = rule_set[i][3]
                    break
            elif rule_set[i][1] == "=":
                if value == rule_set[i][2]:
                    rule_key = rule_set[i][3]
                    break
            else:
                rule_key = rule_set[-1]
                break
        if rule_key == "R":
            break
        if rule_key == "A":
            x = ref.get("x")
            m = ref.get("m")
            a = ref.get("a")
            s = ref.get("s")
            total += (x+m+a+s)
            break
print(total)
    
