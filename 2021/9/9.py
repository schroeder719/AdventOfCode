import os
import re
import common.util as u
import numpy as np
#print(os.getcwd())

data = u.readfile(u.AOC_2021 + "\\9\\input.txt",Integer=False)


ROW = len(data)
COL = len(data[0])
 
# Initialize direction vectors
dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]
vis = [[False for i in range(COL)] for j in range(ROW)]
 
# Function to check if mat[row][col]
# is unvisited and lies within the
# boundary of the given matrix
def isValid(row, col):
    global ROW
    global COL
    global vis
     
    # If cell is out of bounds
    if (row < 0 or col < 0 or row >= ROW or col >= COL):
        return False
 
    # If the cell is already visited
    if (vis[row][col]):
        return False
 
    # Otherwise, it can be visited
    return True
 
# Function to perform DFS
# Traversal on the matrix grid[]
def DFS(row, col, grid):
    global dRow
    global dCol
    global vis
     
    # Initialize a stack of pairs and
    # push the starting cell into it
    st = []
    st.append([row, col])
    count = 0
 
    # Iterate until the
    # stack is not empty
    while (len(st) > 0):
        # Pop the top pair
        curr = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        row = curr[0]
        col = curr[1]
 
        # Check if the current popped
        # cell is a valid cell or not
        if (isValid(row, col) == False) or grid[row][col] == 9:
            continue
 
        # Mark the current
        # cell as visited
        vis[row][col] = True
 
        # Print the element at
        # the current top cell
        #print(grid[row][col], end = " ")
        count+=1
 
        # Push all the adjacent cells
        for i in range(4):
            adjx = row + dRow[i]
            adjy = col + dCol[i]
            st.append([adjx, adjy])
    return count

for i in range(len(data)):
    t = []
    for j in range(len(data[i])):
        t.append(int(data[i][j]))
    data[i] = t
print(data)

a = np.array(data)
risk = 0

low_points = []

for row in range(len(a)):
    if row == 0:
        t=0
        b=2
    elif row == len(a)-1:
        t=1
        b=1
    else:
        t=1
        b=2
        

    for col in range(len(data[row])):
        if col == 0:
            l = 0
            r = 2
        elif col == len(data[row])-1:            
            l = 1
            r = 1
        else:
            l = 1
            r = 2
        
        
        #print(a[row,col], a[(row-t):(row+b), (col-l):(col+r)])
        #print(" X ")
        #print(a[r][c])
        if a[(row-t):(row+b), (col-l):(col+r)].min() == a[row,col]:
            print(a[row,col])
            risk+= a[row,col]+1
            low_points.append([row,col])
print(risk)
supply = 1
basins = []
for lp in low_points:
    print(lp)
    basins.append(DFS(lp[0],lp[1],a))
basins.sort()
print(basins)
supply = 1
for b in basins[-3:]:
    supply *=b
print(supply)

        #    print("{},{}".format(r,c))


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


