import os
import re
from typing import Deque
import common.util as u
import numpy as np
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\12\\input.txt",Integer=False)
  

# Function to check if mat[row][col]
# is unvisited and lies within the
# boundary of the given matrix
def isValid(target,path):
    #global edges
    #global nds
    global nodes
     
    if target.islower():
        if nodes[target] == 0:
            return False
    return True
 
def load_graph(edg,nds,data):
    for d in data:
        a = d.split("-")
        for j in range(len(a)):
            if not a[j] in nds.keys():
                if a[j].islower():
                    nds[a[j]] = 1
                else:
                    nds[a[j]] = -1

        if a[0] in edges.keys():
            i = edges[a[0]]
            if not a[1] in i:
                i.append(a[1])
                edges[a[0]] = i
        else:
            edges[a[0]] = [a[1],]

        if a[1] in edges.keys():
            i = edges[a[1]]
            if not a[0] in i:
                i.append(a[0])
                edges[a[1]] = i
        else:
            edges[a[1]] = [a[0],]
    nds['start'] = 1
    nds['end'] = 1

# Function to perform DFS
def BFS(s,d, nodes, edges, path):   
    # Initialize a stack of pairs and
    # push the starting cell into it
    global count
    global all_paths
    
    if s.islower():
        nodes[s] -=1

    path.append(s)       

    if s == d:
        #print(path)
        all_paths.add(",".join(path))
        count+=1
    else:            
        # Push all the adjacent cells
        for i in edges[s]:
            if isValid(i,path):
                BFS(i,d,nodes,edges,path)
    path.pop()
    nodes[s] +=1
    # if s == 'start' or s == 'end':
    #     nodes[s] = 1
    # elif s.islower():
    #     nodes[s] = 2

edges = {}
nodes = {}

load_graph(edges,nodes,data)

print(edges)
print("")
print(nodes)
count = 0
all_paths = set()

for k in nodes.keys():
    if k.islower() and k != 'start' and k != 'end':     
        nodes[k] = 2        
        path = []
        BFS('start','end',nodes,edges,path)
        nodes[k] = 1

for i in all_paths:
    print(i)
print(len(all_paths))