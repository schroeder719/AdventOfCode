
import os
import re
import common.util as u
#import common.comp as c
import logging
import time
import copy


#data = u.readfile(u.AOC_2020 + "\\18\\input.txt")
raw = u.readfile(u.AOC_2019 + "\\18_input_ex.txt")

class Pos:
    x = 0
    y = 0
    
    DIR_NORTH = 1
    DIR_SOUTH = 2
    DIR_WEST  = 3
    DIR_EAST  = 4
    
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def north(self):
        self.y-=1
    def south(self):
        self.y+=1
    def east(self):
        self.x+=1
    def west(self):
        self.x-=1
    def move(self,direction):
        if direction == self.DIR_NORTH:
            self.north()
        elif direction == self.DIR_SOUTH:
            self.south()
        elif direction == self.DIR_EAST:
            self.east()
        elif direction == self.DIR_WEST:
            self.west()


# A simple Python program to introduce a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data, position): 
        self.data = data  # Assign data 
        self.adj = []
        self.pos = position
        self.id =0
        self.dist = 0
        self.predeccesor = None

    def add_neighbor(self,node):
            self.adj.append(node)
        
import queue    
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.POI = {}
        self.count = 1
        self.nodes = []
        self.keys = []
        self.locks = []

    def DFS(self,node):
        if node.id == 0:
            node.id = self.count
            if node.data != '.':
                print("Adding {} to the POI dictionary".format(node.data))
                self.POI[node.data] = node
            self.count+=1
            #print("{}({},{}) is finding neighbors".format(self.data,self.pos.x,self.pos.y))
            neighbors = [nodes[node.pos.y][node.pos.x-1],
                 nodes[node.pos.y-1][node.pos.x], 
                 nodes[node.pos.y][node.pos.x+1], 
                 nodes[node.pos.y+1][node.pos.x]]

            for n in neighbors:
                if n is not None:
                    #print(n.data,end="")
                    node.add_neighbor(n)
                    if n.id == 0:
                        self.DFS(n)

    def build_tree_dfs(self,nodes):
        for y in range(len(nodes)):
            for x in range(len(nodes[y])):
                n = nodes[y][x]
                if n != None:
                    self.nodes.append(n)
                    if ord(n.data) >= 65 and ord(n.data) <= 90:
                        self.locks.append(n.data)
        self.count = 1
        for n in self.nodes:
            #print(n.data,end="")
            if n.id == 0:
                self.DFS(n)
            
        
    def printPOI(self):
        print("# of POIs: {}".format(len(self.POI.items())))
        for k,v in self.POI.items():
            print("{} is at ({},{}) is {} steps".format(k,v.pos.x,v.pos.y,v.dist))

    def shortestPath(self,first_node):
        for n in self.nodes:
            n.dist = 10000000
            #print(n.data, end="")

        first_node.dist = 0
        q = queue.Queue()
        q.put(first_node)
        while not q.empty():
            v = q.get()
            for adjnode in v.adj:
                #print(adjnode.data,end="")
                #if ord(adjnode.data) >= 65 and ord(adjnode.data) <= 90:
                if adjnode.data in self.locks:
                    weight = 1000
                else:
                    weight = 1
                if adjnode.dist > v.dist + weight:
                    adjnode.dist = v.dist + weight
                    adjnode.predeccesor = v
                    #print("adding {}".format(adjnode.data))
                    q.put(adjnode)

    def nextNode(self, current):
        m = Node("?",Pos(0,0))
        m.dist = 10000
        if not self.POI:
            return None

        try:
            del self.POI[current.data]
        except:
            print("{} is not a POI".format(current.data))
        for k,v in self.POI.items():
            if v.dist < m.dist:
                m = v
        if m.dist == 10000:
            print(self.POI.items())
        return m
map = []
for line in raw:
    l = []
    l[:0]=line
    map.append(l)

nodes = [[None for i in range(len(map[j]))] for j in range(len(map))]
ll  = LinkedList()
first = True
count=0

POI = {}
node_count = 0
for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] not in ['#','.']:
            #print("{}: ({},{})".format(map[y][x],x,y))
            POI[map[row][col]] = Pos(col,row)
        if map[row][col] != '#':
            #print(map[y][x])
            count+=1
            nodes[row][col] = Node(map[row][col], Pos(col,row))
            node_count+=1

print("{} {}".format(count,node_count))
ll.head = nodes[POI['@'].y][POI['@'].x]
ll.build_tree_dfs(nodes)
print(ll.count)

done = False
total = 0
n= ll.head
while not done:
    ll.shortestPath(n)
    n = ll.nextNode(n)
    if n is None or n.dist == 10000:
        break
    print("Next Node is {} at {} steps".format(n.data,n.dist))
    total+=n.dist
    if ord(n.data) >= 97 and ord(n.data) <= 122:
        try:
            ll.keys.append(n.data)
            if n.data.upper() in ll.locks:
                ll.locks.remove(n.data.upper())
            else:
                print("{} not in locks".format(n.data.upper()))
        except ValueError:
            print(n.data)
            print(ll.keys)
            print(ll.locks)
            exit(1)
    if ord(n.data) >= 65 and ord(n.data) <= 90:
        print("opened door: {}".format(n.data))
print("{} total steps".format(total))
