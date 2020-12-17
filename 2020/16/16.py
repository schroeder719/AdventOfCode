import os
import re
import common.util as u
#import common.comp as c
import logging
import time


data = u.readfile(u.AOC_2020 + "\\16\\input.txt")
#data = u.readfile(u.AOC_2020 + "\\16\\input_ex.txt")

class Field:

    def __init__(self,info):
        self.name = info[0]
        ranges = info[1:]
        r = []
        for i in ranges:
            r.append(int(i))
        self.ranges = r
        self.index = -1

        if len(self.ranges) != 4:
            print("init error:{}".format(self.ranges))
            exit(1)
    def setIndex(self, idx):
        self.index = idx

    def setId(self,id):
        self.id = id


    def check(self, num):
        val =  (num >= self.ranges[0] and num <= self.ranges[1]) or (num >= self.ranges[2] and num <= self.ranges[3])
        return val

    def print(self):
        print("{} {} {} {}".format(self.name,self.ranges, self.id, self.index) )

# def caf(i):
#     for f in fields:
#         if not f.check(int(i)):
#             return False

class Fields:

    def __init__(self):
        self.fields = []

    def addfield(self, field):
        field.setId(len(self.fields)+1)
        self.fields.append(field)
        self.possibleIndex = []
    
    def setIndex(self,id,index):
        for f in self.fields:
            if f.id == id:
                f.index = index

    #returns true if all fields in the ticket 
    def checkTicket(self,ticket):
        sum = 0
        all_valid = True
        for v in ticket:
            valid = False
            for f in self.fields:
                if f.check(int(v)):
                    valid = True
                    break
            if not valid:
                all_valid = False
                sum+=int(v)
        return all_valid,sum

    def print(self):
        for f in self.fields:
            f.print()

    def getUnfound(self):
        uf = []
        for f in self.fields:
            if f.index == -1:
                uf.append(f.id)
        return uf
    
    def getFound(self):
        ff = []
        for f in self.fields:
            if f.index > 0:
                ff.append(f.id)
        return ff

    def addIndex(self,index):
        self.possibleIndex[index]
    
    def count(self):
        return len(self.fields)

    # return list of fields that work for that column
    def checkColumn(self,tickets,col):
        tf  = []
        for t in tickets:
            tf.append(t[col])
        res = []
        for f in self.fields:
            all_good = True
            for v in tf:
                if not f.check(v):
                    all_good = False
                    break
            if all_good:
                res.append(f.id)
        return res
    





        
fields = Fields()
tickets = []
sum = 0
step = 0
for line in data:
    #print("Step {}".format(step))
    if line == "":
        step+=1
        continue
    elif line == "your ticket:" or line == "nearby tickets:":
        continue

    if step == 0:
        match = re.match(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$", line.strip())
        if match:
        #print(match.groups())
            fields.addfield(Field(match.groups()))
        else:
            print("no match: {}".format(line))
        
    elif step == 1:
        my_ticket = line.split(",")

    elif step == 2:
        res = line.split(",")
        v, s = fields.checkTicket(res)
        sum += s
        if v:
            t = []
            for i in res:
                t.append(int(i))
            tickets.append(t)
        #else:
        #    print("invalid: "+ str(res))

if sum != 23925:
    print("Part1 Error")
    exit(1)
#fields.print()

uf = fields.getUnfound()
ff = fields.getFound()
print(uf)
print(ff)

print("")

for t in tickets:
    print(t)
all = {}
column = {}
# col == field number
for col in range(fields.count()):
    r = fields.checkColumn(tickets,col)
    all[len(r)] = r
    column[len(r)] = col+1

for key in all.keys():
    print(all[key])

print(all.keys())
print(column.keys())

for key in column.keys():
    print(column[key])

for i in range(1,fields.count()+1):
    l = all[i] # l is list of fields that work for column (i)
    for f in ff:
        l.remove(f)
    if len(l) == 1:
        found = l[0] # remaining field that works for column (i)
        uf.remove(found)
        ff.append(found)
        fields.setIndex(found, column[i])

        print("{}: found: {}".format(found, column[i]))
    else:
        print("error 185")
        exit(185)

    # count = 0
    # last = 0
    # for a in range(len(all)):
    #     if i in all[a]:
    #         count+=1
    #         last = i
    # #if count == 1:
    # print ("{} {}".format(i,count))
    # fields.setIndex(i, count)

    
    

    # tf = get_col(tickets,col)
    # for f in uf:
    #     all_good = True
    #     field.ceck
    #     fields.checkTicket
    #     for t in range(len(tickets)):
    #         g = tickets[t]
    #         v = int(g[col])
    #         if not fields[f].check(v):
    #             all_good = False
    #             print("{} is not {} [{}]".format(v, fields[f].name, fields[f].ranges))
    #             break
    #     if all_good:
    #         print("Found {}: {}".format(fields[f].name, col))
    #         fields[f].setIndex(col)
    #         ff.append(f)
    #         uf.remove(f)
    #         break
        # else:
        #     print("not {}".format(f))

# print(" ")
total = 1

# for f in fields:
#     if "departure" in f.name:
#         print("{}: {}".format(f.name,my_ticket[f.index]))
#         total*=int(my_ticket[f.index])


print(" ")

for f in fields.fields:
    f.print()

print(" ")

for i in range(len(my_ticket)):
    for f in fields.fields:
        idx = f.index-1
        if idx == i:
            
            if "departure" in f.name:                
                print("{}[{}]: {}".format(f.name,idx,my_ticket[idx]))
                total*=int(my_ticket[idx])

print("{}".format(total))
print("done")

