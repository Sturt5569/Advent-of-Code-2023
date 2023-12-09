file = open('Advent of Code 2023/aoc 4 input.txt')
cards = {}
for i in range(1,212):
    cards.update({i:1})
linenum = 1
for line in file:
    
    card = 0
    draw = []
    player = []
    numbers = line.split()
    for i in range(len(numbers)):
        if i < 2:
            continue
        elif i < 12:
            draw.append(numbers[i])
        elif i > 12:
            player.append(numbers[i])
    for num in player:
        if num in draw:
            card += 1
    
    if linenum < 211:
        number_of_cards = cards.get(linenum)
        for i in range(number_of_cards):
            for i in range(card):
                curr_card = linenum + 1 + i
                curr_value = cards.get(curr_card)
                curr_value += 1
                cards.update({curr_card:curr_value})
    linenum += 1
total = 0
for key in cards:
    temp = cards.get(key)
    total += temp
print(total)
file.close()