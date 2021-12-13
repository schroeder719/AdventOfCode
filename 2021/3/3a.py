import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\3\\input.txt",Integer=False)
print(data)

#data = [199,200,208,210,200,207,240,269,260,263]
count = [0,0,1,1,1,1,1,1,1,1,1,1]
count2 = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(count)):
    count[i] = 0
print (count)
total = len(data)
for l in data:
    pos = 0
    for i in l:
        if i == '1':
            count[pos] += 1
        pos+=1
for i in range(len(count)):
    if count[i] > 500:
        count[i] = 1
    else:
        count[i] = 0    
print(count)
print(total)

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