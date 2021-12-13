import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\2\\input.txt",Integer=False)
print(data)

#data = [199,200,208,210,200,207,240,269,260,263]

h = 0
d = 0
a = 0
reg = re.compile("(forward|down|up) (\d)")
for cmd in data:
    match = reg.match(cmd)
    x = int(match.group(2))
    m = match.group(1)[0]
    if m == 'f':
        h += x
        d += x * a
    elif m == 'd':
        a += x
    elif m == 'u':
        a -= x
print("h: {} d: {}  == {}".format(h,d,h*d))
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