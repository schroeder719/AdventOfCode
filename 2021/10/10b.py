import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\10\\input.txt",Integer=False)

points = { 
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
pair = { 
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

scores = []
for row in data:
    total = 0
    stack = deque()
    for c in row:
        if c in ['(','[','{', '<']:
            stack.append(c)
        elif c in [')',']','}', '>']:
            #print(stack)
            v = stack.pop()
            if v != pair[c]:
                #invalid
                #print(c)
                #total+=points[c]
                stack = []
                break
        else:
            print("error")
    while(len(stack) > 0):
        v = stack.pop()
        total*=5
        total+=points[pair[v]]
    #print(total)
    if total > 0:
        scores.append(total)
scores.sort()
print(scores)
i = int(len(scores)/2)

print("SCORE:")
print(scores[i])
