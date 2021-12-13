import os
import re
import common.util as u
#print(os.getcwd())

cmds = u.readfile(u.AOC_2021 + "\\4\\input.txt",Integer=False)[0]
raw_boards  = u.readfile(u.AOC_2021 + "\\4\\input2.txt",Integer=False)
print(cmds)
class Board:
    W = 5
    H = 5
    def __init__(self,id,data):
        self.id = id
        self.data = []
        self.called = []
        self.hits = [0] * (self.W*self.H)
        for i in data:
            for j in i.split():
                self.data.append(j)
    def print(self):
        print(self.data)

    def call(self,val):
        self.called.append(val)
        if val in self.data:
            index = self.data.index(val)
            self.hits[index] = 1
            return True
        else:
            return False
    
    def check(self):
        for i in range(0,25,5):
            if sum(self.hits[i:i+5]) == 5:
                print("{}".format(self.data[i:i+5]))
                return True
        for i in range(0,5):
            total = 0
            winners = []
            for j in range(0,25,5):
                total+=self.hits[i+j]
                winners.append(self.data[i+j])
            if total == 5:
                print(winners)
                return True

    def score(self):
        t = 0
        for i in range(0,25):
            if self.hits[i] == 0:
                t+= int(self.data[i])
        lc = int(self.called[-1])
        print("{} * {} = {}".format(t,lc,t*lc))
        return lc*t

bid = 0        
count = 0 
boards = []
while count < len(raw_boards):
    boards.append(Board(bid,raw_boards[count:count+5]))
    count+=6
    bid+=1

for i in cmds.split(','):
    for b in boards:
        if b.call(i):
            if b.check():
                print("{} won!".format(b.id))
                b.score()
                exit()

