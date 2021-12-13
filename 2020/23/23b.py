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

for i in range(10,1000000+1):
    cups.append(i)

cc = cups[0]
ci = 0

dc = -1
di = -1
l = len(cups)
mx = max(cups)
mn = min(cups)
lof = [0,0,0]
of = [0,0,0]

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
    global l
    pucs = []
    ii = ci+1
    #pucs = [ii,ii+1%l,ii+2%l]
    for i in range(3):
        try:
            pucs.append(cups.pop(ii))
        except IndexError:
            #print("INDEX ERROR!")
            ii = 0
            pucs.append(cups.pop(ii))
    #print("PUCS: {}".format(pucs))
    dc = cc - 1
    while dc < mn or dc in pucs:
        if dc < mn:
            dc = mx
            di = l-1
        else:
            dc-=1
    di = cups.index(dc)
    #print("DC: {}".format(dc))
   
    #display(cups)
    cups[di+1:di+1] = pucs
    while(cups[ci] != cc): # I think cc should have only shifted right by up to 3
        ci +=1
    ci = (ci+1)%(l)
    cc = cups[ci]
    
tic = time.perf_counter()
for i in range (100000):
    #print("-- move {} --".format(i+1))        
    #display(cups)
    move(cups)
    #print("")
    if i % 10000 == 0:
        toc = time.perf_counter()
        chucks_to_go = ((10000000-i)/10000)*(toc-tic)/3600
        print(f"Completed in {toc - tic:0.4f} seconds, about {chucks_to_go:0.4f} remaining")
        print(i)
        tic = time.perf_counter()
    ii = cups.index(1)
    for j in range(3):
        of[j] = cups[ii]
        ii+=1
        if ii >= l:
            ii = 0
    if of != lof:
        print(f"{lof}->{of} at {i}")
        lof = of.copy()


#display(cups)