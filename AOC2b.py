file = open('Advent of Code 2023/aoc2 Input.txt')
total = 0
for line in file:
    green = 0
    red = 0
    blue = 0

    words = line.split()
    game_number = words[1]
    game_number = game_number[:-1]
    words[1] = game_number
    print(words)
    for i in range(len(words)):
        if 'blue' in words[i]:
            if int(words[i-1]) > blue:
                blue = int(words[i-1])
        if 'red' in words[i]:
            if int(words[i-1]) > red:
                red = int(words[i-1])
        if 'green' in words[i]:
            if int(words[i-1]) > green:
                green = int(words[i-1])
    set = green*blue*red
    total += set
print(total)
file.close()