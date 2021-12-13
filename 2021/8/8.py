import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\8\\input.txt",Integer=False)
count = [0]*8

def counter(words):
    print(words)
    for w in words:
        print(w, len(w))
        count[len(w)]+=1
    


for r in data:
    val = r.split("|")
    counter(val[1][1:].split(" "))
print(count)
# 1, 4, 7, or 8 
one = 2
four = 4
seven = 3
eight = 7

print(count[one] + count[four] + count[seven] + count[eight])


# for i in data[0]:
#     if i != ',':
#         fish.append(int(i))
# print(fish)
# print("After {} days: {}\n".format(0,len(fish)))
# for d in range(256):
#     for f in range(len(fish)):
#         if fish[f] == 0:
#             fish.append(8)
#             fish[f] = 6
#         else:
#             fish[f] -= 1
#     if d % 8 == 7:
#         print("After {} days: {}\n".format(d,len(fish)))
# print("After {} days: {}\n".format(d,len(fish)))
# #b = len(fish)        
# #total = b**16
# #print(total)


