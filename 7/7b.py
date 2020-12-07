import os
import re
import queue

def readfile(filename,lines=True):
    with open(os.path.join(os.getcwd(),filename)) as f:
        data = f.read()
    if lines:
        data = data.split('\n')
    return data

def prt(line,*argv):
    if '@' in line:
        line = line.replace('@',"{}")
        
    elif line == "":
        for arg in argv:
            line += "{} "
        line=line[0:-1]
    print(line.format(*argv))



# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data, weight=0): 
        self.vertex = data 
        self.weight = weight
        self.next = None

# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, size): 
        self.V = size
        self.graph = [None] * self.V

    # Function to add an edge in an directed graph 
    def add_edge(self, src, dest, weight=0):
        # Adding the node to the source node 
        node = AdjNode(dest,weight) 
        temp = self.graph[src]
        if temp is None:
            self.graph[src] = node
        else:
            while temp.next: 
                temp = temp.next
            temp.next = node 

    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}[{}]".format(temp.vertex,temp.weight), end="") 
                temp = temp.next
            print(" \n") 

    def print_graph_names(self,ib): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(ib[i]), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}[{}]".format(ib[temp.vertex],temp.weight), end="") 
                temp = temp.next
            print(" \n") 


    def required(self,id):
        total = 1
        temp = self.graph[id]
        if temp is not None:
            while temp:
                req = self.required(temp.vertex)
                #print("{}+={}*{}".format(total,temp.weight,req))
                total += temp.weight * req 
                
                temp = temp.next
            
        return total 
    
    

# Driver program to the above graph class 
if __name__ == "__main__": 
    data = readfile("2020\\7\\input.txt")
    idx = 0
    bi = dict()
    ib = dict()
    for line in data:
        r = line.split(" bags contain ")
        if r[0] not in bi:
            bi[r[0]] = idx
            ib[idx] = r[0]
            idx+=1
        rr = r[1].split(", ")
        for j in rr:
            e = re.match(r"^(\d+) ([a-z ]+) bags?\.?$",j)
            if e:
                g = e.groups()
                if g[1] not in bi:
                    bi[g[1]] = idx
                    ib[idx] = g[1]
                    idx+=1
            elif j != "no other bags.":
                print("e error >{}<".format(j))

    V = len(bi)
    graph = Graph(V)
    for line in data:
        r = line.split(" bags contain ")
        id = bi[r[0]]
        rr = r[1].split(", ")
        for j in rr:
            e = re.match(r"^(\d+) ([a-z ]+) bags?\.?$",j)
            if e:
                g = e.groups()
                graph.add_edge(id,bi[g[1]],int(g[0]))
            elif j != "no other bags.":
                print("e error >{}<".format(j))                
                exit

    result = graph.required(bi['shiny gold']) - 1
    print(result)
