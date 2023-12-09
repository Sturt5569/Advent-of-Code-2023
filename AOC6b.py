file = open('Advent of Code 2023/aoc 6 input.txt')

t = [47847467]
d = [207139412091014]

for i in range(1):
    val = 0
    for j in range(47847467):
        time2 = t[i]-j
        speed = j
        dist = time2 * speed
        if dist > d[i]:
            val += 1
    print(val)

file.close()