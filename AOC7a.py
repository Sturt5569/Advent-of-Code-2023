file = open('Advent of Code 2023/aoc 7 input.txt')

lett_rank = {"A":1,"K":2, "Q":3, "J":4, "T":5, "9":6, "8":7, "7":8, "6":9, "5":10, "4":11, "3":12, "2":13}

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pairs = []
one_pair = []
high_card = []
def convert_num(ch):
    temp = lett_rank.get(ch)
    return temp
for line in file:
    counts = {"A":0,"K":0, "Q":0, "J":0, "T":0, "9":0, "8":0, "7":0, "6":0, "5":0, "4":0, "3":0, "2":0}
    code = []
    converted = []

    for ch in line:
        if ch == " ":
            break
        else:
            code.append(ch)
    for ch in code:
        num = counts.get(ch)
        num += 1
        counts.update({ch:num})
        dig = convert_num(ch)
        converted.append(dig)

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0 

    for key in counts:
        if counts[key] == 5:
            five += 1
        if counts[key] == 4:
            four += 1
        if counts[key] == 3:
            three += 1
        if counts[key] == 2:
            two += 1
        if counts[key] == 1:
            one += 1
    line = line.split()
    converted.append(int(line[1]))

    if five == 1:
        five_kind.append(converted)
    elif four == 1:
        four_kind.append(converted)
    elif three == 1 and two == 1:
        full_house.append(converted)
    elif three == 1:
        three_kind.append(converted)
    elif two == 2:
        two_pairs.append(converted)
    elif two == 1:
        one_pair.append(converted)
    elif one == 5:
        high_card.append(converted)
    else:
        print("SORT ERROR")
five_kind.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
four_kind.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
full_house.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
three_kind.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
two_pairs.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
one_pair.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))
high_card.sort(key= lambda x: (x[0],x[1],x[2],x[3],x[4]))

final_order = []

for set in five_kind:
    final_order.append(set)
for set in four_kind:
    final_order.append(set)
for set in full_house:
    final_order.append(set)
for set in three_kind:
    final_order.append(set)
for set in two_pairs:
    final_order.append(set)
for set in one_pair:
    final_order.append(set)
for set in high_card:
    final_order.append(set)

total = 0
for i in range(len(final_order)):
    rank = 1000-i
    score = final_order[i][5] * rank
    total += score

print(total)

file.close()