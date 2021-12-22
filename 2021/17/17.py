import os
import re
from typing import Deque
#import common.util as u
import sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path+"../../common")
import numpy as np
#print(os.getcwd())

#data = u.readfile(u.AOC_2021 + "\\12\\input_test.txt",Integer=False)n

conv = {'#':1, ".":0, 0.0:".",1.0:"#",'T':2,2:'T','S':3,3:'S'}

#test
#x=(20,30)
#y=(-10,-5)

#puzzle
x=(137,171)
y=(-98,-73)

x_offset=5
y_offset=10000

def pp(pic,file):
    for row in range(len(pic)):
        line=""
        for col in range(len(pic[row])):
            char = conv[pic[row,col]]
            line+=char
            #print(char,end="")
            
        print(line)
        if file:
            file.write(line)


#m = np.zeros((200,100))

def run(dx,dy,m,x_offset,y_offset):
    
    X = x_offset
    Y = y_offset

    m[Y,X] = 3 #mark the start
    max_x,max_y = 0,0
    while True:
        X+=dx
        Y+=dy
        max_x=max((X-x_offset),max_x)
        max_y=max(-(Y-y_offset),max_y)

        if m[Y,X] == 2:
            m[Y,X] = 1
            return True,(max_x,max_y),m
        m[Y,X] = 1
        #print("{},{}".format(Y-y_offset,X-x_offset))

        dy+=1
        if dx > 0:
            dx-=1
        else:
            dx+=1

        
        if X > x[1]+x_offset or -(Y-y_offset) < y[0]:
            return False,max,m 
    #pp(m)
    print("Max x: {}  Max y: {}".format(max_x,max_y))

m = np.zeros((1000+y_offset,300+x_offset))
m[abs(y[1])+y_offset:abs(y[0])+y_offset+1, x[0]+x_offset:x[1]+x_offset+1] = 2
max_h = 0
for xx in range(10):
    for yy in range(-200,0):
        hit, maxv, n = run(xx,yy,m.copy(),x_offset,y_offset)
        if hit:
            print("Max x: {}  Max y: {}".format(maxv[0],maxv[1]))
            if maxv[1] > max_h:
                max_h = maxv[1]
                max_map = n.copy()
with open(os.path.join(dir_path,"map.txt"),"w") as f:
    pp(max_map,f)
print(max_h)

