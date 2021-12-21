import os
import re
from typing import Deque
#import common.util as u
import sys
print(__file__)
sys.path.append(__file__+"../../common")
import numpy as np
#print(os.getcwd())

#data = u.readfile(u.AOC_2021 + "\\12\\input_test.txt",Integer=False)n

conv = {'#':1, ".":0, 0.0:".",1.0:"#",'T':2,2:'T','S':3,3:'S'}

#test
x=(20,30)
y=(-10,-5)

#puzzle
#x=(137,171)
#y=(-98,-73)

x_offset=5
y_offset=50

def pp(pic):
    for row in range(len(pic)):
        for col in range(len(pic[row])):
            char = conv[pic[row,col]]
            print(char,end="")
            
        print("")

#m = np.zeros((200,100))
m = np.zeros((100+y_offset,35+x_offset))
m[abs(y[1])+y_offset:abs(y[0])+y_offset, x[0]+x_offset:x[1]+x_offset] = 2

X = x_offset
Y = y_offset

m[Y,X] = 3
max_x,max_y = 0,0
dx = 6
dy = -9
done = False
while True:
    X+=dx
    Y+=dy
    max_x=max(X,max_x)
    max_y=max(Y,max_y)

    if m[Y,X] != 0:
        done = True
        m[Y,X] = 1
        break
    m[Y,X] = 1

    dy+=1
    if dx > 0:
        dx-=1
    else:
        dx+=1

    
    if X > x[1]+x_offset and Y > y[0]+y_offset:
        break
pp(m)
print("Max x: {}  Max y: {}".format(max_x-x_offset,max_y-y_offset))

