import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy
import math

info = dict()

#data = u.readfile(u.AOC_2020 + "\\21\\input_ex.txt")
data = u.readfile(u.AOC_2020 + "\\21\\input.txt")
food = []
for line in data:
    r1 = line.split(" (contains")
    ing = r1[0].split(" ")
    als = r1[1][:-1].split(",")
    food.append([ing,set(als)])
all_ingredients = set()
for f in food:
    all_ingredients = all_ingredients.union(f[0])
    for alg in f[1]:
        
        if alg in info.keys():
            s = info[alg]
            info[alg] = s.intersection(f[0])
        else:
            s = set(f[0])
            info[alg] = s
        
  

#print(food)
print(all_ingredients)
ingredients_witout_alergies = all_ingredients.copy()
for k in info.keys():
    print("{} : {}".format(k,info[k]))
    ingredients_witout_alergies = ingredients_witout_alergies - info[k]
print(ingredients_witout_alergies)

count = 0
for f in food:
    for ing in f[0]:
        if ing in ingredients_witout_alergies:
            count+=1
print(count)