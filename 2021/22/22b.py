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
data = u.readfile(u.AOC_2021 + "\\22\\input_ex.txt")
#
offset = 100000
offset = 50
X = 50 + offset
Y = X * (50+offset)

state = {"on":1,"off":0}
points = {}
regex = re.compile("^(on|off) x=([-]?\d+)\.\.([-]?\d+),y=([-]?\d+)\.\.([-]?\d+),z=([-]?\d+)\.\.([-]?\d+)$")
mx = 0
mn = 0
ON_OFF = 0
ON = 1
OFF = 0
X1 = 1
X2 = 2
Y1 = 3
Y2 = 4
Z1 = 5
Z2 = 6


AXIS = ((X1,X2),(Y1,Y2),(Z1,Z2))




steps = []
for d in data:
    r = regex.match(d)
    if not r:
        print("NO MATCH, Exiting!!")
        exit
    
    g = [state[r.groups()[0]]]
    g += [int(x)+offset for x in r.groups()[1:]]
    steps.append(g)

on_regions = []
new_regions = []

def add_new_region(new):
    if not new in new_regions:
        new_regions.append(new)


def handle_new_region(new):
    if new[ON_OFF] == ON:
        if len(on_regions) == 0:
            on_regions.append(new)
        else:
  
            for r in on_regions:
                
                col = False
                # x axis
                if new[X1] < r[X1] and new[X2] > r[X2]: # new region extends both sides of existing region
                    add_new_region([1,r[X2]+1,new[X2],new[Y1],new[Y2],new[Z1],new[Z2]])
                    add_new_region([1,new[X1],r[X1]-1,new[Y1],new[Y2],new[Z1],new[Z2]])
                    col = True
                elif new[X1] >= r[X1] and new[X1] < r[X2] and new[X2] > r[X2]: # lower boundary of new region inside old region
                    add_new_region([1,r[X2]+1,new[X2],new[Y1],new[Y2],new[Z1],new[Z2]])
                    col = True
                elif new[X2] >= r[X1] and new[X2] < r[X2] and new[X1] < r[X1]: # upper boundary of new region inside old region
                    add_new_region([1,new[X1],r[X1]-1,new[Y1],new[Y2],new[Z1],new[Z2]])
                    col = True
                
                # y axis
                if new[Y1] < r[Y1] and new[Y2] > r[Y2]: # new region extends both sides of existing region
                    add_new_region([1,new[X1],new[X2],r[Y2]+1,new[Y2],new[Z1],new[Z2]])
                    add_new_region([1,new[X1],new[X2],new[Y1],r[Y1]-1,r[Z1],r[Z2]])
                    col = True
                elif new[Y1] >= r[Y1] and new[Y1] < r[Y2] and new[Y2] > r[Y2]: # lower boundary of new region inside old region
                    add_new_region([1,new[X1],new[X2],r[Y2]+1,new[Y2],new[Z1],new[Z2]])
                    col = True
                elif new[Y2] >= r[Y1] and new[Y2] < r[Y2] and new[Y1] < r[Y1]: # upper boundary of new region inside old region
                    add_new_region([1,new[X1],new[X2],new[Y1],r[Y1]-1,new[Z1],new[Z2]])
                    col = True

                # z axis
                if new[Z1] < r[Z1] and new[Z2] > r[Z2]: # new region extends both sides of existing region
                    add_new_region([1,new[X1],new[X2],new[Y1],new[Y2],r[Z2]+1,new[Z2]])
                    add_new_region([1,new[X1],new[X2],new[Y1],new[Y2],new[Z1],r[Z1]-1])
                    col = True
                elif new[Z1] >= r[Z1] and new[Z1] < r[Z2] and new[Z2] > r[Z2]: # lower boundary of new region inside old region
                    add_new_region([1,new[X1],new[X2],new[Y1],new[Y2],r[Z2]+1,new[Z2]])
                    col = True
                elif new[Z2] >= r[Z1] and new[Z2] < r[Z2] and new[Z1] < r[Z1]: # upper boundary of new region inside old region
                    add_new_region([1,new[X1],new[X2],new[Y1],new[Y2],new[Z1],r[Z1]-1])
                    col = True
            if not col:

                on_regions.append(new)

    elif new[ON_OFF] == OFF:
        if len(on_regions) == 0:
            pass # nothing to do
        else:
            for r in on_regions:
                col = False
                # x axis
                if new[X1] >= r[X1] and new[X1] < r[X2] and new[X2] >= r[X1] and new[X2] < r[X2]: # off region inside both sides of on region
                    add_new_region([1,r[X1]+1,new[X1],r[Y1],r[Y2],r[Z1],r[Z2]])
                    add_new_region([1,new[X2],r[X2]-1,r[Y1],r[Y2],r[Z1],r[Z2]])
                    col = True
                elif new[X1] >= r[X1] and new[X1] < r[X2] and new[X2] > r[X2]: # lower boundary of off region inside old region
                    add_new_region([1,r[X1]+1,new[X1],r[Y1],r[Y2],r[Z1],r[Z2]])
                    col = True
                elif new[X2] >= r[X1] and new[X2] < r[X2] and new[X1] < r[X1]: # upper boundary of off region inside old region
                    add_new_region([1,new[X2],r[X2]-1,r[Y1],r[Y2],r[Z1],r[Z2]])
                    col = True
                
                # y axis
                if new[Y1] >= r[Y1] and new[Y1] < r[Y2] and new[Y2] >= r[Y1] and new[Y2] < r[Y2]: # off region inside both sides of on region
                    add_new_region([1,r[X1],r[X2],r[Y1]+1,new[Y1],r[Z1],r[Z2]])
                    add_new_region([1,r[X1],r[X2],new[Y2],r[Y2]-1,r[Z1],r[Z2]])
                    col = True
                elif new[Y1] >= r[Y1] and new[Y1] < r[Y2] and new[Y2] > r[Y2]: # lower boundary of off region inside old region
                    add_new_region([1,r[X1],r[X2],r[Y1]+1,new[Y1],r[Z1],r[Z2]])
                    col = True
                elif new[Y2] >= r[Y1] and new[Y2] < r[Y2] and new[Y1] < r[Y1]: # upper boundary of off region inside old region
                    add_new_region([1,r[X1],r[X2],new[Y2],r[Y2]-1,r[Z1],r[Z2]])
                    col = True

                # z axis
                if new[Z1] >= r[Z1] and new[Z1] < r[Z2] and new[Z2] >= r[Z1] and new[Z2] < r[Z2]: # off region inside both sides of on region
                    add_new_region([1,r[X1],r[X2],r[Y1],r[Y2],r[Z1]+1,new[Z1]])
                    add_new_region([1,r[X1],r[X2],r[Y1],r[Y2],new[Z2],r[Z2]-1])
                    col = True
                elif new[Z1] >= r[Z1] and new[Z1] < r[Z2] and new[Z2] > r[Z2]: # lower boundary of off region inside old region
                    add_new_region([1,r[X1],r[X2],r[Y1],r[Y2],r[Z1]+1,new[Z1]])
                    col = True
                elif new[Z2] >= r[Z1] and new[Z2] < r[Z2] and new[Z1] < r[Z1]: # upper boundary of off region inside old region
                    add_new_region([1,r[X1],r[X2],r[Y1],r[Y2],new[Z2],r[Z2]-1])
                    col = True
                if col:
                    on_regions.remove(r)
        
