raw = """*******
*##.##*
*.#.##*
*##..#*
*#.#..*
*.###.*
*******"""
# raw = """*******
# *....#*
# *#..#.*
# *#..##*
# *..#..*
# *#....*
# *******"""

map = raw.split("\n")
POI = {}
# for y in range(len(map)):
#     for x in range(len(map[y])):
#         if map[y][x] not in ['#','.']:
#             #print("{}: ({},{})".format(map[y][x],x,y))
#             POI[map[y][x]] = Pos(x,y)
#         #print(map[y][x], end="")
#     #print("")


#print("{}: ({},{})".format('@',POI['@'].x,POI['@'].y))
buffer = [['#' for i in range(len(map[j]))] for j in range(len(map))]
new_buffer = [[0 for i in range(len(map[j]))] for j in range(len(map))]
div = [[0 for i in range(len(map[j]))] for j in range(len(map))]
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
while not done:
    for y in range(1,len(map)-1):
        for x in range(1,len(map[y])-1):
            count = 0
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
            if buffer[y][x] == '.' and (new_buffer[y][x] == 1 or new_buffer[y][x] == 2):
                buffer[y][x] = '#'
                print("B", end='')
            elif buffer[y][x] == '#' and new_buffer[y][x] != 1:
                buffer[y][x] = '.' 
                print("D", end='')
            else:
                print("L", end='')
        print("")
    
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
    for i in hist:
        if i == diversity:
            done = True
    hist.append(diversity)
    print(diversity)


    # inpt = input()
    # if inpt == 'q':
    #     done = True
#print(buffer)

