file = open('Advent of Code 2023/aoc 6 input.txt')

t = [47,84,74,67]
d = [207,1394,1209,1014]

for i in range(4):
    val = 0
    for j in range(t[i]):
        time2 = t[i]-j
        speed = j
        dist = time2 * speed
        if dist > d[i]:
            val += 1
    print(val)

file.close()