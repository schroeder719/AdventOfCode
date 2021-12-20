import os
import re
import common.util as u
import numpy as np
from collections import deque
#print(os.getcwd())


def filter(pic,x,y):
    global algo
    
    a = pic[x-1,y-1:y+2]
    b = pic[x,y-1:y+2]
    c = pic[x+1,y-1:y+2]
    a = np.concatenate((a,b), axis=None)
    a = np.concatenate((a,c), axis=None)
    key = ""
    # if x == 5 and y == 5:
    #     print(a)

    for i in a:
        if i == 0.0:
            key += '0'
        else:
            key += '1'
    #print(key)
    val = int(key,2)
    return algo[val]
def translate(pic,zeros,prt):
    count = 0
    if zeros:
        newpic = np.zeros((pic.shape[0],pic.shape[1]))
    else:
        newpic = np.ones((pic.shape[0],pic.shape[1]))
    # print(pic)
    # for row in range(1,len(pic)-1):
    #     for col in range(1,len(pic[row])-1):
    #         print(conv[pic[row,col]],end="")
    #     print("")
    # print("")
    for row in range(1,len(pic)-1):
        for col in range(1,len(pic[row])-1):
            char = filter(pic, row,col)
            if prt: print(char,end="")
            newpic[row,col] = conv[char]
            if char == '#':
                count+=1
        if prt: print("")
    return newpic,count
def upsize(a, n):
    if a[0,0] == 0:
        zeros = True
    else:
        zeros = False
    n2 = int(n/2)
    if zeros:
        pic = np.zeros((a.shape[0]+n,a.shape[1]+n))
    else:
        pic = np.ones((a.shape[0]+n,a.shape[1]+n))
    pic[n2:a.shape[0]+(n2),n2:a.shape[1]+n2] = a
    return pic

def pp(pic):
    for row in range(len(pic)):
        for col in range(len(pic[row])):
            char = conv[pic[row,col]]
            print(char,end="")
            
        print("")

if __name__ == "__main__":
    data = u.readfile(u.AOC_2021 + "\\20\\input.txt",Integer=False)

    algo = data[0]
    data = data[2:]
    conv = {'#':1, ".":0, 0.0:".",1.0:"#"}
    # for i in range(10):
    #     conv[chr(97+i)] = i
    #     conv[i] = chr(97+1)


    # print(algo)
    # print(data)
    for i in range(len(data)):
        t = []
        for j in range(len(data[i])):
            t.append(conv[data[i][j]])
        data[i] = t
    pic = np.array(data)
    pic = upsize(pic,15)
    # n = 30
    # n2 = int(n/2)
    # pic = np.zeros((a.shape[0]+n,a.shape[1]+n))
    # pic[n2:a.shape[0]+(n2),n2:a.shape[1]+n2] = a

#    pic,count = translate(pic,True, False)
    for x in range(50):
        pic = upsize(pic[1:pic.shape[0]-1,1:pic.shape[1]-1],4)
        pic,count = translate(pic,False, False)
    pp(pic)    
    print(count)

    
    
    #print(newpic)
    #    # f = a.copy()
    # # f.fill(1)
    # # print(f)    
    # counter = 0
    # print(a)
    # print(a[0,2])
    
    # for s in range(1000):
    #     #print(s)
    #     #step 1
    #     increase(a)
    #     #print(a)
    #     #step 2
    #     while flash(a): pass
    #         #print(a)
    #     #step 3
    #     a, counter,rc = reset(a,counter)
    #     if rc == 100:
    #         print("sync round: {}".format(s+1))
    #         break
    # print(a)
    # print(counter)
    #     #print(" X ")
    #     #print(a[r][c])
    #     # if a[(row-t):(row+b), (col-l):(col+r)].min() == a[row,col]:
    #     #     print(a[row,col])
    #     #     risk+= a[row,col]+1
    #     #     low_points.append([row,col])