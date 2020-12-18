import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy


#data = u.readfile(u.AOC_2020 + "\\18\\input.txt")
data = u.readfile(u.AOC_2020 + "\\18\\input.txt")


two = "5 + 9 + 3 + ((2 + 8 + 2) + 8 + 9 * (4 * 2 * 5) + 6) * 4"
one = "1 + (2 * 3) + (4 * (5 + 6))"


def calc(expr):
    pos = []
    ci = 0
    while ci < len(expr):
        if expr[ci] == '(':
            pos.append(ci)
            ci+=1
        elif expr[ci] == ')':
            try:
                i1 = int(pos.pop())
            except IndexError:
                print("Index Error")
                exit(1)
            i2 = int(ci)
            ss = calc(expr[i1+1:i2])
            expr = expr[0:i1] + str(ss) + expr[i2+1:]
            if len(pos) > 0:
                ci = pos.pop()
            else:
                ci=0
        else:
            ci+=1
    total = None
    for h in expr.split(" * "):
        terms = h.split(" ")
        val = 0
        for ti in range(len(terms)):
            if ti == 0:
                val = int(terms[ti])
            elif terms[ti] in ['+','*']:
                op = terms[ti]
            else:
                if op == '+':
                    val += int(terms[ti])
                elif op == '*':
                    val *= int(terms[ti])
        if total is None:
            total = val
        else:
            total *=val
    return total

sum = 0
for line in data:
    s = calc(line)
    print(s)
    sum+=s

#sum = calc(two)
print(sum)