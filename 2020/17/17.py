import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy


#data = u.readfile(u.AOC_2020 + "\\17\\input.txt")
data = u.readfile(u.AOC_2020 + "\\17\\input.txt")

# print(data)
# cube = []
# for i in range(3):
#     cube.append(data)

# for z in range(3):
#     for y in range(3):
#         print(cube[x][y][z])
#         # for x in range(3):
#         #     print(cube[x][y][z])

class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print("{:02}, {:02}, {:02}".format(self.x,self.y,self.z))
    

class Cube:

    def __init__(self,x,y,z,state):
        self.p = Point(x,y,z)
        self.x = self.p.x
        self.y = self.p.y
        self.z = self.p.z
        self.state = state

    def isMatch(self,x,y,z):
        return self.p.x == x and self.p.y == y and self.p.z == z

    def getNeighborList(self):
        n = []
        for x in range(self.p.x-1,self.p.x+2):
            for y in range(self.p.y-1,self.p.y+2):
                for z in range(self.p.z-1,self.p.z+2):
                    #print("{},{},{}".format(x,y,z))
                    if not self.isMatch(x,y,z):
                        n.append(Point(x,y,z))
        return n

    def isActive(self):
        return self.state == 1

    def getPoint(self):
        return self.p

    def setState(self, s):
        self.state = s
    
    def print(self):
        print("{},{},{}:{}".format(self.x,self.y,self.z,self.state))

    def setId(self, id):
        self.id = id

class Space:
    max = 30
    half = 15
    
    def __init__(self, data):
        self.cubes = dict()
        self.xmx = 0
        self.xmn = 0
        self.ymx = 0
        self.ymn = 0
        self.zmx = 0
        self.zmn = 0

        self.flexList = []
        
        self.load(data)

    def calcId(self,p):
        id = p.z* (self.max*self.max) + (p.y * self.max) + p.x
        return id
    
    def load(self, data):
        leny = len(data)
        lenx = len(data[0])
        offx = Space.half - lenx/2
        offy = Space.half - leny/2
        for y in range(len(data)):
            for x in range(len(data[y])):
                if data[y][x] == '#':
                    s = 1
                else:
                    s = 0
                self.addCube(Cube(int(x+offx),int(y+offy),self.half-1,0))
                self.addCube(Cube(int(x+offx),int(y+offy),self.half,s))
                self.addCube(Cube(int(x+offx),int(y+offy),self.half+1,0))
                print(data[y][x], end="")
            print("")
    
    def addCube2(self,x,y,z,state):
        c = Cube(x,y,z, state)
        self.addCube(c)

    def addCube(self,c):
        id = self.calcId(c.getPoint())
        c.setId(id)
        self.cubes[id] = c

    def fillSpace(self,x,y,z):
        for x in range(x):
            for y in range(y):
                for z in range(-int(z/2),int(z/2)+1):
                    c = self.getCubeByAddress(x,y,z)


    def getCubeByAddress(self,x,y,z):
        try:
            c = self.cubes[self.calcId(Point(x,y,z))]
        except KeyError:
            c = Cube(x,y,z,0)
            #self.addCube(c)
            self.flexList.append(c)

        return c

    def getCubeByPoint(self,p):
        try:
            c = self.cubes[self.calcId(p)]
        except KeyError:
            c = Cube(p.x,p.y,p.z,0)
            #self.addCube(c)
            self.flexList.append(c)

        return c

    def printReport(self):
        for z in range(self.zmn, self.zmx):
            self.printSlice(z)
    def printList(self):
        for c in self.cubes:
            c.print()

    def printSlice(self, z):
        print("Z: {}".format(z))
        print(" ",end="")
        for x in range(self.xmn, self.xmx+1):
            print("{}".format(x),end="")
        print("")
        for y in range(self.ymn,self.ymx+1):
            print("{}".format(y),end="")
            for x in range(self.xmn, self.xmx+1):
                c = self.getCubeByAddress(x,y,z)
                if c is not None:
                    if (c.state == 0):
                        print('.', end="")
                    else:
                        print('#', end="")
            print("")

    def countActive(self):
        count = 0
        for k in self.cubes.keys():
            if self.cubes[k].state == 1:
                count+=1
        return count

    def updateCube(self, p, state):
        id = self.calcId(Point(p.x,p.y,p.z))
        try:
            c = self.cubes[id]
            c.state = state
        except KeyError:
            c = Cube(p.x,p.y,p.z,state)
        
        self.cubes[id] = c

    def flex(self):
        for i in self.flexList:
            self.addCube(i)
        self.flexList =[]

def cycle(space):
    
    sa = []
    si = []
    for key in space.cubes.keys():
        c = space.cubes[key]
        nl = c.getNeighborList()
        #nl = space.fixNeighborList(nl)
        count = 0
        #print("")
        #c.print()
        #print("----------")
        for n in nl:
            #print("   ", end="")
            #n.print()
            cb = space.getCubeByPoint(n)
            if cb.isActive():
                count+=1
        if c.isActive():
            if not (count == 2 or count == 3):
                #print("a->i")
                si.append(c.getPoint())
                #space.getCubeByPoint(c.getPoint()).setState(0)
            else:
                pass
        else:
            if count == 3:
                #print("i->a")
                sa.append(c.getPoint())
                #space.getCubeByPoint(c.getPoint()).setState(1)
    for i in sa:
        #space.getCubeByPoint(i).setState(1)
        space.updateCube(i,1)
    for i in si:
        #space.getCubeByPoint(i).setState(0)
        space.updateCube(i,0)
    print("")
    
    space.flex()
    return space
            

s = Space(data)

# s.printSlice(0)
# s.printSlice(1)

# center = s.getCubeByAddress(0,0,0)
# center.getNeighborList()

s.printReport()
#s.printList()
for i in range(6):
    s = cycle(s)
    print("\n\nCYCLE: {}".format(i))
    s.printReport()
    #s.printList()

    print(s.countActive())
    