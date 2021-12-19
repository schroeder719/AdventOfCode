import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())

def pp(a):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row,col] == 0:
                print('.', end='')
            else:
                print('#', end='')
        print("")
    print("")

if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\13\\input_a.txt",Integer=False)
    folds = u.readfile(u.AOC_2021 + "\\13\\input_b.txt",Integer=False)
    max_x = 0
    max_y = 0
    coords = []
    for d in data:
        val = d.split(",")
        coords.append([int(val[0]),int(val[1])])
        if int(val[0]) >= max_x:
            max_x = int(val[0]) + 1
        if int(val[1]) >= max_y:
            max_y = int(val[1]) + 1
    print(max_x,max_y)
    a = np.zeros((max_y,max_x))
    for c in coords:
        print(c)
        a[c[1],c[0]] = 1
        
    pp(a)

    for i in range(len(folds)):
        print("step: {}".format(i))
        f = folds[i]
        l = int(f.split('=')[1])
        t = l - 1
        if 'y' in f: # horizontal fold up
            for r in range(l+1,len(a)):
                for c in range(len(a[r])):
                   if a[r,c] == 1:
                       a[t,c] = 1
                t-=1
            a = a[0:l, 0:]
        else: # virtical fold left
            for r in range(len(a)):
                for c in range(l+1,len(a[r])):
                    if a[r,c] == 1:
                        a[r,t] = 1
                    t-=1
                t = l-1
            a = a[0:, 0:l]
        count = np.count_nonzero(a == 1)
        print(count)
        pp(a)
        
            

    exit()

