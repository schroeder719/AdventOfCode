import os
import re
import common.util as u
#import common.comp as c
import logging
import time

data = u.readfile(u.AOC_2020 + "\\13\\input.txt")

# for i in ab:
#     j = int(at/i)
#     k = (at%i)
#     if (i*j)+k == at:
#         print("{} x {} + {} = {}".format(i,j,k,at))
#     else:
#         print("Error")
#     wt.append(at % (i))
def part1():
    at = int(data[0])
    sched = data[1]
    ab = []
    for i in sched.split(','):
        if i not in ['x']:
            ab.append(int(i))
    print(at, ab)
    wt = []
    for i in ab:
        t= 0
        while t <= at:
            t+=i
        wt.append(t - at)
    print(wt)
    for i in range(len(wt)):
        if wt[i] == min(wt):
            print ("{} x {} = {}".format(ab[i],wt[i],ab[i]*wt[i]))
            exit

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def part2():
    at = int(data[0])
    sched = data[1]
    s = sched.split(',')
    ab = []
    for i in s:
        if i not in ['x']:
            ab.append(int(i))
    pos = []
    for i in s:
        if i not in ['x']:
            pos.append(s.index(i))
    diff = []
    for i in range(len(pos)):
        if i == 0:
            diff.append(pos[i])
        else:
            diff.append(pos[i]-pos[i-1])


    for i in ab:
        if is_prime(i):
            pass
        else:
            print("{} is not prime".format(i))

    print(ab, pos,diff)

    wt = []
    

    i = 100000000000000
    #i = 0
    #i = int(s[0])
    found = False

    last_i = 0
    incr = 1
    hi=-1
    while not found:
        j = i
        stack = []
        for b in ab:
            j+= diff[ab.index(b)]
            if j % int(b) == 0:
                if ab.index(b) > hi:
                    hi = ab.index(b)
                    #print("{} % {} == 0".format(j,int(b)))    
                    
                    #print("{}".format(i-last_i))
                    
                    if last_i > 0:
                        incr = incr*ab[hi-1]
                        #print("incr: {}".format(incr))
                    last_i = i
                stack.append("{} % {} == 0".format(j,int(b)))
            else:
                j = 0
                break
        if j == 0:
            i+=incr
        else:
            for s in stack:
                print(s)
            found = True
    print("{}".format(i))
        
#print(1068781%7)
tic = time.perf_counter()
part2()
toc = time.perf_counter()
print(f"Completed in {toc - tic:0.4f} seconds")

