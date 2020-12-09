# raw = """*******
# *##.##*
# *.#.##*
# *##..#*
# *#.#..*
# *.###.*
# *******"""
raw = """*******
*....#*
*#..#.*
*#..##*
*..#..*
*#....*
*******"""

map = raw.split("\n")
POI = {}
# for y in range(len(map)):
#     for x in range(len(map[y])):
#         if map[y][x] not in ['#','.']:
#             #print("{}: ({},{})".format(map[y][x],x,y))
#             POI[map[y][x]] = Pos(x,y)
#         #print(map[y][x], end="")
#     #print("")

def get_recursive_count(last_buffer,_x,_y):
    count = 0
    if _x == 2 and _y == 3:
        for y in range(1,6):
            if last_buffer[y][1] == '#':
                count+=1
    if _x == 4 and _y == 3:
        for y in range(1,6):
            if last_buffer[y][5] == '#':
                count+=1
    if _x == 3 and _y == 2:
        for x in range(1,6):
            if last_buffer[1][x] == '#':
                count+=1
    if _x == 3 and _y == 4:
        for x in range(1,6):
            if last_buffer[5][x] == '#':
                count+=1
    return count
#print("{}: ({},{})".format('@',POI['@'].x,POI['@'].y))
buffer = [['#' for i in range(len(map[j]))] for j in range(len(map))]
new_buffer = [[0 for i in range(len(map[j]))] for j in range(len(map))]
div = [[0 for i in range(len(map[j]))] for j in range(len(map))]
last_buffer = new_buffer.copy()
p = 1
for y in range(1,len(div)-1):
    for x in range(1,len(div[y])-1):
        div[y][x] = p
        p = p*2

print(div)

for y in range(len(map)):
    for x in range(len(map[y])):
        buffer[y][x] = map[y][x]


for y in buffer:
    for x in y:
        print(x, end='')
    print("")
# for y in new_buffer:
#     for x in y:
#         print(x, end='')
#     print("")
hist = []
done = False
loop = 0
while not done:
    for y in range(1,len(map)-1):
        for x in range(1,len(map[y])-1):
            if y == 3 and x == 3:
                continue
            count = 0
            count+=get_recursive_count(last_buffer, x,y)
            if buffer[y][x-1] == '#': #left
                count+=1
            if buffer[y][x+1] == '#': #right
                count+=1
            if buffer[y-1][x] == '#': #down
                count+=1
            if buffer[y+1][x] == '#': #up
                count+=1
            new_buffer[y][x] = count
    
    for y in range(1,len(map)-1):
        for x in range(1,len(map[y])-1):
            if y == 3 and x == 3:
                continue
            if buffer[y][x] == '.' and (new_buffer[y][x] == 1 or new_buffer[y][x] == 2):
                buffer[y][x] = '#'
                print("B", end='')
            elif buffer[y][x] == '#' and new_buffer[y][x] != 1:
                buffer[y][x] = '.' 
                print("D", end='')
            else:
                print("L", end='')
        print("")
    last_buffer = buffer.copy()
    for y in new_buffer:
        for x in y:
            print(x, end='')
        print("")           
    for y in buffer:
        for x in y:
            print(x, end='')
        print("")
    diversity = 0
    for y in range(1,len(buffer)-1):
        for x in range(1,len(buffer[y])-1):
            if buffer[y][x] == '#':
                diversity+= div[y][x]
    #for i in hist:
    #    if i == diversity:
    #        done = True
    loop+=1
    if loop == 11:
        done = True
    hist.append(diversity)
    #print(diversity)
    print("---------------------------")


    # inpt = input()
    # if inpt == 'q':
    #     done = True
#print(buffer)

