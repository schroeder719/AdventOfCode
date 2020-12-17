import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy


#data = u.readfile(u.AOC_2020 + "\\17\\input.txt")
data = u.readfile(u.AOC_2020 + "\\17\\input_ex.txt")

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
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w  = w

    def print(self):
        print("{:02}, {:02}, {:02},{:02}".format(self.x,self.y,self.z,self.w))
    

class Cube:

    def __init__(self,x,y,z,w,state):
        self.p = Point(x,y,z,w)
        self.x = self.p.x
        self.y = self.p.y
        self.z = self.p.z
        self.w = self.p.w
        self.state = state

    def isMatch(self,x,y,z,w):
        return self.p.x == x and self.p.y == y and self.p.z == z and self.p.w == w

    def getNeighborList(self):
        n = []
        for x in range(self.p.x-1,self.p.x+2):
            for y in range(self.p.y-1,self.p.y+2):
                for z in range(self.p.z-1,self.p.z+2):
                    #print("{},{},{}".format(x,y,z))
                    for w in range(self.p.w-1,self.p.w+2):
                        if not self.isMatch(x,y,z,w):
                            n.append(Point(x,y,z,w))
        return n

    def isActive(self):
        return self.state == 1

    def getPoint(self):
        return self.p

    def setState(self, s):
        self.state = s
    
    def print(self):
        print("{},{},{},{}:{}".format(self.x,self.y,self.z,self.w,self.state))

    def setId(self, id):
        self.id = id

class Space:
    max = 30
    half = 15
    max_y = max
    max_z = max * max
    max_w = max * max * max
    
    def __init__(self, data):
        self.cubes = dict()
        self.flexList = []    
        self.load(data)

    def calcId(self,p):
        #id = p.z* (self.max*self.max) + (p.y * self.max) + p.x
        #id =                    p.z* (self.max*self.max) + (p.y * self.max) + p.x
        id = (p.w*self.max_w) + (p.z* self.max_z) + (p.y * self.max_y) + p.x
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
                self.addCube(Cube(int(x+offx),int(y+offy),self.half-1,self.half,0))
                self.addCube(Cube(int(x+offx),int(y+offy),self.half,self.half,s))
                self.addCube(Cube(int(x+offx),int(y+offy),self.half+1,self.half,0))
                print(data[y][x], end="")
            print("")
        dim = (len(data) + 2)
        offset = Space.half - int(dim/2)

        
        for x in range(offset,offset+dim+1):
            for y in range(offset,offset+dim+1):
                for z in range(offset,offset+dim+1):
                    for w in range(offset,offset+dim+1):
                        #print("{},{},{}:{}".format(x,y,z,w))
                        self.addCube(Cube(x,y,z,w,0),overwrite=False)
    
    # def addCube2(self,x,y,z,state):
    #     c = Cube(x,y,z, state)
    #     self.addCube(c)

    def addCube(self,c,overwrite=True):
        id = self.calcId(c.getPoint())
        c.setId(id)
        if not overwrite:
            if id in self.cubes.keys():
                return
        # if id in self.cubes.keys():
        #     print("error addCube")
        #     exit(1)
        self.cubes[id] = c

    def getCubeByAddress(self,x,y,z,w):
        try:
            c = self.cubes[self.calcId(Point(x,y,z,w))]
        except KeyError:
            c = Cube(x,y,z,w,0)
            #self.addCube(c)
            self.flexList.append(c)

        return c

    def getCubeByPoint(self,p):
        try:
            c = self.cubes[self.calcId(p)]
        except KeyError:
            c = Cube(p.x,p.y,p.z,p.w,0)
            #self.addCube(c)
            self.flexList.append(c)

        return c

    def printReport(self, i):
        offset = 2 + i*2
        for z in range(self.half-offset, self.half+offset):
            for w in range(self.half-offset, self.half+offset):
                self.printSlice(z,w, offset)
    # def printList(self):
    #     for c in self.cubes:
    #         c.print()

    def printSlice(self, z, w, offset):
        print("Z: {} W:{}".format(z,w))
        print(" ",end="")
        for x in range(self.half-offset, self.half+offset):
            print("{}".format(x),end="")
        print("")
        for y in range(self.half-offset, self.half+offset):
            print("{}".format(y),end="")
            for x in range(self.half-offset, self.half+offset):
                c = self.getCubeByAddress(x,y,z,w)
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
        id = self.calcId(p)
        try:
            c = self.cubes[id]
            c.state = state
        except KeyError:
            c = Cube(p.x,p.y,p.z,p.w,state)
        
        self.cubes[id] = c

    def flex(self):
        for i in self.flexList:
            self.addCube(i,False)
        self.flexList =[]

def cycle(space):
    
    sa = []
    si = []
    for key in space.cubes.keys():
        c = space.cubes[key]
        nl = c.getNeighborList()
        
        count = 0
        #print("")
        #c.print()
        #print("----------")
        for n in nl:
            #print("   ", end="")
            #n.print()
            if space.getCubeByPoint(n).isActive():
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
print(s.countActive())
#s.printReport(0)
for i in range(6):
    s = cycle(s)
    print("\n\nCYCLE: {}".format(i))
    #s.printReport(i)
    print(s.countActive())
    