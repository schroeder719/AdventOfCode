import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\3\\input.txt",Integer=False)
print(data)

#data = [199,200,208,210,200,207,240,269,260,263]

def getCount(data):
    count = [0,0,0,0,0,0,0,0,0,0,0,0]
    for l in data:
        pos = 0
        for i in l:
            if i == '1':
                count[pos] += 1
            pos+=1
    # for i in range(len(count)):
    #     if count[i] > 500:
    #         count[i] = 1
    #     else:
    #         count[i] = 0
    return count

def remove(data, pos, val):
    newdata = []
    for i in range(0, len(data), 1):
        if data[i][pos] != val:
            newdata.append(data[i])
    return newdata

d1 = data.copy()
d2 = data.copy()
#count = getCount(d1)
#print(count)
pos = 0
while len(d1) > 1:
    count = getCount(d1)

    if count[pos] >= (len(d1)/2):
        d1 = remove(d1,pos,'0')
    else:
        d1 = remove(d1,pos,'1')
    print(len(d1),pos)
    # if len(d1) <= 7:
    #     print(count)
    #     print(d1)
    #     break
    pos+=1
print(d1)
pos  = 0
while len(d2) > 1:
    count = getCount(d2)

    if count[pos] < (len(d2)/2):
        d2 = remove(d2,pos,'0')
        #print("remove 0")
    else:
        d2 = remove(d2,pos,'1')
        #print("remove 1")
    #print(len(d2),pos)
    #print(d2)
    # if len(d1) <= 7:
    #print(count)
    #     print(d1)
    #     break
    pos+=1
print(d2)
d1i = int(d1[0],2)
d2i = int(d2[0],2)
print(d1i)
print(d2i)
print(d1i*d2i)

#total = len(data)
    
#print(count)
#print(total)

#     r = int(l[0:7].replace('F', '0').replace('B', '1'),2)
#     c = int(l[7:10].replace('L', '0').replace('R', '1'), 2)
#     i = (r*8)+c
#     if i > max:
#         max = i
#     seats.remove(i)
#     print("row: {} col: {} id: {}".format(r,c,i))
# print(max)
# #optional
# s = seats.copy()
# for i in seats:
#     if i-1 in seats or i+1 in seats:
#         s.remove(i)
# print("My seat: {}".format(s[0]))