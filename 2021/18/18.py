import os
import re
import common.util as u
import numpy as np
import sys
from collections import deque
#print(os.getcwd())

class SnailNumber():
    l = None
    r = None
    p = None


    @classmethod
    def fromParts(cls,left,right,parent):
        s = SnailNumber("")
        s.setLeft(left)
        s.setRight(right)
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
                    self.l = int(snt[0:i])
                else:
                    self.l = SnailNumber(snt[0:i], self)
                if snt[i+1:].isnumeric():
                    self.r = int(snt[i+1:])
                else:
                    self.r = SnailNumber(snt[i+1:], self)
            
    def __add__(self, o):
        nsn = SnailNumber(o)
        self.p = SnailNumber.fromParts(self,nsn,None) #make a new parent
        return self.p

    def __radd__(self,o):
        nsn = SnailNumber(o)
        self.p = SnailNumber.fromParts(nsn, self,None) #make a new parent
        return self.p
    
    def getText(self):
        if self.l is None or self.r is None:
            print("error")
        if isinstance(self.l, int):
            left = str(self.l)
        else:
            left = self.l.getText()
        if isinstance(self.r,int):
            right = str(self.r)
        else:
            right = self.r.getText()
        return "[{},{}]".format(left,right)

    def setLeft(self,L):
        self.l = L

    def setRight(self,R):
        self.r = R

    def pp(self):
        print(self.getText())

    def treeWalk(self):
        if self.l is not None:
            if isinstance(self.l, int):
                print(self.l)
            else:
                self.l.treeWalk()
        if self.r is not None:
            if isinstance(self.r, int):
                print(self.r)
            else:
                self.r.treeWalk()

    def add_left(self,av):
        if isinstance(self.l,int):
            self.l +=av
        else:
            self.l.add_left(av)

    def add_right(self,av):
        if isinstance(self.r,int):
            self.r +=av
        else:
            self.r.add_right(av)


    def explode(self, d):
        res = False
        lrv = 0
        rrv = 0
        le = False
        re = False
        if d >= 4 and self.l is not None and self.r is not None:
            if isinstance(self.l,int) and isinstance(self.r,int):
               d-=1
               return True,self.l,self.r 
        if self.l is not None:
            if not isinstance(self.l, int):
                d+=1
                res,lrv,rrv = self.l.explode(d)
                le = True
                re = False  
                if res:
                    self.l = 0
                               
        if not res and (self.r is not None) and (lrv >=0) and (rrv>=0):
            if not isinstance(self.r, int):
                d+=1
                res,lrv,rrv = self.r.explode(d)
                re = True
                le = False
                if res:
                    self.r = 0
                    
                    
        if isinstance(self.l,int):
            if (res and re) or (not res and lrv >0):
                self.l += lrv
                lrv = -1
        if isinstance(self.r,int):
            if (res and le) or (not res and rrv > 0):
                self.r += rrv
                rrv = -1

        if self.p is None:
            if le and (rrv > 0):
                self.r.add_left(rrv)
            elif re and (lrv > 0):
                self.l.add_right(lrv)


        res = False
        d-=1
        return res,lrv,rrv
        
            


#    def __reduce():

if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\18\\input_test.txt",Integer=False)
    
    # for d in data:
    #     sn = SnailNumber(d)
    #     snt = sn.getText() 
    #     if snt != d:
    #         print("ERROR: {} != {}",format(snt,d))
    #     sn.pp()
    sn= SnailNumber("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    #sn= SnailNumber("[[6,[5,[4,[3,2]]]],1]")
    # sn= SnailNumber("")
    # sn=SnailNumber("[[[[[9,8],1],2],3],4]")
    sn.pp()
    d = 0
    sn.explode(d)
    sn.pp()
    sn.explode(d)
    sn.pp()
