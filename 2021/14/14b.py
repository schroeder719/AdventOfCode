import os
import re
import common.util as u
import numpy as np
import sys
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
    data = u.readfile(u.AOC_2021 + "\\14\\input_test.txt",Integer=False)

    rules = { }
    rules2 = { }


    pt = data[0]
    pt = "NN"
    for i in range(2,len(data)):
        r = data[i].split(' ')
        k = r[0]
        v = r[-1]
        rules[k] = v
    print(rules)

    d = deque()
    for p in pt:
        d.append(p)
    i = 0
    
    for step in range(40):
        new_k = "".join(d)
        print(step)
        done = False
        while not done:
            found = False
            if i + 1 == len(d):
                done = True
            else:            
                #print(d[i])
                # dstr = "".join(d)
                # dstr = dstr[i:]
                # for k in sorted(rules2, key=lambda k: len(rules2[k])):
                #     if dstr.startswith(k):
                #         for c in len(k):
                #             d.remove(i)
                #         for c in rules2[k]:
                #             d.insert(i+1,c)
                #             i+=1        
                #         found = True
                #         break
                if not found:
                    k = d[i] + d[i+1]
                    v = rules[k]
                    if v:
                        d.insert(i+1,rules[k])
                        i+=1
                    i+=1
        new_val = "".join(d)
        rules2[new_k] = new_val
        i = 0

    #done, so count it out
    
    count = {}
    for i in d:
        if i in count.keys():
            count[i] = count[i]+1
        else:
            count[i] = 1
    min = sys.maxsize
    max = 0
    for i, (j,k) in enumerate(count.items()):
        if k < min:
            min = k
        elif k > max:
            max = k
    print("{} - {} = {}".format(max,min,max-min))
    