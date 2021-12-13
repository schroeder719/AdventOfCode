import os
from common.util import readfile as rf, prt

seats = []
for j in range (0,900):
    seats.append(j)
print(seats)

data = readfile("2021\\1\\input.txt")

max = 0
for l in data:
    print(l)

#     l=l.strip()       
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