import os
import re
from sre_constants import GROUPREF
import common.util as u
#import common.comp as c
import logging
import time
import copy
import numpy as np

#data = u.readfile(u.AOC_2020 + "\\17\\input.txt")
data = u.readfile(u.AOC_2021 + "\\22\\input.txt")
#
offset = 100000
X = 50 + offset
Y = X * (50+offset)

state = {"on":1,"off":0}
points = {}
regex = re.compile("^(on|off) x=([-]?\d+)\.\.([-]?\d+),y=([-]?\d+)\.\.([-]?\d+),z=([-]?\d+)\.\.([-]?\d+)$")
mx = 0
mn = 0

steps = []
for d in data:
    r = regex.match(d)
    if not r:
        print("NO MATCH, Exiting!!")
        exit
    
    g = [state[r.groups()[0]]]
    g += [int(x) for x in r.groups()[1:]]
    mn = min(min(g),mn)
    mx = max(max(g),mx)
    steps.append(g)
print(mx, mn)
for g in steps:
    r = regex.match(d)
    if not r:
        print("NO MATCH, Exiting!!")
        exit
    
    g = [state[r.groups()[0]]]

    
    for i in range(1,len(g),2):
        if g[i] < -50:
            g[i] = -50
    for i in range(2,len(g),2):
        if g[i] > 50:
            g[i] = 50

    print(r.groups())

    if g[0]: # on
        for x in range(g[1]+offset,g[2]+1+offset):
            for y in range(g[3]+offset,g[4]+1+offset):
                for z in range(g[5]+offset,g[6]+1+offset):
                    if x <= 50 + offset and y <= 50 +offset and z <= 50 +offset and x >= 0 and y >= 0 and z >=0:
                        num = x + (y * X) + (z * X * Y)
                        points[num] = 1
    else:
        for x in range(g[1]+offset,g[2]+1+offset):
            for y in range(g[3]+offset,g[4]+1+offset):
                for z in range(g[5]+offset,g[6]+1+offset):
                    if x <= 50 + offset and y <= 50 +offset and z <= 50 +offset:  
                        num = x + (y * X) + (z * X * Y)
                        if num in points.keys():
                            points.pop(num)
    print(len(points))
    
