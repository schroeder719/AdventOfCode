import os
#from colorama import Fore, Back, Style, init
import re



class Passes:
    #p = None
    def __init__(self, filename):
        self.p = []
        self.load(filename)
        


    def load(self, filename):
        with open(filename) as f:
            for line in f:
                self.p.append(Pass(line.strip()))
    
    def calcAll(self):
            for p in self.p:
                p.calc()

    def disAll(self):
        for p in self.p:
            p.dis()

    def getMaxId(self):
        max = 0
        for p in self.p:
            if p.id > max:
                max = p.id
        print("max: {}".format( max))

    def findMissing(self):
        seats = []
        for i in range (0,872):
            seats.append(i)
        for p in self.p:
            seats.remove(p.id)

        print(seats)


class Pass:
    def __init__(self, r):
        self.r = r
        self.calc
        self.col = 0
        self.row = 0
        self.id = 0
    
    def calc(self):
        val = 127
        row = 0
        
        #r = self.r
        for i in range(0,7):
            val = int(val/2)
         #   print(self.r[i])
            if  self.r[i] == 'B':
                row += val + 1
            #elif self.r[i] == 'F':
            #    row = 0
            
            print(val)
        #print("")
 
        val = 7
        col = 0
        for i in range(7,10):
         #   print(self.r[i])
            val = int(val/2)
            if  self.r[i] == 'R':
                col += val +1
            #elif self.r[i] == 'L':
            #print(val)
            print(col)
        self.col = col
        self.row = row
        self.id = (row * 8) + col

        #print("")
        #print("")
    
    def dis(self):
        print("row: {} col: {} id: {}".format(self.row,self.col,self.id))

ps = Passes(os.path.join(os.getcwd(), "2020\\5\\input.txt"))
ps.calcAll()
ps.disAll()
ps.getMaxId()
ps.findMissing()
