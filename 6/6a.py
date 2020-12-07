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

alpha = []
for i in range (97, 123):
    alpha.append(chr(i))

print(alpha)
print(len(alpha))
total = 0
g = ""
for line in data:
    if line == "":
        print(g, end="")
        a = alpha.copy()
        for c in g:
            if c in a:
                a.remove(c)

        t = (26 - len(a))
        total += t
        print(" " + str(t))
        g = ""
    else:
        g+= line

print("total: {}".format(total))

