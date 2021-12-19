import os
import re
import common.util as u
import numpy as np
import sys
from collections import deque
#print(os.getcwd())

import math

ID = [sum, math.prod, min, max,
      lambda ls: ls[0], # literal
      lambda ls: 1 if ls[0] > ls[1] else 0,  # gt
      lambda ls: 1 if ls[0] < ls[1] else 0,  # lt
      lambda ls: 1 if ls[0] == ls[1] else 0] # eq


def process(bd):
    global cmds
    #print("==========================================")
    tid = 0
    tver = 0
    i = 0
    ste = 0
    val = 0
     
    ver = int(bd[0:3],2)
    tver += ver
    id = int(bd[3:6],2)
    tid+=id
    i+=6
    print("Version: ",ver)
    print("id: ", id)
    if id == 4:
        vals = [0]
        valstr = ""
        while True:
                v = bd[i+1:i+5]
                valstr += v
                i+=5
                if bd[i-5] == '0':
                    ste = 3
                    vals = [int(valstr,2),]
                    break
                
    else:
        vals = []
        if bd[i] == '0':
            length = int(bd[i+1:i+16],2)
            i+= 16
            end = i + length
            while (i < end):
                t, ni, val = process(bd[i:])
                tver+=t
                i+=ni
                vals.append(val)
        elif bd[i] == '1': # number of subpackets
            num_packets = int(bd[i+1:i+12],2)
            i+=12
            while (num_packets > 0):
                t,ni, val = process(bd[i:])
                tver+=t
                i+=ni
                vals.append(val)
                num_packets-=1
    rv = ID[id](vals)
    return tver, i, rv


if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\16\\input.txt",Integer=False)
    for k in data:
        bd = ""

        if k[0] == '#':
            continue
        for a in k:
            h = int(a,16)
            bd+=format(h,'04b')
        print(k)
        total, i, val = process(bd)
        print("total", total)
        print("value:", val)
        print("***************************************************************************")
        print("***************************************************************************")
# print("Ver: {}".format(ver))
# print("id: {}".format(id))
# print("Value: {}".format(int(val,2)))
