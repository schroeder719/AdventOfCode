import os
import re
import common.util as u
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\8\\input.txt",Integer=False)
count = [0]*8

one = 2
four = 4
seven = 3
eight = 7

def counter(words):
    print(words)
    for w in words:
        print(w, len(w))
        count[len(w)]+=1
total = 0  
for r in data:
    val = r.split("|")
    
    p = {}
    words = val[0][:-1].split(" ")
    for w in words:
        ws = set(w)
        #print(ws)
        wl = len(w)
        if wl == 2: # 1
            p[1] = ws
        elif wl == 3: # 7
            p[7] = ws
        elif wl == 4: # 4
            p[4] = ws
        elif wl == 7: # 8
            p[8] = ws
    
    for w in words:
        wl = len(w)
        ws = set(w)
        if wl == 5: # 2,3,5
            if  (p[4]-p[1]).issubset(ws): # this is 5
                p[5] = ws
            else: # 2 or 3
                if p[1].issubset(ws): # this 3
                    p[3] = ws
                else:
                    p[2] = ws
        elif wl == 6: # 0,6,9
            if p[4].issubset(ws): # this is 9
                p[9] = ws
            elif p[1].issubset(ws):
                p[0] = ws
            else: #this is 6
                p[6] = ws
    #print(p)
    # # for i in p:
    # #     if len(i) == 1:
    # #         print("{} is a match!".format(i))
    # #find "a"
    # for i in range(len(p)):
    #     if len(p[i]) == 3:
    #         j = i
    #     if len(p[i]) == 2:
    #         k = i
    # matched[a] = p[j] - p[k]

    # print(matched[a])

    words = val[1][1:].split(" ")
    print(words)
    # for w in words:
    #     print(w)
    #     ws = set(w)
    #     for k in range(10):
    #         if len(ws.intersection(p[k])) == len(ws):
    #             print(k)

    # break

    decoder = {"".join(sorted(list(v))):k for k,v in p.items() }
    val = "".join([str(decoder["".join(sorted(v))]) for v in words])
    print(val)
    total+=int(val)
print(total)
#print(count)
# 1, 4, 7, or 8 


#print(count[one] + count[four] + count[seven] + count[eight])


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


