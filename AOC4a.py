file = open('Advent of Code 2023/aoc 4 input.txt')
points = 0
for line in file:
    print(line)
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
    print(card)
    if card == 1:
        points += 1
    if card > 1:
        init = 1
        for i in range(card-1):
            init *= 2
        points += init
print(points)
file.close()