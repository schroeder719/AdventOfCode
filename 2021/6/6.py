import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\6\\input.txt",Integer=False)
fish = []
for i in data[0]:
    if i != ',':
        fish.append(int(i))
print(fish)
print("After {} days: {}\n".format(0,len(fish)))
for d in range(256):
    for f in range(len(fish)):
        if fish[f] == 0:
            fish.append(8)
            fish[f] = 6
        else:
            fish[f] -= 1
    if d % 8 == 7:
        print("After {} days: {}\n".format(d,len(fish)))
print("After {} days: {}\n".format(d,len(fish)))
#b = len(fish)        
#total = b**16
#print(total)


