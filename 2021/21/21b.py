from functools import lru_cache
import os
import re
import common.util as u
from itertools import product
import numpy as np
from copy import copy,deepcopy
from collections import deque,Counter
from typing import Tuple
#print(os.getcwd())


start = [6,10] #player
sums = Counter(sum(rolls) for rolls in product((1,2,3), repeat=3))
rules = [3, 21, 10]


next_place = []
for i in range(0,rules[2]+1):
    rolls = [0]*10
    for r,t in sums.items():
        x = i+r - (rules[2]*(np.floor((i+r-1)/rules[2])))
        rolls[r] = int(x)
    next_place.append(rolls)
next_place = tuple(next_place)

@lru_cache(maxsize=None)
def play(p1:int, p2:int, p1s:int, p2s:int, turn) -> Tuple[int,int]:
    global sums
    global rules
    global next_place

    if p1s >= rules[1]: 
        return (1,0)
    if p2s >= rules[1]: 
        return (0,1) 
    
    wins = [0,0]

    for r,t in sums.items():
        if turn == 0:
            p1_t =  next_place[p1][r]
            p1s_t  = p1s + p1_t
            #play the other person
            w = play(p1_t,p2,p1s_t,p2s,1)
        else:
            p2_t =  next_place[p2][r]
            p2s_t  = p2s + p2_t
            w = play(p1,p2_t,p1s,p2s_t,0)

        wins[0] += w[0] * t
        wins[1] += w[1] * t
    return wins

total_wins = play(start[0],start[1],0,0,0)
print(total_wins)
print("answer: ",max(total_wins))
# print(scores)
# print("{} * {} = {}".format(min(scores),roll_count,int(min(scores)*roll_count)))