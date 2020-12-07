import os

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


data = readfile("2020\\6\\input.txt")
s = None
total = 0
for line in data:
    if line == "":
        total += len(s)
        s = None
    else:
        if s is None:
            s = set(line)
        else:
            # part 1
            s = set(line).union(s)
            # part 2
            #s = set(line).intersection(s)
        

print("total: {}".format(total))

