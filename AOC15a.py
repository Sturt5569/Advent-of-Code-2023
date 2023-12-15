file = open('Advent of Code 2023/aoc 15 input.txt')

def run_code(code):
    value = 0
    for ch in code:
        value += ord(ch)
        value *= 17
        value = value % 256
    return value

total = 0
code = []

for line in file:
    for ch in line:
        if ch == "/n":
            continue
        elif ch == ",":
            total += run_code(code)
            code = []
        else:
            code.append(ch)

print(total)
file.close()
