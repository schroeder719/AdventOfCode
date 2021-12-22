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

test = [(23,-10),(25,-9),(27,-5),(29,-6),(22,-6),(21,-7),(9,0),(27,-7),(24,-5),(25,-7),(26,-6),(25,-5),(6,8),(11,-2),(20,-5),(29,-10),(6,3),(28,-7),(8,0),(30,-6),(29,-8),(20,-10),(6,7),(6,4),(6,1),(14,-4),(21,-6),(26,-10),(7,-1),(7,7),(8,-1),(21,-9),(6,2),(20,-7),(30,-10),(14,-3),(20,-8),(13,-2),(7,3),(28,-8),(29,-9),(15,-3),(22,-5),(26,-8),(25,-8),(25,-6),(15,-4),(9,-2),(15,-2),(12,-2),(28,-9),(12,-3),(24,-6),(23,-7),(25,-10),(7,8),(11,-3),(26,-7),(7,1),(23,-9),(6,0),(22,-10),(27,-6),(8,1),(22,-8),(13,-4),(7,6),(28,-6),(11,-4),(12,-4),(26,-9),(7,4),(24,-10),(23,-8),(30,-8),(7,0),(9,-1),(10,-1),(26,-5),(22,-9),(6,5),(7,5),(23,-6),(28,-10),(10,-2),(11,-1),(20,-9),(14,-2),(29,-7),(13,-3),(23,-5),(24,-8),(27,-9),(30,-7),(28,-5),(21,-10),(7,9),(6,6),(21,-5),(27,-10),(7,2),(30,-9),(21,-8),(22,-7),(24,-9),(20,-6),(6,9),(29,-5),(8,-2),(27,-8),(30,-5),(24,-7)]

#test
# X=(20,30)
# Y=(-10,-5)

#puzzle
X=(137,171)
Y=(-98,-73)

x_offset=5
y_offset=125

def pp(pic,file=None):
    for row in range(len(pic)):
        line=""
        for col in range(len(pic[row])):
            char = conv[pic[row,col]]
            line+=char
            #print(char,end="")
            
        print(line)
        if file:
            file.write(line)



def run(dx=6,dy=9, m=None):
    global x_offset,y_offset    
    max_x,max_y = 0,0
    x = 0
    y = 0
    while True:
        x+=dx
        y+=dy
        max_x=max(x,max_x)
        max_y=max(y,max_y)

        #print(x,y)
        if m is not None:
            m[(-y+y_offset),x+x_offset] = 1
        if x >= X[0] and x <= X[1] and y >= Y[0] and y <= Y[1]:
            # if ph:
            #     print("hit: {},{}".format(x,y))
            return True, max_x,max_y

        dy-=1
        if dx > 0:
            dx-=1
        elif dx <0:
            dx+=1

        if (x > X[1] and y < Y[0]) or (dx == 0 and y < Y[0]):
            return False,0,0

m = np.zeros((150,100))
m[0+y_offset,0+x_offset] = 3
m[-Y[1]+y_offset:-Y[0]+y_offset+1, X[0]+x_offset:X[1]+x_offset+1] = 2
# run(9,0,m)
# pp(m)
################################################
max_h = 0
count = 0
hits = []

for dx in range(0,300):
    for dy in range(-300,300):
        if dx == 0 and dy == 0:
            continue
        #n = m.copy()
        #print("try: {},{}".format(dx,dy))
        hit, max_x, max_y = run(dx,dy)
        if hit:
            #print("dx,dy: {},{}".format(dx,dy))
            #hits.append((dx,dy))
            count+=1
            #print("Max x: {}  Max y: {}".format(max_x,max_y))
            max_h = max(max_y,max_h)

print(count)
#print(hits)
#############################################





# with open(os.path.join(dir_path,"map.txt"),"w") as f:
#     pp(max_map,f)
# print(max_h)

# test_s= set(test)
# hits_s = set(hits)

# missing = test_s.difference(hits_s)
# for g in missing:
#     n = m.copy()
#     run(g[0],g[1],n)
#     pp(n)

# n = m.copy()
# run(9,0,n)
# pp(n)
#test.sort(key=lambda x: x[0])
#print(test)
# rem = list(range(len(test)))
# print(rem)
# for i in hits:
#     for j in range(len(test)):
#         if i[0] == test[j][0] and i[1] == test[j][1]:
#             #print(j)
#             rem.remove(j)
# print(rem)
# for k in rem:
#     print(test[k])

     
#print("Max y: {} hits: {}".format(max_h,count))


