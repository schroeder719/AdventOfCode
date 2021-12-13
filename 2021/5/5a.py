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
        # self.table[0][0] = 1
        # self.table[9][9] = 3
        # self.table[0][9] = 2
        # self.table[9][0] = 4
        
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

    # def call(self,val):
    #     self.called.append(val)
    #     if val in self.data:
    #         index = self.data.index(val)
    #         self.hits[index] = 1
    #         return True
    #     else:
    #         return False
    
    # def check(self):
    #     for i in range(0,25,5):
    #         if sum(self.hits[i:i+5]) == 5:
    #             print("{}".format(self.data[i:i+5]))
    #             return True
    #     for i in range(0,5):
    #         total = 0
    #         winners = []
    #         for j in range(0,25,5):
    #             total+=self.hits[i+j]
    #             winners.append(self.data[i+j])
    #         if total == 5:
    #             print(winners)
    #             return True

    def score(self):
        count = 0
        for y in range(self.y):
            for x in range(self.x):
                if self.table[y][x] >= 2:
                    count+=1
        print(count) 

t = Table(1000,1000)
t.print()

reg = re.compile("(\d+),(\d+) -> (\d+),(\d+)")
for l in lines:
    print(l)
    m =  reg.match(l)
    if not m:
        print("MATCH ERROR")
        exit()

    x1  = int(m.group(1))
    y1  = int(m.group(2))
    x2  = int(m.group(3))
    y2  = int(m.group(4))

    t.addLine(x1,y1,x2,y2)
t.print()
t.score()

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

