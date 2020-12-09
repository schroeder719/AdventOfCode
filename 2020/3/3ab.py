import os
#from colorama import Fore, Back, Style, init
import re


class Forest:
    map=[]
    x = 0
    y = 0
    w = 0
    h = 0
    def __init__(self, filename, move_x, move_y):
        self.load(filename)
        self.move_x = move_x
        self.move_y = move_y

    def load(self, filename):
        m=[]
        with open(filename) as f:
            for line in f:
                if self.w == 0:
                    self.w = len(line.rstrip())
                self.h+=1
                #print(line)
                #print(list(line))
                m.append(list(line.rstrip()))
                #print(m)
            #print(m)
            self.map = m
            print("map is {} by {}".format(self.w,self.h))

    def display(self):
        for y in self.map:
            print("".join(y))
                
    
    def move(self):
        self.x+=self.move_x
        self.y+=self.move_y
        if self.x > self.w-1:
            #print("{},{}->".format(self.x,self.y), end='')
            self.x -= self.w
            #self.y +=1
            #print("{},{}".format(self.x,self.y))
            #self.display()
            #print("")
            
        if self.y > self.h-1:
            return False,0
        
        try:
            current = self.map[self.y][self.x]
        except:
            print("{},{}".format(self.x,self.y))
            exit(1)
        #print(current,end="")
        if current  == '#' or current == 'X':
            self.map[self.y][self.x] = 'X'
            return True,1
        elif current == '.' or current == 'O':
            self.map[self.y][self.x] = 'O'
            return True,0
        else:
            print("unexpected: {} at {},{}".format(current,self.x,self.y))
            exit(1)
        

    def run(self):
        c = True
        trees = 0
        while (c):
            c, r = self.move()
            trees+=r
            #if trees > 20:
            #    c=False
        print("")
        print("total trees for {},{}: {} ".format(self.move_x,self.move_y, trees))
        return trees
            
            
                


total_valid = 0
total = 0
#init(autoreset=True)
f = Forest(os.path.join(os.getcwd(), "2020\\3\\input.txt"),1,1)
#f.display()
f_1_1 = f.run()

## this is the part one answer
f = Forest(os.path.join(os.getcwd(), "2020\\3\\input.txt"),3,1)
f_3_1 = f.run()

f = Forest(os.path.join(os.getcwd(), "2020\\3\\input.txt"),5,1)
f_5_1 = f.run()

f = Forest(os.path.join(os.getcwd(), "2020\\3\\input.txt"),7,1)
f_7_1 = f.run()

f = Forest(os.path.join(os.getcwd(), "2020\\3\\input.txt"),1,2)
f_1_2 = f.run()


print("total: {}".format(f_1_1*f_3_1*f_5_1*f_7_1*f_1_2))

