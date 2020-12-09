import os
import re
import common.util as u
import common.comp as c


data = u.readfile(u.AOC_2020 + "\\8\\input.txt")
tl = 0
for lines in data:
    tl+=1
chg = 0 

comp = c.Computer()

for i in range(0,tl):
    print("i:{}".format(i))
    p = data.copy()
    if "jmp" in p[i]:
        cmd = p[i].split(" ")
        p[i] = 'nop' + " " + cmd[1]
        print(p[i])
        res,acc = comp.load_run(p)
                    
    elif "nop" in p[i]:
        cmd = p[i].split(" ")
        p[i] = 'jmp' + " " + cmd[1]
        print(p[i])
        res,acc = comp.load_run(p)
    else:
        continue

    if res == True:
        print("finished")
        print("acc: {}".format(acc))
        exit(0)
    