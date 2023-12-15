file = open('Advent of Code 2023/aoc 15 input.txt')
boxes = [[] for x in range(256)]

def run_code(code):
    box = 0

    for ch in code:
        if ch.isalpha():
            box += ord(ch)
            box *= 17
            box = box % 256
        if ch == "-":
            remove_lens(code,box)
            break
        if ch == "=":
            add_lens(code,box)
            break

def remove_lens(code,box):
    for i in range(len(boxes[box])):
        if code[:-1] == boxes[box][i][0]:
            del boxes[box][i]
            break

def add_lens(code, box):
    if boxes[box] == []:
        boxes[box].append([code[:-2],code[-1]])
    else:
        found = False
        for pos,lens in enumerate(boxes[box]):
            if lens[0] == code[:-2]:
                boxes[box][pos][1] = code[-1]
                found = True
                break
        if found:
            return
        else:
            boxes[box].append([code[:-2],code[-1]])
 
total = 0
code = ""

for line in file:
    for ch in line:
        if ch == "/n":
            continue
        elif ch == ",":
            run_code(code) 
            code = ""
        else:
            code += ch
total = 0

for i, box in enumerate(boxes):
    power = i+1
    for j, slot in enumerate(box):
        total += power * (j+1) * int(slot[1])

print(total)
file.close()