if __name__ == "__main__":

    for s in steps:
        print("***********************************************")
        print("New: {}".format(s))
        add_new_region(s)
        print("New: {}".format(s))
        while len(new_regions) > 0:
            print(len(new_regions))
            new = new_regions.pop()
            
            handle_new_region(new)
    print(len(on_regions))

#print(mx, mn)
# for g in steps:
#     r = regex.match(d)
#     if not r:
#         print("NO MATCH, Exiting!!")
#         exit
    
#     g = [state[r.groups()[0]]]

    
#     for i in range(1,len(g),2):
#         if g[i] < -50:
#             g[i] = -50
#     for i in range(2,len(g),2):
#         if g[i] > 50:
#             g[i] = 50

#     print(r.groups())

#     if g[0]: # on
#         for x in range(g[1]+offset,g[2]+1+offset):
#             for y in range(g[3]+offset,g[4]+1+offset):
#                 for z in range(g[5]+offset,g[6]+1+offset):
#                     if x <= 50 + offset and y <= 50 +offset and z <= 50 +offset and x >= 0 and y >= 0 and z >=0:
#                         num = x + (y * X) + (z * X * Y)
#                         points[num] = 1
#     else:
#         for x in range(g[1]+offset,g[2]+1+offset):
#             for y in range(g[3]+offset,g[4]+1+offset):
#                 for z in range(g[5]+offset,g[6]+1+offset):
#                     if x <= 50 + offset and y <= 50 +offset and z <= 50 +offset:  
#                         num = x + (y * X) + (z * X * Y)
#                         if num in points.keys():
#                             points.pop(num)
#     print(len(points))
    
