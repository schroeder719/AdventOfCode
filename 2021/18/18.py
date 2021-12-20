import os
import re
import common.util as u
import numpy as np
import sys
import copy
from collections import deque
#print(os.getcwd())

class SnailNumber():
    l = None
    r = None
    p = None
    v = None

    @classmethod
    def fromParts(cls,left,right,parent,val):
        s = SnailNumber("")
        s.setLeft(left)
        s.setRight(right)
        s.v = val
        s.p = parent
        return s

    def __init__(self, snt, parent=None):
        self.p = parent

        if len(snt) == 0:
            return
        counter = 0
        if snt[0] != '[' or snt[-1] != ']':
            print("Error: ", snt)
            exit()
        snt = snt[1:-1] # trim ends
        for i in range(len(snt)):
            if snt[i] == "[":
                counter+=1
            elif snt[i] == "]":
                counter-=1
            elif snt[i] == ',' and counter == 0:
                if snt[0:i].isnumeric():
                    self.l = SnailNumber.fromParts(None,None,self,int(snt[0:i]))
                else:
                    self.l = SnailNumber(snt[0:i], self)
                if snt[i+1:].isnumeric():
                    self.r =  SnailNumber.fromParts(None,None,self,int(snt[i+1:]))
                else:
                    self.r = SnailNumber(snt[i+1:], self)
            
    def __add__(self, o):
        nsn = SnailNumber(o)
        self.p = SnailNumber.fromParts(self,nsn,None, None) #make a new parent
        nsn.p = self.p
        return self.p

    def __radd__(self,o):
        nsn = SnailNumber(o)
        self.p = SnailNumber.fromParts(nsn, self,None, None) #make a new parent
        return self.p
    
    def getText(self):
        if self.v is not None:
            return self.v
        left = self.l.getText()
        right = self.r.getText()
        return "[{},{}]".format(left,right)

    def setLeft(self,L):
        self.l = L

    def setRight(self,R):
        self.r = R

    def pp(self):
        print(self.getText())

    # def treeWalk(self):
    #     if self.l is not None:
    #         if isinstance(self.l, int):
    #             print(self.l)
    #         else:
    #             self.l.treeWalk()
    #     if self.r is not None:
    #         if isinstance(self.r, int):
    #             print(self.r)
    #         else:
    #             self.r.treeWalk()

    def mag(self):
        mag = 0
        if self.l.v is not None:
            mag += self.l.v*3
        else:
            mag+=(self.l.mag()*3)
        if self.r.v is not None:
            mag += self.r.v*2
        else:
            mag+=(self.r.mag()*2)
        return mag


    #    def __reduce():
    def rnum(self):
        if self.p is None:
            return None
        if self == self.p.r:
            return self.p.rnum()
        n = self.p.r
        while n.l is not None:
            n = n.l
        return n

    # Get the next number to the left of node
    def lnum(self):
        if self.p is None:
            return None
        if self == self.p.l:
            return self.p.lnum()
        n = self.p.l
        while n.r is not None:
            n = n.r
        return n


    def split(self):
        res = False
        if self.v is not None:
            if self.v >= 10:
                self.l = SnailNumber.fromParts(None, None, self, int(self.v/2))
                self.r = SnailNumber.fromParts(None, None, self, int((self.v+1)/2))
                self.v = None
                return True
        
        if self.l != None:
            if self.l.split():
                return True
        if self.r != None:
            if self.r.split():
                return True

        return False

    def add_left(self,av):
        if isinstance(self.l,int):
            self.l +=av
        else:
             return self.l.add_left(av)
        

    def add_right(self,av):
        if isinstance(self.r,int):
            self.r +=av
        else:
            self.r.add_right(av)

    def findEx(self, depth=0):
        if depth == 4 and self.v == None:
            return self
        
        if self.l is not None:
            le = self.l.findEx(depth+1)
            if le:
                return le
        if self.r is not None:
            re = self.r.findEx(depth+1)
            if re:
                return re
        return None


    def explode(self, d):
        en = self.findEx()
        if en is None:
            return False

        nl = en.l.lnum()
        if nl is not None:
            nl.v += en.l.v

        nr = en.r.rnum()
        if nr is not None:
            nr.v += en.r.v

        en.l = None
        en.r = None
        en.v = 0
        return True

    def reduce(self):
        done = False
        while not done:
            #self.pp()
            #print("trying exlpode")
            d = 0
            e = False
            s = False
            
            if self.explode(d):
                #print("explode")
                e = True
                continue
            else:
                #self.pp()
                #print("trying split")
                s = self.split()
                #if s:
                    #print("split")
            done = not s and not e
        #self.pp()




if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\18\\input.txt",Integer=False)
    sn = SnailNumber(data[0])
    sn.pp()
    for d in data[1:]:
        print("*******************************")
        print("Adding: {}".format(d))
        sn+= d
        sn.reduce()
        #sn.pp()

    print(sn.mag())
    max = 0
    for i in range(len(data)):        
        for k in range(len(data)):
            if i == k:
                continue
            #b = copy.copy(a)
            b = SnailNumber(data[i])
            b += data[k]
            b.reduce()
            mag = b.mag()
            if mag > max:
                max = mag
            print("n", end="")
        print("n")
    print(max)




    
    # sn= SnailNumber("[[[[4,3],4],4],[7,[[8,4],9]]]")
    # sn.pp()
    # sn+= "[1,1]"
    # sn.pp()
    # sn.reduce()
    # sn+= "[6,6]"
    # sn.pp()
    # sn.reduce()
    # sn.pp()
    #sn= SnailNumber("[[6,[5,[4,[3,2]]]],1]")
    # sn= SnailNumber("")
    # sn=SnailNumber("[[[[[9,8],1],2],3],4]")
    

    # sn.pp()
    # res,lrv, rrv = sn.explode(d)
    # sn.pp()
    # res,lrv, rrv = sn.explode(d)
    # sn.pp()