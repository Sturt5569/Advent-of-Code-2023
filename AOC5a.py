file = open('Advent of Code 2023/aoc 5 input.txt')

filter = 0
seeds = []
seedsoil = []
soilfert = []
fertwater = []
waterlight = []
lighttemp = []
temphumid = []
humidloc = []

for line in file:

    if line.find("seed-to-soil") != -1:
        filter += 1
        continue
    if line.find("soil-to-fertilizer") != -1:
        filter += 1
        continue
    if line.find("fertilizer-to-water") != -1:
        filter += 1
        continue
    if line.find("water-to-light") != -1:
        filter += 1
        continue
    if line.find("light-to-temperature") != -1:
        filter += 1
        continue
    if line.find("temperature-to-humidity") != -1:
        filter += 1
        continue
    if line.find("humidity-to-location") != -1:
        filter += 1
        continue
    line = line.split()
    if len(line) == 0:
        continue    
    if line[0] == "seeds:":
        seeds = line[1:]

    if filter == 1:
        seedsoil.append(line)
    if filter == 2:
        soilfert.append(line)
    if filter == 3:
        fertwater.append(line)
    if filter == 4:
        waterlight.append(line)
    if filter == 5:
        lighttemp.append(line)
    if filter == 6:
        temphumid.append(line)
    if filter == 7:
        humidloc.append(line)
    #print(line)

locs = []
for seed in seeds:
    found = False
    for x in seedsoil:
        if int(seed) >= int(x[1]) and int(seed) <= (int(x[1]) + int(x[2])):
            found = True
            soil = int(seed) + (int(x[0]) - int(x[1]))
            #print(seed,x[0],(int(x[0]) + int(x[2])))
    if not found:
        soil = seed
        print(seed,"soilnotfound",soil)
    

    found = False
    for x in soilfert:
        if int(soil) >= int(x[1]) and int(soil) <= (int(x[1]) + int(x[2])):
            found = True
            fert = int(soil) + (int(x[0]) - int(x[1]))       
    if not found:
        fert = soil
        print(seed,soil,"fertnotfound",soil)

    found = False
    for x in fertwater:
        if int(fert) >= int(x[1]) and int(fert) <= (int(x[1]) + int(x[2])):
            found = True
            water = int(fert) + (int(x[0]) - int(x[1])) 
    if not found:
        water = fert
        print(seed,fert,"waternotfound",water)

    found = False
    for x in waterlight:
        if int(water) >= int(x[1]) and int(water) <= (int(x[1]) + int(x[2])):
            found = True
            light = int(water) + (int(x[0]) - int(x[1]))  
    if not found:
        light = water 
        print(seed,water,"lightnotfound",light)

    found = False
    for x in lighttemp:
        if int(light) >= int(x[1]) and int(light) <= (int(x[1]) + int(x[2])):
            found = True
            temp = int(light) + (int(x[0]) - int(x[1]))
    if not found:
        temp = light 
        print(seed,light,"tempnotfound",temp) 
            #print(seed,soil,fert,water,light,temp)

    found = False
    for x in temphumid:
        if int(temp) >= int(x[1]) and int(temp) <= (int(x[1]) + int(x[2])):
            found = True
            humid = int(temp) + (int(x[0]) - int(x[1]))
    if not found:
        humid = temp
        print(seed,temp,"humidnotfound",humid)

    found = False
    for x in humidloc:
        if int(humid) >= int(x[1]) and int(humid) <= (int(x[1]) + int(x[2])):
            found = True
            loc = int(humid) + (int(x[0]) - int(x[1]))
    if not found:
        loc = humid    
        print(seed,humid,"locnotfound",loc)
    print(seed,soil,fert,water,light,temp,humid,loc)        
    locs.append(loc)


res = 999999999999

for loc in locs:
    if loc < res:
        res = loc

print(res)

file.close()