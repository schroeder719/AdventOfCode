import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math
import queue


#cups = [ int(x) for x in "389125467" ]
cups = [ int(x) for x in "389547612" ]


cc = cups[0]
ci = cups.index(cc)

dc = -1
di = -1
l = len(cups)
sl = l-3
mx = max(cups)
mn = min(cups)

def display(cups):
    for i in range(len(cups)):
        if i == ci:
            print("({}) ".format(cups[i]), end="")
        elif i == di:
            print("[{}] ".format(cups[i]), end="")
        elif i == len(cups)-1:
            print("{}".format(cups[i]))
        else:
            print("{} ".format(cups[i]), end="")

def move(cups):
    global cc
    global dc
    global mn
    global di
    global ci
    pucs = []
    ii = ci+1
    for i in range(3):
        if ii >= len(cups):
            ii = 0
        pucs.append(cups.pop(ii))
    print("PUCS: {}".format(pucs))
    dc = cc - 1
    while not dc in cups:
        if dc < mn:
            dc = mx
        else:
            dc-=1
    print("DC: {}".format(dc))
    di = cups.index(dc)
    display(cups)
    cups[di+1:di+1] = pucs
    ci = cups.index(cc)
    ci = (ci+1)%(l)
    cc = cups[ci]
    

for i in range (100):
    print("-- move {} --".format(i+1))        
    display(cups)
    move(cups)
    print("")
display(cups)



