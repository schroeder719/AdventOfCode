import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\10\\input.txt",Integer=False)

points = { 
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
pair = { 
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}
total = 0
for row in data:
    stack = deque()
    for c in row:
        if c in ['(','[','{', '<']:
            stack.append(c)
        elif c in [')',']','}', '>']:
            #print(stack)
            v = stack.pop()
            if v != pair[c]:
                #invalid
                print(c)
                total+=points[c]
                break
        else:
            print("error")
print(total)
