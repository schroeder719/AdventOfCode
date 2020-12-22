import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math


#data = u.readfile(u.AOC_2020 + "\\20\\input_ex.txt")
data = u.readfile(u.AOC_2020 + "\\20\\input.txt")

class Tile:
    WIDTH=10
    HEIGHT=10
    PIXLE = {"#":1,".":0}
    def __init__(self,data):
        self.id = int(re.match(r"Tile (\d+):$",data[0]).group(1))

        self.map = data[1:]
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        self.matchCount = 0
        self.sides = [0,0,0,0]
        self.order = 0
        self.calcEdges()
        

    def calcEdges(self):
        data = self.map
        lef = 0
        rig = 0
        top = 0
        bot = 0
        for row in range(0,len(data)):
            lef += self.PIXLE[data[row][0]]*(2**row)
            rig += self.PIXLE[data[row][len(data[row])-1]]*(2**row)
        cols = len(data[0])-1
        for col in range(cols,-1,-1):
            top += self.PIXLE[(data[0][col])]*(2**(cols-col))
            bot += self.PIXLE[(data[len(data)-1][col])]*(2**(cols-col))

        
        self.left = lef
        self.left_r = int('{:010b}'.format(lef)[::-1], 2)
        self.right = rig
        self.right_r = int('{:010b}'.format(rig)[::-1], 2)
        self.top = top
        self.top_r = int('{:010b}'.format(top)[::-1], 2)
        self.bottom = bot
        self.bottom_r = int('{:010b}'.format(bot)[::-1], 2)
        pass

    def flipV(self):
        #self.displayMap()
        #print("")
        newMap = []
        for row in self.map:
            newMap.append(row[::-1])
        self.map = newMap
        sides = self.sides
        l = sides[0]
        r = sides[2]
        sides[2] = l
        sides[0] = r
        self.sides = sides
        #self.displayMap()
        #self.calcEdges()



    def flipH(self):
        #self.displayMap()
        #print("")
        newMap = []
        for row in self.map:
            newMap.insert(0,row)
        self.map = newMap
        sides = self.sides
        t = sides[1]
        b = sides[3]
        sides[1] = b
        sides[3] = t
        self.sides = sides
        #self.displayMap()
        #self.calcEdges()

    def rotateR90(self):
        #self.displayMap()
        #print("")
        A = []
        for line in self.map:
            A.append(list(line))
        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp
        newMap = []
        for row in A:
            newMap.append("".join(row))
        sides = self.sides
        sides.insert(0,sides.pop())
        self.sides = sides
        self.map = newMap
        #self.displayMap()
        

    def match(self):
        pass

    def display(self):
        print("Tile {} ".format(self.id), end="")
        print("  L: {} ".format(self.left), end="")
        print("  R: {} ".format(self.right), end="")
        print("  T: {} ".format(self.top), end="")
        print("  B: {} ".format(self.bottom))
        #for line in self.full:
        #    print(line)
    def displayMap(self):
        for line in self.map:
            print(line)

    def getEdges(self):
        return (self.id, self.left, self.top,self.right,self.bottom, self.left_r,self.top_r, self.right_r,self.bottom_r)
    
    def getEdge(self,i):
        if i == 0:
            return self.left
        elif i == 1:
            return self.top
        elif i == 2:
            return self.right
        elif i == 3: 
            return self.bottom
        elif i == 4:
            return self.left_r
        elif i == 5:
            return self.top_r
        elif i == 6:
            return self.right_r
        elif i == 7: 
            return self.bottom_r

    
    def setMatchCount(self,count):
        self.matchCount = count

    def fitMatch(self,match):
        for i in range(len(match)):
            e = match[i]
            if e > 0:
                if e == self.left or e == self.left_r:
                    self.reposition(0,i,e)
                
                elif e == self.top or e == self.top_r:
                    self.reposition(1,i,e)
                
                elif e == self.right or e == self.right_r:
                    self.reposition(2,i,e)
                
                elif e == self.bottom or e == self.bottom_r:
                     self.reposition(3,i,e)
                
                else:
                    continue
                self.calcEdges()
                break

        # first side should be oriented correctly now, check other sides
        found = True
        lookup = [self.left,self.top,self.right,self.bottom]
        for i in range(4):
            if match[i] > 0 and match[i] != lookup[i]:
                found = False
                break
            elif match[i] == -1 and self.sides[i] != 1:
                found = False
                break

        return found

    def reposition(self,a,b,e):
        #a is found side, b is side needed
        while a != b:
            self.rotateR90()
            a = (a+1)%4
        self.calcEdges()
        if self.getEdge(b) != e and self.getEdge(b+4) == e:
            if b == 0 or b == 2:
                self.flipH()
            else:
                self.flipV()



    def setSides(self,sides):
        self.sides = sides




