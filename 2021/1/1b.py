import os

AOC_2020="AOC\\2020"
AOC_2019="AOC\\2019"
AOC_COMMON="AOC\\common"

def readfile(filename,lines=True, Integer=False):
    with open(os.path.join(os.getcwd(),filename)) as f:
        data = f.read()
    if lines:
        data = data.split('\n')
    if Integer:
        data = [int(i) for i in data]
    return data

def prt(line,*argv):
    if '@' in line:
        line = line.replace('@',"{}")
        
    elif line == "":
        for arg in argv:
            line += "{} "
        line=line[0:-1]
    print(line.format(*argv))


def test():
    a = "1"
    b = "2"
    c = "3"

    prt("@ @ @ ",a, b,c )
    prt("", a,b,c)

seats = []
for j in range (0,900):
    seats.append(j)
print(seats)

data = readfile("d:\\AdventOfCode\AOC\\2021\\1\\input.txt",Integer=True)

#data = [199,200,208,210,200,207,240,269,260,263]

max = 0
count = 0
last = 0
for i in range(3,len(data)+1):
    next = sum(data[i-3:i])
    
    if last > 0:
        if next > last:
            count+=1
    print("{}, {}, {}".format(next,last,count))
    last = next
print(count)
    
    
#     l=l.strip()       
#     r = int(l[0:7].replace('F', '0').replace('B', '1'),2)
#     c = int(l[7:10].replace('L', '0').replace('R', '1'), 2)
#     i = (r*8)+c
#     if i > max:
#         max = i
#     seats.remove(i)
#     print("row: {} col: {} id: {}".format(r,c,i))
# print(max)
# #optional
# s = seats.copy()
# for i in seats:
#     if i-1 in seats or i+1 in seats:
#         s.remove(i)
# print("My seat: {}".format(s[0]))