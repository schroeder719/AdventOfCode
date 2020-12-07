import os
import re

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

    # Function to add an edge in an undirected graph 
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

        # Adding the source node to the destination as 
        # it is the undirected graph 
        #node = AdjNode(src, weight)
        #node.next = self.graph[dest] 
        #self.graph[dest] = node 

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

    def count(self,ib,id):
        total = 0
        contains = []
        for i in range(self.V): 
            #print("Adjacency list of vertex {}\n head".format(i), end="") 
            if i == id:
                continue
            temp = self.graph[i] 
            while temp: 
                if temp.vertex == id:
                    #print(" -> {}[{}]".format(ib[temp.vertex],temp.weight), end="") 
                    print("{} contains {}".format(ib[i], ib[id]))
                    if not i in contains:
                        contains.append(i)
                temp = temp.next
        for i in contains:
            total+= self.count(ib, i)
        return total

    def countc(self,ib,id, contains=None,visited=None):
        root = False
        if contains is None:
            root = True
            contains = []
        if visited is None:
            visited = []
        for i in range(self.V):
            if self.graph[i] is None:
                continue
            #print("Adjacency list of vertex {}\n head".format(i), end="") 
            #print(i)
            temp = self.graph[i]
            while temp: 
                if temp.vertex == id:
                    #print(" -> {}[{}]".format(ib[temp.vertex],temp.weight), end="") 
                    print("{} contains {}".format(ib[i], ib[id]))
                    if not i in contains:
                        contains.append(i)
                temp = temp.next
            #visited.append(i)
        for i in contains:
            if i not in visited:
                print("looking in {}".format(ib[i]))
                visited.append(i)
                self.countc(ib, i, contains, visited)
        if root:
            print("contains: {}".format(len(contains)))
            #for i in contains:
            #    print("{}: {}".format(i,ib[i]))


# Driver program to the above graph class 
if __name__ == "__main__": 
    data = readfile("2020\\7\\input.txt")
    idx = 0
    bi = dict()
    ib = dict()
    for line in data:
        r = line.split(" bags contain ")
        #print(r[0])
        if r[0] not in bi:
            bi[r[0]] = idx
            ib[idx] = r[0]
            idx+=1
        rr = r[1].split(", ")
        for j in rr:
            e = re.match(r"^(\d+) ([a-z ]+) bags?\.?$",j)
            if e:
                g = e.groups()
                #print(g[1])
                if g[1] not in bi:
                    bi[g[1]] = idx
                    ib[idx] = g[1]
                    idx+=1
            elif j != "no other bags.":
                print("e error >{}<".format(j))
                
    #for key in bi:
    #    print(key, '->', bi[key])

    V = len(bi)
    graph = Graph(V)
    for line in data:
        r = line.split(" bags contain ")
        #print(r[0])
        id = bi[r[0]]
        rr = r[1].split(", ")
        for j in rr:
            e = re.match(r"^(\d+) ([a-z ]+) bags?\.?$",j)
            if e:
                g = e.groups()
                graph.add_edge(id,bi[g[1]],g[0])
                #print(g[1])
                #if g[1] not in bi:
                #    bi[g[1]] = idx
                #    idx+=1
            elif j != "no other bags.":
                print("e error >{}<".format(j))                
                exit

    
    graph.countc(ib,bi['shiny gold'])
    #graph.print_graph() 
    #for key in bi:
    #    print(key, '->', bi[key])
    # for key in ib:
    #     print(key, '->', ib[key])
    
    #print(ib[4])
    #print(bi['shiny gold'])

# # This code is contributed by Kanav Malhotra 
