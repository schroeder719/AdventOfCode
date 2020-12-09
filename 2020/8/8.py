import os
import re
import common.util as u

def run(data, tl):

    mv = 0
    pc = 0
    acc = 0
    history = []
        #print("total: {}".format(tl))
    while(True):
        #print(history)
        if pc in history:
            print("acc: {}".format(acc))
            return False, 0
        elif pc >= tl:
            print("acc: {}".format(acc))
            return True, acc
        else:
            history.append(pc)
            cmd = data[pc].split(" ")
            d = int(cmd[1])
            #print(cmd)
            if cmd[0] == 'acc':
                acc+= d
                mv = 1
            elif cmd[0] == 'jmp':
                mv = d
            elif cmd[0] == 'nop':
                mv = 1
        pc =  pc + mv
        #print(pc)
    

data = u.readfile(u.AOC_2020 + "\\8\\input.txt")
tl = 0
for lines in data:
    tl+=1
chg = 0 

for i in range(0,tl):
    print("i:{}".format(i))
    p = data.copy()
    if "jmp" in p[i]:
        cmd = p[i].split(" ")
        p[i] = 'nop' + " " + cmd[1]
        print(p[i])
        res,acc = run(p,tl)
                    
    elif "nop" in p[i]:
        cmd = p[i].split(" ")
        p[i] = 'jmp' + " " + cmd[1]
        print(p[i])
        res,acc = run(p,tl)
    else:
        continue

    if res == True:
        print("finished")
        print("acc: {}".format(acc))
        exit(0)
    
