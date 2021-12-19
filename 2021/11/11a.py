import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())


def increase(a, v=1):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row,col] >= 0:
                a[row,col] +=1
    return a

def flash(g):
    rtn = False
    for row in range(len(a)):
        if row == 0:
            t=0
            b=2
        elif row == len(a)-1:
            t=1
            b=1
        else:
            t=1
            b=2
            

        for col in range(len(a[row])):
            if col == 0:
                l = 0
                r = 2
            elif col == len(a[row])-1:            
                l = 1
                r = 1
            else:
                l = 1
                r = 2

            if g[row,col] > 9:
                local = g[(row-t):(row+b), (col-l):(col+r)]
                increase(local)
                g[row,col] = -1
                rtn = True

    return rtn

def reset(a,counter):
    round_counter = 0
    for row in range(len(a)):
        for col in range(len(data[row])):
            if a[row,col] == -1:
                a[row,col] = 0
                round_counter+=1
    counter+=round_counter
    return a,counter,round_counter

if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\11\\input.txt",Integer=False)

    for i in range(len(data)):
        t = []
        for j in range(len(data[i])):
            t.append(int(data[i][j]))
        data[i] = t
    a = np.array(data)
    # f = a.copy()
    # f.fill(1)
    # print(f)    
    counter = 0
    print(a)
    for s in range(1000):
        #print(s)
        #step 1
        increase(a)
        #print(a)
        #step 2
        while flash(a): pass
            #print(a)
        #step 3
        a, counter,rc = reset(a,counter)
        if rc == 100:
            print("sync round: {}".format(s+1))
            break
    print(a)
    print(counter)
        #print(" X ")
        #print(a[r][c])
        # if a[(row-t):(row+b), (col-l):(col+r)].min() == a[row,col]:
        #     print(a[row,col])
        #     risk+= a[row,col]+1
        #     low_points.append([row,col])