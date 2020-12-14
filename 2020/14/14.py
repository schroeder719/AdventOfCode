import os
import re
import common.util as u
#import common.comp as c
import logging


data = u.readfile(u.AOC_2020 + "\\14\\input.txt")



# mask = X11001110001101XX01111X1001X01101111
# mem[32163] = 23587
# mem[59015] = 3487205
# mem[25831] = 33360
# mem[62711] = 224797
# mem[41307] = 1818

def maskVal(mask, val):
    print("{} {:X} ".format( mask, val), end="")
    res = 0
    n = [int(x) for x in bin(val)[2:]]
    nn = [0 for x in range(36-len(n))] + n


    #print(len(nn))
    #print(len(mask))
    for i in range(35,-1,-1):
        if mask[i] == 'X':
                if nn[i] == 1:
                    res += 2 ** (35-i)
        elif mask[i] == '1':
            res += 2 ** (35-i)
        elif mask[i] == '0':
            pass
        else:
            print("unexpected")
            exit(1)
    #print(res)
    print(" {:X}".format(res))
    return res

        


def part1(data):
    memory = dict()
    mask = ""
    for line in data:
        maskm = re.match(r"^mask = ([X10]{36})$", line)
        if not maskm:
            mem =  re.match(r"^mem\[([0-9]+)\] = (\d+)$", line)

        if maskm:
            #print("mask: {}".format(maskm.group(1)))
            mask = maskm.group(1)
        elif mem:
            #print("mem: {} = {}".format(mem.group(1), mem.group(2)))
            addr = mem.group(1)
            v = mem.group(2)
            #print(addr,v)
            val = maskVal(mask, int(v))
            memory[addr] = val
        maskm = None
        mem = None
    print(memory)
    sum  = 0
    for key in memory.keys():
        sum+= memory[key]
    print(sum)


def part2(data):
    
    def intToBitArray(intVal):
        n = [x for x in bin(intVal)[2:]]
        nn = ['0' for x in range(36-len(n))] + n
        return nn

    def bitArrayToInt(m):
        """
        docstring
        """
        res = 0
        for b in range(36):
            if m[b] == '1':
                res += 2 ** (35-b)
        return res
    

    def write(mem, mask, ad, val):
        #print("{} {} {:X}".format( mask,ad, val))
        #res = 0
        #n = [int(x) for x in bin(val)[2:]]

        #m = mask
        pl = []
        address = intToBitArray(int(ad))
        m = [char for char in mask] 
        for i in range(len(m)):
            if m[i] == 'X':
                pl.append(i)
                m[i] = '0'
            elif m[i] == '0':
                m[i] = address[i]
                
        for c in range(2 ** len(pl)):
            res = 0
            addr = [x for x in bin(c)[2:]]
            addr.reverse()
            #addr = [0 for x in range(-len(a1))] + a1
            i = 0
            for i in range(len(pl)):
                if i < len(addr):
                    s = len(pl)-i
                    t = pl[s-1]
                    m[t] = addr[i]
                    
                else:
                    break
                
            res = bitArrayToInt(m)
            memory[res] = val
            #print("{:X} = {}".format(res,val))
               
    memory  = dict()
    mask = ""
    for line in data:
        maskm = re.match(r"^mask = ([X10]{36})$", line)
        if not maskm:
            mem =  re.match(r"^mem\[([0-9]+)\] = (\d+)$", line)

        if maskm:
            #print("mask: {}".format(maskm.group(1)))
            mask = maskm.group(1)
        elif mem:
            #print("mem: {} = {}".format(mem.group(1), mem.group(2)))
            addr = mem.group(1)
            v = mem.group(2)
            #print(addr,v)
            write(memory,mask, addr, int(v))
        else:
            print("unexpected 2:" + str(line))
            exit(1)
        maskm = None
        mem = None
    #print(memory)
    sum  = 0
    for key in memory.keys():
        sum+= memory[key]
    print(sum)



# mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
# val = ("41307", 101)
# maskVal(mask,val)



part2(data)
# pl = ['a','b','c']
# for c in range(2 ** len(pl)):
#             print(c)