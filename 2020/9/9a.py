import os
import re
import common.util as u
import common.comp as c
import logging


data = u.readfile(u.AOC_2020 + "\\9\\input.txt")
tl = 0
for lines in data:
    tl+=1
chg = 0 

comp = c.Computer()

def test(i):
    for j in range(i-25,i):
        for k in range(i-24,i):
            if (i != j):
                print("{} {}, {}+{}={}".format(j,k,data[j],data[k],data[j]+data[k]))
                if int(data[j])+int(data[k]) == int(data[i]):
                    return True
    return False
def part1():
    for i in range(25,len(data)):
        print(data[i])
        if test(i) == False:
            print("no match: {}".format(data[i]))
            exit()

def part2():
    found = False
    target = 1639024365
    i = 651
    while not found:
        i-=1
        print(i)
        total = int(data[i])
        j = i

        while (total < target and j >0):
            j-=1
            total += int(data[j])
            
        
        if total == target:
            print("total: {} target: {}".format(total,target))
            found = True
            print("{},{}".format(i,j))
            t = 0
            mn = target
            mx = 0
            for l in range(j,i+1):
                a = int(data[l])
                t += a
                if a > mx:
                    mx = a
                if a < mn:
                    mn = a
            print(t)
            print("{}+{}={}".format(mn,mx, mx+mn))

part2()




    