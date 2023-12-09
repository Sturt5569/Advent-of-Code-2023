file = open('Advent of Code 2023/aoc 5 input.txt')

filter = 0
seeds = []
soils = []
ferts = []
waters = []
lights = []
temps = []
hums = []
locs = []

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
        for i in range(1,len(line)):
            if i % 2 == 1:
                seed = [int(line[i]),int(line[i]) + int(line[i+1])-1]
                seeds.append(seed)    
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


def convert_list(list):
    for i in range(len(list)):
        for j in range(3):
            temp = int(list[i][j])
            list[i][j] = temp
    return list
        
seedsoil = convert_list(seedsoil)
soilfert = convert_list(soilfert)
fertwater = convert_list(fertwater)
waterlight = convert_list(waterlight)
lighttemp = convert_list(lighttemp)
temphumid = convert_list(temphumid)
humidloc = convert_list(humidloc)


seedsoil.sort(key= lambda x: x[1])
soilfert.sort(key= lambda x: x[1])
fertwater.sort(key= lambda x: x[1])
waterlight.sort(key= lambda x: x[1])
lighttemp.sort(key= lambda x: x[1])
temphumid.sort(key= lambda x: x[1])
humidloc.sort(key= lambda x: x[1])
seedsoil2 = []
for x in soilfert:
    y = [0,0]
    y[0],y[1] = x[1],x[1]+x[2]
    seedsoil2.append(y)
print(seedsoil2)
#print(seedsoil)
for seed in seeds:
    for x in seedsoil:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if seed[1] < seedsoil[0][1]:
            soils.append(seed)
        elif seed[0] > seedsoil[-1][1]:
            soils.append(seed)
        elif seed[0] >= lran[0] and seed[1] <= lran[1]: # fully in range
            soils.append([seed[0]+lcon,seed[1]+lcon]) 
        elif seed[0] < lran[0] and seed[1] >= lran[0] and seed[1] <= lran[1]: # top half in range
            seeds.append([seed[0],lran[0]-1])
            soils.append([lran[0]+lcon,seed[1]+lcon])
        elif seed[0] < lran[0] and seed[1] > lran[1]:
            seeds.append([seed[0],lran[0]-1])
            seeds.append([lran[1]+1,seed[1]])
            soils.append([lran[0]+lcon,lran[1]+lcon]) 
        elif seed[0] >= lran[0] and seed[0] <= lran[1] and seed[1] > lran[1]: # top half out of range
            soils.append([seed[0]+lcon,lran[1]+lcon])
            seeds.append([lran[1]+1,seed[1]])

soils2 = []
for soil in soils:
    if soil not in soils2:
        soils2.append(soil)
soils = soils2

#---------- run through SOIL to FERT conversion ----------#

for soil in soils:
    for x in soilfert:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if soil[1] < soilfert[0][1]:
            ferts.append(soil)
        elif soil[0] > soilfert[-1][1]:
            ferts.append(soil)
        elif soil[0] >= lran[0] and soil[1] <= lran[1]: # fully in range
            ferts.append([soil[0]+lcon,soil[1]+lcon]) 
        elif soil[0] < lran[0] and soil[1] >= lran[0] and soil[1] <= lran[1]: # top half in range
            soils.append([soil[0],lran[0]-1])
            ferts.append([lran[0]+lcon,soil[1]+lcon])
        elif soil[0] < lran[0] and soil[1] > lran[1]:
            soils.append([soil[0],lran[0]-1])
            soils.append([lran[1]+1,soil[1]])
            ferts.append([lran[0]+lcon,lran[1]+lcon]) 
        elif soil[0] >= lran[0] and soil[0] <= lran[1] and soil[1] > lran[1]: # top half out of range
            ferts.append([soil[0]+lcon,lran[1]+lcon])
            soils.append([lran[1]+1,soil[1]])

ferts2 = []
for fert in ferts:
    if fert not in ferts2:
        ferts2.append(fert)
ferts = ferts2

#---------- run through FERT to WATER conversion ----------#

for fert in ferts:
    for x in fertwater:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if fert[1] < fertwater[0][1]:
            waters.append(fert)
        elif fert[0] > fertwater[-1][1]:
            waters.append(fert)
        elif fert[0] >= lran[0] and fert[1] <= lran[1]: # fully in range
            waters.append([fert[0]+lcon,fert[1]+lcon]) 
        elif fert[0] < lran[0] and fert[1] >= lran[0] and fert[1] <= lran[1]: # top half in range
            ferts.append([fert[0],lran[0]-1])
            waters.append([lran[0]+lcon,fert[1]+lcon])
        elif fert[0] < lran[0] and fert[1] > lran[1]:
            ferts.append([fert[0],lran[0]-1])
            ferts.append([lran[1]+1,fert[1]])
            waters.append([lran[0]+lcon,lran[1]+lcon]) 
        elif fert[0] >= lran[0] and fert[0] <= lran[1] and fert[1] > lran[1]: # top half out of range
            waters.append([fert[0]+lcon,lran[1]+lcon])
            ferts.append([lran[1]+1,fert[1]])

waters2 = []
for water in waters:
    if water not in waters2:
        waters2.append(water)
