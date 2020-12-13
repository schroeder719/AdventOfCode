import os
import re
import common.util as u
#import common.comp as c
import logging


data = u.readfile(u.AOC_2020 + "\\12\\input.txt")

def run(data):

    x = 0
    y = 0
    d = 0
    
    trns = {0:'E', 90: 'N', 180:'W', 270:'S'  } 

    def move(a,v,x,y):
        if a == 'N' :
            y+= v
        elif a == 'W' :
            x-= v
        elif a == 'S' :
            y-= v
        elif a == 'E' :
            x+= v
        return x,y
        #print("total: {}".format(tl))
    def turn(d,a,v):
        if a == 'L':
            d+=v
        elif a == 'R':
            d-=v
        
        if d == -90:
            d = 270
        if d == -180:
            d = 180
        if d == -270:
            d = 90
        if d >= 360:
            d = d%360
        return x,y,d

    
    for c in data:
        print("{},{}:{}".format(x,y,d))
        a = c[0]
        v = int(c[1:])
        if a in ['N','W','S','E']:
            x,y = move(a,v,x,y)
        elif a in ['L','R']:
            x,y,d = turn(d,a,v)
        elif a == 'F':
            x,y = move(trns[d],v,x,y)
        else:
            print("unkonwn cmd")
            exit(1)
    print("total = {} + {} = {}".format(abs(x),abs(y), abs(x)+abs(y)))

def run2(data):

    wx = 10
    wy = 1
    x = 0
    y = 0 


    def move(a,v,x,y):
        if a == 'N' :
            y+= v
        elif a == 'W' :
            x-= v
        elif a == 'S' :
            y-= v
        elif a == 'E' :
            x+= v
        else:
            print("unkonwn cmd a {}",a)
            exit(2)
        return x,y

        #print("total: {}".format(tl))
    def turn(a,x,y,v):
        vv = v
        while (vv > 0):
            #print("{},{} -> ".format(x,y), end="")
            if a == 'L':
                tx = abs(y)
                ty = abs(x)
                if (x >= 0 and y > 0):  #Q1 -> Q2
                    tx = -tx
                elif (x <= 0 and y >= 0): #Q2 -> Q3
                    ty = -ty
                    tx = -tx
                elif(x <= 0 and y < 0): # Q3 -> Q4
                    ty = -ty
                elif (x >= 0 and y <= 0): # Q4 ->Q1
                    pass
                else:
                    print("unkonwn cmd {}",a)
                    exit(4)
            elif a == 'R':
                tx = abs(y)
                ty = abs(x)
                if (x > 0 and y >= 0):  #Q1 -> Q4
                    ty = -ty
                elif (x <= 0 and y >= 0): #Q2 -> Q1
                    pass
                elif(x <= 0 and y < 0): # Q3 -> Q2
                    tx = -tx
                elif (x > 0 and y < 0): # Q4 ->Q3
                    ty = -ty
                    tx = -tx
                else:
                    print("unkonwn cmd {}",a)
                    exit(3)
            else:
                print("unkonwn cmd b {}",a)
            vv-=90
            x=tx
            y=ty
        #print("{},{} ".format(x,y))
        return x,y
        
    for c in data:
        # count+=1
        # if count > 30:
        #     exit(1)
        
        a = c[0]
        v = int(c[1:])
        
        if a in ['N','W','S','E']:
            print("{}: {},{} -> ".format(c, wx, wy), end="")
            wx,wy = move(a,v,wx,wy)
            print("{},{}".format(wx,wy))
        elif a in ['L','R']:
            print("{}: {},{} -> ".format(c, wx, wy), end="")
            wx,wy = turn(a,wx,wy,v)
            print("{},{}".format(wx,wy))
        elif a == 'F':
            print("{}: {},{} [{}]-> ".format(c, x, y, v), end="")
            x += wx*v
            y += wy*v
            print("{},{}".format(x,y))
        else:
            print("unkonwn cmd")
            exit(1)
        print("s:({},{})  w:({},{})".format(x,y,wx,wy, c))
    print("total = {} + {} = {}".format(abs(x),abs(y), abs(x)+abs(y)))
    #59709

run2(data)