class Picture:
    OPPOSITE = [2,3,1,0]
    def __init__(self, data):
        self.tiles = dict() 
        self.freq = dict()
        self.placed = []
        picdata = []
        self.grid = None
        for line in data:
            if line == "":
                t = Tile(picdata)
                self.tiles[t.id] = t
                picdata = []
            else:
                picdata.append(line)
        


        print("# of tiles: {}".format(len(self.tiles)))
        
    def calculate(self):
        self.freq = dict()
        self.edges = dict()
        for k in self.tiles.keys():
            #self.tiles[k].display()
            edges = self.tiles[k].getEdges()
            self.countSides(edges)
            #edges = edges[1:]
            for e in (edges[1:]):
                if e in self.edges.keys():
                    lst = self.edges[e]

                else:
                    lst = []
                lst.append(k)
                self.edges[e] = lst
        
        count = [0]*10
        #sum = 0
        for k,v in self.freq.items():
            #print("{}: {}".format(k,v))
            count[v]+=1
            #sum+= self.freq[k]
        #print(count, sum)
        self.freqCount = count
        

    def countSides(self,lst):
        fm = 0
        for side in lst[1:]:
            if side in self.freq.keys():
                count = self.freq[side]
                self.freq[side] = count + 1
                fm+=1
            else:
                self.freq[side] = 1
        self.tiles[lst[0]].setMatchCount(fm)
        


    def printFreq(self):
        count = [0]*10
        sum = 0
        for k,v in self.freq.items():
            print("{}: {}".format(k,v))
            count[v]+=1
            sum+= self.freq[k]
        print(count, sum)
        #self.freqCount = count

    def findCorners(self):
        matches = []
        sidesLookup = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
        for k in self.tiles.keys():
            t = self.tiles[k]
            #need to find a corner, which means two adjasent edges are unique
            edges = t.getEdges()[1:]
        
            for i in range(0,4):
                if self.freq[edges[i]] == 1 and self.freq[edges[(i+1)%4]] == 1 and self.freq[edges[(i+4)%8]] == 1  and self.freq[edges[(i+5)%8]] == 1:
                    t.setSides(sidesLookup[i].copy())
                    matches.append(t.id)
                    print("{}".format(t.id))
                    break
        sum = 1
        for i in matches:
            sum*=i
        print("{}".format(sum))
        self.corners = matches

    def findSides(self):
        # sides only have one edge that doesn't have a match
        matches = []
        for k in self.tiles.keys():
            if k in self.corners:
                continue
            t = self.tiles[k]
            edges = t.getEdges()[1:]
            count = 0
            sides = [0,0,0,0]
            for i in range(4):
                if self.freq[edges[i]] == 1 and self.freq[edges[i+4]] == 1:
                    count+=1
                    sides[i] = 1
            if count == 1:
                matches.append(k)
                t.setSides(sides)
        print("Found {} side pieces".format(len(matches)))
        self.sides = matches

    def findMatchingTile(self,match):
        #match is a 4 element array where non-zero elements need to match, order is l,t,r,b, negative elemint indicates side
    
        for i in range(4):
            if match[i] > 0:
                n = self.tiles[match[i]]
                ns = (n.getEdges()[1:])
                side = ns[self.OPPOSITE[i]]
                match[i] = side
        for i in range(4):
            if match[i] > 0:
                tiles = self.edges[match[i]]
                for i in tiles:
                    if i in self.placed:
                        continue
                    t = self.tiles[i]
                    if t.fitMatch(match):
                        return t.id

    def layout(self):
        #place first corner:
       
        order = int(math.sqrt(len(self.tiles)))
        self.order = order
        grid = [[-1 for i in range(order+2)] for j in range(order+2)]
        newgrid = [[0 for i in range(order)] for j in range(order)]
        for row in range(order):
            for col in range(order):
                grid[row+1][col+1] = 0

        last = 0
        for row in range(1,order+1):
            for col in range(1,order+1):
                if row == 1 and col == 1:

                    #find the corner piece
                    corner = self.tiles[self.corners[0]]
                    while corner.sides != [1,1,0,0]:
                        corner.rotateR90()
                    corner.calcEdges()
                    grid[1][1] = corner.id
                    self.placed.append(corner.id)
                    last = corner.id
                else:
                    target = [grid[row][col-1],grid[row-1][col],grid[row][col+1],grid[row+1][col]]
                    f = self.findMatchingTile(target)
                    if f:
                        self.placed.append(f)
                        grid[row][col] = f
                #print(grid)

        for row in range(order):
            for col in range(order):
                newgrid[row][col] = grid[row+1][col+1]
        self.grid = newgrid
        print(grid)


        # last = self.findMatchingTile([-1,corner.bottom,0,0])
        # grid[1][0] = last
        # last = self.findMatchingTile([-1,self.tiles[last].bottom,0,-1])
        # grid[2][0] = last
        # print(grid)
    def removeBoarders(self):
        tilegrid = [[None for i in range(self.order)] for j in range(self.order)]
        for row in range(self.order):
            for col in range(self.order):
                id = self.grid[row][col]
                tilegrid[row][col] = self.tiles[id]
        lines = [""]*(self.order*8)
        i = 0
        for trow in tilegrid:
            for tcol in trow:
                for row in range(1,9):
                    lines[i+row-1] += tcol.map[row][1:9]
            i+=8 
        self.wholeMap = lines
        #for row in lines:
        #    print(row)

    def findSeaMonsters(self):
        seaMonsterCount = 0
        wholeMap = self.wholeMap
        tries = 0
        while seaMonsterCount == 0:
            print("{}".format(tries))
            if tries in [0,3,6,9]:
                wholeMap = self.rotateR90(wholeMap)                
            elif tries in [1,4,7,10]:
                wholeMap = self.flipH(wholeMap)
            elif tries in [2,5,8,11]:
                wholeMap = self.flipV(wholeMap)

            tries+=1
            if tries >11:
                return
            
            for r in range(len(self.wholeMap)-2):
                for c in range(len(self.wholeMap[0])-20):
                    if wholeMap[r][c+18] == '#' and \
                        wholeMap[r+1][c+0] == '#' and \
                        wholeMap[r+1][c+5] == '#' and \
                        wholeMap[r+1][c+6] == '#' and \
                        wholeMap[r+1][c+11] == '#' and \
                        wholeMap[r+1][c+12] == '#' and \
                        wholeMap[r+1][c+17] == '#' and \
                        wholeMap[r+1][c+18] == '#' and \
                        wholeMap[r+1][c+19] == '#' and \
                        wholeMap[r+2][c+1] == '#' and \
                        wholeMap[r+2][c+4] == '#' and \
                        wholeMap[r+2][c+7] == '#' and \
                        wholeMap[r+2][c+10] == '#' and \
                        wholeMap[r+2][c+13] == '#' and \
                        wholeMap[r+2][c+16] == '#':
                        print("Found Sea Monster!")
                        seaMonsterCount+=1
            waves = 0
            for r in range(len(self.wholeMap)):
                waves+= self.wholeMap[r].count('#')
                    
        print("Total waves: {}".format(waves))
        print("Total Sea Monsters: {}".format(seaMonsterCount))
        print("Waves not a sea monster: {}".format(waves-(seaMonsterCount*15)))
        return seaMonsterCount, waves



    def printSeaMonster(self):
        row = 3
        col = 21
        for row in range(row):
            for col in range(col):
                if row in [0,] and col in [18]:
                    print("#",end="")
                elif row in [1,] and col in [0,5,6,11,12,17,18,19]:
                    print("#", end="")
                elif row in [2,] and col in [1,4,7,10,13,16]:
                    print("#", end="")
                else:
                    print(" ",end="")
            print("")
        print("")

    def rotateR90(self,map):
        #self.displayMap()
        #print("")
        A = []
        for line in map:
            A.append(list(line))
        N = len(A[0])
        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = A[i][j]
                A[i][j] = A[N - 1 - j][i]
                A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
                A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
                A[j][N - 1 - i] = temp
        newMap = []
        for row in A:
            newMap.append("".join(row))
        # sides = self.sides
        # sides.insert(0,sides.pop())
        # self.sides = sides
        return newMap

    def flipV(self,map):
        #self.displayMap()
        #print("")
        newMap = []
        for row in map:
            newMap.append(row[::-1])
        return newMap

        #self.displayMap()
        #self.calcEdges()



    def flipH(self,map):
        newMap = []
        for row in map:
            newMap.insert(0,row)
        return newMap
        
                

p = Picture(data)
#p.printFreq()
#p.tiles[1427].rotateR90()
#p.findMatches()
p.calculate()
p.printFreq()
p.findCorners()
p.findSides()
p.layout()
p.removeBoarders()
p.printSeaMonster()
p.findSeaMonsters()