waters = waters2

#---------- run through WATER to LIGHT conversion ----------#

for water in waters:
    for x in waterlight:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if water[1] < waterlight[0][1]:
            lights.append(water)
        elif water[0] > waterlight[-1][1]:
            lights.append(water)
        elif water[0] >= lran[0] and water[1] <= lran[1]: # fully in range
            lights.append([water[0]+lcon,water[1]+lcon]) 
        elif water[0] < lran[0] and water[1] >= lran[0] and water[1] <= lran[1]: # top half in range
            waters.append([water[0],lran[0]-1])
            lights.append([lran[0]+lcon,water[1]+lcon])
        elif water[0] < lran[0] and water[1] > lran[1]:
            waters.append([water[0],lran[0]-1])
            waters.append([lran[1]+1,water[1]])
            lights.append([lran[0]+lcon,lran[1]+lcon]) 
        elif water[0] >= lran[0] and water[0] <= lran[1] and water[1] > lran[1]: # top half out of range
            lights.append([water[0]+lcon,lran[1]+lcon])
            waters.append([lran[1]+1,water[1]])

lights2 = []
for light in lights:
    if light not in lights2:
        lights2.append(light)
lights = lights2

#---------- run through LIGHT to TEMP conversion ----------#

for light in lights:
    for x in lighttemp:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if light[1] < lighttemp[0][1]:
            temps.append(light)
        elif light[0] > lighttemp[-1][1]:
            temps.append(light)
        elif light[0] >= lran[0] and light[1] <= lran[1]: # fully in range
            temps.append([light[0]+lcon,light[1]+lcon]) 
        elif light[0] < lran[0] and light[1] >= lran[0] and light[1] <= lran[1]: # top half in range
            lights.append([light[0],lran[0]-1])
            temps.append([lran[0]+lcon,light[1]+lcon])
        elif light[0] < lran[0] and light[1] > lran[1]:
            lights.append([light[0],lran[0]-1])
            lights.append([lran[1]+1,light[1]])
            temps.append([lran[0]+lcon,lran[1]+lcon]) 
        elif light[0] >= lran[0] and light[0] <= lran[1] and light[1] > lran[1]: # top half out of range
            temps.append([light[0]+lcon,lran[1]+lcon])
            lights.append([lran[1]+1,light[1]])

temps2 = []
for temp in temps:
    if temp not in temps2:
        temps2.append(temp)
temps = temps2

#---------- run through TEMP to HUMID conversion ----------#

for temp in temps:
    for x in temphumid:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if temp[1] < temphumid[0][1]:
            hums.append(temp)
        elif temp[0] > temphumid[-1][1]:
            hums.append(temp)
        elif temp[0] >= lran[0] and temp[1] <= lran[1]: # fully in range
            hums.append([temp[0]+lcon,temp[1]+lcon]) 
        elif temp[0] < lran[0] and temp[1] >= lran[0] and temp[1] <= lran[1]: # top half in range
            temps.append([temp[0],lran[0]-1])
            hums.append([lran[0]+lcon,temp[1]+lcon])
        elif temp[0] < lran[0] and temp[1] > lran[1]:
            temps.append([temp[0],lran[0]-1])
            temps.append([lran[1]+1,temp[1]])
            hums.append([lran[0]+lcon,lran[1]+lcon]) 
        elif temp[0] >= lran[0] and temp[0] <= lran[1] and temp[1] > lran[1]: # top half out of range
            hums.append([temp[0]+lcon,lran[1]+lcon])
            temps.append([lran[1]+1,temp[1]])

hums2 = []
for hum in hums:
    if hum not in hums2:
        hums2.append(hum)
hums = hums2
print(len(hums))

#---------- run through HUMID to LOCATION conversion ----------#

for hum in hums:
    for x in humidloc:
        lran = (x[1],x[1]+x[2]-1)
        lcon= x[0] - x[1]
        if hum[1] < humidloc[0][1]:
            locs.append(hum)
        elif hum[0] > humidloc[-1][1]:
            locs.append(hum)
        elif hum[0] >= lran[0] and hum[1] <= lran[1]: # fully in range
            locs.append([hum[0]+lcon,hum[1]+lcon]) 
        elif hum[0] < lran[0] and hum[1] >= lran[0] and hum[1] <= lran[1]: # top half in range
            hums.append([hum[0],lran[0]-1])
            locs.append([lran[0]+lcon,hum[1]+lcon])
        elif hum[0] < lran[0] and hum[1] > lran[1]:
            hums.append([hum[0],lran[0]-1])
            hums.append([lran[1]+1,hum[1]])
            locs.append([lran[0]+lcon,lran[1]+lcon]) 
        elif hum[0] >= lran[0] and hum[0] <= lran[1] and hum[1] > lran[1]: # top half out of range
            locs.append([hum[0]+lcon,lran[1]+lcon])
            hums.append([lran[1]+1,hum[1]])

locs2 = []
for loc in locs:
    if loc not in locs2:
        locs2.append(loc)
locs = locs2
print(len(locs))
res = 9999999999
for loc in locs:
    if loc[0] < res:
        res = loc[0]
print("Result is", res)
file.close()