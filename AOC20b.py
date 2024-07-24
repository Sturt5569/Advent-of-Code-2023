modules = {}
fl_fl = {}
cons = {}
pulse_stk = []
low_count = 0
high_count = 0

file = open('Advent of Code 2023/aoc 20 input.txt')
lines = file.readlines()
file.close()

for line in lines:
    line = line.replace(",","").split()
    if line[0] == "broadcaster":
        dest = []
        for i in range(2,len(line)):
            dest.append(line[i])
        modules.update({"bcst":dest})

    elif line[0][0] == "%":
        dest = []
        for i in range(2,len(line)):
            dest.append(line[i])
        fl_fl.update({line[0][1:]:[0,dest]})
        modules.update({line[0][1:]:"%"})

    elif line[0][0] == "&":
        dest = []
        for i in range(2,len(line)):
            dest.append(line[i])
        cons.update({line[0][1:]:[dest,[]]})
        modules.update({line[0][1:]:"&"})

for key in cons:
    inputs = []
    for line in lines:
        line = line.replace(",","").split()
        if key in line[2:]:
            inputs.append([line[0][1:],0])
    newvals = cons.get(key)
    newvals[1] = inputs
 
cycles = 10000
i = 0
for i in range(cycles):
    i += 1

    for b in modules.get("bcst"):
        pulse_stk.append((b,"L",0))                                                                         

    while True:     
        #print(pulse_stk[0])  
        mod,val,frm = pulse_stk.pop(0)
        if modules.get(mod) == "%":
            if val == "L":
                node = fl_fl.get(mod)
                if node[0] == 0:
                    node[0] = 1
                    pls = "H"
                else:
                    node[0] = 0
                    pls = "L"
                fl_fl.update({mod:node})
                for n in node[1]:
                    pulse_stk.append((n,pls,mod))

        if modules.get(mod) == "&":
            chk_mod = cons.get(mod)[1]
            for i,m in enumerate(chk_mod):
                if m[0] == frm:
                    if val == "H":
                        chk_mod[i][1] = 1
                    elif val == "L":
                        chk_mod[i][1] = 0
            pls = "L"
            for m in chk_mod:
                if m[1] == 0:
                    pls = "H"
            nodes = cons.get(mod)[0]
            for n in nodes:
                pulse_stk.append((n,pls,mod))

        if pulse_stk == []:
            break 
        #print(cons.get("ql")[1])

