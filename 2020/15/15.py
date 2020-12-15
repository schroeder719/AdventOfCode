import os
import re
import common.util as u
#import common.comp as c
import logging
import time


#data = u.readfile(u.AOC_2020 + "\\15\\input.txt")

data = (1,0,16,5,17,4)
#data = (3,1,2) #1836
def sayGame(n,start):
    said = dict()
    say = 0
    i = 0
    last = 0
    while i < n:
        
        if i < len(start):
            say = start[i]    
        else:
            if last in said.keys():
                t = said[last]
                if len (t) > 1:
                    say = t[-1] - t[-2]
                else:
                    say = 0
                #said[say] = i
            else:
                say = 0
                #said[say] = i
        if say in said.keys():
            t = said[say]
            t.append(i)
            if len(t) > 1:
                t = [t[-2],t[-1]]
            said[say] = t
        else:
            said[say] = [i,]
        last = say
        #print(say, said[say], i)
        if i == n-1:
            print("Turn {}:".format(i+1),end="" )
            #print(said)
            print(say)
        i+=1

toc = time.perf_counter()

#part 1:
tic = time.perf_counter()
sayGame(2020,data)
toc = time.perf_counter()
print(f"Completed in {toc - tic:0.4f} seconds")

#part 2:
tioc = time.perf_counter()
sayGame(30000000,data)
toc = time.perf_counter()
print(f"Completed in {toc - tic:0.4f} seconds")