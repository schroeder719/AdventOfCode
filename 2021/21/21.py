import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())

players = [6,10]
scores = [0,0]

die = 1
roll_count = 0

def roll():
    global die
    global roll_count
    r = die
    die = ((die)%1000)+1
    #print(r)
    roll_count+=1
    return r
    

def roll_dice(count=1):
    ret = 0
    for i in range(count):
        ret += roll()
    return ret

def modulo(a, n, d):
    return a - (n*(np.floor((a-d)/n)))

while max(scores) < 1000:
    for i in range(len(players)):
        players[i] = modulo(players[i]+roll_dice(3),10,1)
        scores[i]+=players[i]
        if scores[i] >= 1000: break
        print(scores)

print(players)
print(scores)
print("{} * {} = {}".format(min(scores),roll_count,int(min(scores)*roll_count)))