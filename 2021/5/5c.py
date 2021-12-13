import os
import re
import common.util as u
#print(os.getcwd())

lines = u.readfile(u.AOC_2021 + "\\5\\input.txt",Integer=False)



class Table:
    W = 5
    H = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.table = [ [0]*x for i in range(y)]
        self.points = []
        
    def print(self):
        for y in range(self.y):
            print(self.table[y])

    def addLine(self,x1,y1,x2,y2):
        self.points.append([x1,y1,x2,y2])
        if y1 == y2:
            if x1 < x2:
                # horiz
                while x1 <= x2:
                    self.table[y1][x1] += 1
                    x1+=1
            elif x1 > x2:
                while x1 >= x2:
                    self.table[y1][x1] += 1
                    x1-=1
        elif x1 == x2:
            if y1 < y2:
                # vert
                while y1 <= y2:
                    self.table[y1][x1] += 1
                    y1+=1
            elif y1 > y2:
                # vert
                while y1 >= y2:
                    self.table[y1][x1] += 1
                    y1-=1
        elif abs(x1-x2) == abs(y1-y2): # 45 degree
            if (x1 < x2):
                xdif = 1
            elif (x1 > x2):
                xdif = -1
            
            if (y1 < y2):
                ydif = 1
            else:
                ydif = -1

            while (x1 != x2 or y1 != y2):
                self.table[y1][x1] +=1
                x1 += xdif
                y1 += ydif
            self.table[y1][x1] +=1

    def score(self):
        count = 0
        for y in range(self.y):
            for x in range(self.x):
                if self.table[y][x] >= 2:
                    count+=1
        print(count) 

reg = re.compile("(\d+),(\d+) -> (\d+),(\d+)")


#
#t = Table(10,10)
#t.print()

points = []

for l in lines:
    #print(l)
    m =  reg.match(l)
    if not m:
        print("MATCH ERROR")
        exit()
    
    points.append( [int(i) for i in m.group(1,2,3,4)]) 
    #print(points[-1])

    # x1  = int(m.group(1))
    # y1  = int(m.group(2))
    # x2  = int(m.group(3))
    # y2  = int(m.group(4))
max_x = 0
max_y = 0
for p in points:
    if p[0] > max_x:
        max_x =p[0]
    if p[2] > max_x:
        max_x =p[2]
    if p[1] > max_y:
        max_y =p[1]
    if p[3] > max_y:
        max_y =p[3]

print(max_x,max_y)

t = Table(max_x+1,max_y+1)
for p in points:
    t.addLine(p[0],p[1],p[2],p[3])
t.score()

#t.addLine(x1,y1,x2,y2)
#t.print()
#t.score()

# bid = 0        
# count = 0 
# boards = []
# while count < len(raw_boards):
#     boards.append(Board(bid,raw_boards[count:count+5]))
#     count+=6
#     bid+=1

# for i in cmds.split(','):
#     for b in boards:
#         if b.call(i):
#             if b.check():
#                 print("{} won!".format(b.id))
#                 b.score()
#                 exit()

