import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math
import queue


#data = u.readfile(u.AOC_2020 + "\\22\\input_ex.txt")
data = u.readfile(u.AOC_2020 + "\\22\\input.txt")

card_pk = 12320657
door_pk = 9659666
subject_num = 7

def transform(loop_size):
    value = 1
    for i in range(loop_size):
        value = value*subject_num
        value = value % 20201227
    return value

done = False
i = 1
while not done:
    if transform(i) == card_pk:
        print(f"Card loop size: {i}")
        done = True
    i+=1
done = False
i=1
while not done:
    if transform(i) == door_pk:
        print(f"Door loop size: {i}")
        done = True
    i+=7
print("done")



cd 