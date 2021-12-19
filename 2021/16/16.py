import os
import re
import common.util as u
import numpy as np
import sys
from collections import deque
#print(os.getcwd())

if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\16\\input.txt",Integer=False)


ste = 0
bd = ""
for a in data[0]:
    h = int(a,16)
    bd+=format(h,'04b')

print(bd)

func_table = [sum,None,min,max,gt,lt]

def process(bd, num_packets=-1, func=None):
    tid = 0
    tver = 0
    i = 0
    np = num_packets
    ste = 0
    while i <= len(bd):
        if i == len(bd) and ste != 3:
            break
        if ste == 0: # version
            val = ""
            ver = int(bd[i:i+3],2)
            tver += ver
            #print(ver)

            i+=3
            ste = 1
        elif ste == 1: # id
            id = int(bd[i:i+3],2)
            tid+=id
            if id == 4:
                ste = 2
            else:
                ste = 4
            i+=3
        elif ste == 2: #lit val
            v = bd[i+1:i+5]
            #print(v)
            val += v
            if bd[i] == '0':
                ste = 3
            i+=5
        elif ste == 3:
            #print(val)
            print("Ver: {}".format(ver))
            print("id: {}".format(id))
            print("Value: {}".format(int(val,2)))
            if np > 0:
                np-=1
            if np == 0:
                return tver,i
            ste = 0
        elif ste == 4: # ID BIT
            id_bit= bd[i]
            if id_bit == '0':
                ste = 5
            else:
                ste = 6
            i+=1
        elif ste == 5: #total length in bits
            length = int(bd[i:i+15],2)
            i+= 15
            t, ni = process(bd[i:i+length])
            tver+=t
            i+=ni
            ste = 0
        elif ste == 6: # number of subpackets
            num_packets = int(bd[i:i+11],2)
            i+=11
            t,ni = process(bd[i:],num_packets)
            tver+=t
            i+=ni
            ste = 0

    return tver, i
total, i = process(bd)
print(total)
# print(val)
# print("Ver: {}".format(ver))
# print("id: {}".format(id))
# print("Value: {}".format(int(val,2)))
