import os
import re
import common.util as u
#import common.comp as c
import logging


data = u.readfile(u.AOC_2020 + "\\10\\input.txt")
#print(data)

for i in range(0,len(data)):
    data[i] = int(data[i])
print(max(data))
data.append(max(data)+3)
data.append(0)
data.sort()
print(data)




def fact(i):
    total = 1
    while i> 0:
        total= total * i
        i-=1
    return total

# def comp(n,r):
#     fact(n)/fact(n-r)

def comp2(n,r):
    return fact(n)/(fact(r) * fact(n-r))


def comp(n):
    total = fact(n) # choose all
    r = n - 1
    while r > 0:
        t = comp2(n,r)
        total += t
        #print(r,t,total)
        r-=1
    return total

def part1():
    a = 0
    b = 0
    for i in range(1,len(data)):
        if data[i] - data[i-1] == 1:
            a+=1
        elif data[i] - data[i-1] == 3:
            b+=1
        else:
            print("not sure: {} {}".format(i,data[i]))

def findlocked():
    locked = [0 for i in range(0,len(data))] 
    locked[0] = 1
    i = 1
    while i < len(data) - 1:
        if data[i+1] - data[i] == 1:
            #locked.append(0)
            i+=1
        elif data[i+1] - data[i] == 3:
            locked[i] = 1
            locked[i+1] = 1
            i+=1
        else:
            print("not sure: {} {}".format(i,data[i]))
    #locked.append(1)

    if len(data) != len(locked):
        print("locked issue")
        print("{} != {}".format(len(data), len(locked)))
        #exit(1)

    return locked


def part2():
    lst = []
    #for i in  range(0,len(data)):
    i = 0
    while (i < len(data)-1):

        count = 0
        for j in range(i+1,len(data)-1):
            #print(i,j)
            if data[j] <= data[i] + 3:
                count+=1
            if data[j] > data[i] + 3:
                break
        lst.append(comp(count))
        print(count)
        if count > 0:
            i+=count
        else:
            i+=1
    print(lst)
    total = 1
    for i in lst:
        total = total * i
    print(total)

def c(n):
    if n > 3:
        return pow(2,n) - (pow(2,n-3) - 1)
    else:
        return pow(2,n) - 1 

def part2a(data,locked):
    i = 1
    sum = 0
    lst = []
    last_locked = 0
    while i < len(data)-1:
        if locked[i] == 1:
            #  and sum > 0:
            #     sum+=1
            
            if sum > 0:
                print("{} {} == {}".format(data[i],data[last_locked],data[i]-data[last_locked]))
                if data[i] - data[last_locked] <= 3:
                    lst.append(c(sum)+1)
                else:
                    lst.append(c(sum))
            last_locked = i
            i+=1
            sum = 0

        else:
            sum+=1
            i+=1
    print(lst)
    total = 1
    for i in lst:
        total = total * i
    print(total)

#print(len(data))
#print(comp(len(data)))
locked = findlocked()
#print(data)
for i in range(0,len(data)):
    if locked[i] == 1:
        print("({:02}) ".format(data[i]), end="")
    else:
        print("{:02} ".format(data[i]), end="")
print("")
# for i in locked:
#     print("{:02} ".format(i), end="")
# print("")
#comp(3)
part2a(data,locked)