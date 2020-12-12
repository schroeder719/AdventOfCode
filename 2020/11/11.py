import os
import re
import common.util as u
#import common.comp as c
import logging


data = u.readfile(u.AOC_2020 + "\\11\\input.txt")
#print(data)

def count(data):
    empty= 0
    occupied = 0
    floor = 0
    for r in data:
        for c in r:
            if c == 'L':
                empty+=1
            elif c == '#':
                occupied+=1
            elif c == ".":
                floor+=1
    return (empty, occupied, floor, empty+occupied+floor)

#return true if a seat is occupied
def status1(data,r,c):   
    if data[r][c] == '.':
        return '.'
    count = 0
    for i in range(r-1,r+2):
        for j in range(c-1,c+2):
            try:
                if i >= 0 and j >= 0:
                    #print("{},{}={}".format(i,j,data[i][j]))
                    if i == r and j == c:
                        pass
                    else:
                        if data[i][j] == '#':
                            count+=1
            except IndexError:
                pass
    if count == 0 and data[r][c] == 'L':
        return '#'
    elif count >= 4 and data[r][c] == '#':
        return 'L'
    return data[r][c]

def status2(data,r,c):   
    if data[r][c] == '.':
        return '.'
    count = 0
    dirs = [(-1,-1),(-1,0),(-1,1),
            (0,-1),        (0,1),
            (1,-1),(1,0),(1,1)]
    count = 0
    for dr in dirs:
        res,ch = check(data,dr,r,c)
        if res and ch == '#':
            count+=1

    if count == 0 and data[r][c] == 'L':
        return '#'
    elif count >= 5 and data[r][c] == '#':
        return 'L'
    return data[r][c]

def check(data,dr,rr,cc):
    f = '.'
    r = rr
    c = cc
    while f == '.':
        r += dr[0]
        c += dr[1]
        try:
            if r < 0 or c < 0 :
                return False,''
            else:
                f = data[r][c]
                
        except IndexError:
            return False,''
    return True,f

def round(data,func):
    nd = []
    for r in range(0, len(data)):
        new = ""
        for c in range(0,len(data[0])):
            new += func(data,r,c)
        nd.append(new)
        
    return nd

def prt(data):
    for r in data:
        for c in r:
            print(c,end="")
        print("")
    print("")

def part1():
    #print(count(data))
    #prt(data)
    done = False
    res = []
    new = data.copy()
    while not done:
        #prt(new)
        new = round(new, status1)
        res.append(count(new))
        #print(res)
        if len(res) > 2:
            if res[-2][1] == res[-1][1]:
                print("{}=={}".format(res[-2][1],res[-1][1]))
                done = True
    prt(new)
def part2():
    #print(count(data))
    #prt(data)
    done = False
    res = []
    new = data.copy()
    while not done:
        #prt(new)
        new = round(new, status2)
        res.append(count(new))
        #print(res)
        if len(res) > 2:
            if res[-2][1] == res[-1][1]:
                print("{}=={}".format(res[-2][1],res[-1][1]))
                done = True
    prt(new)

part2()