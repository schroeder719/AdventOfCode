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

#print(alpha)
#print(len(alpha))
total = 0
g = ""
count = []
for i in range (0, 26):
    count.append(0)
gl = 0
cnt = count.copy()

#print(cnt)
t = 0
for line in data:
    if line == "":
        #print(cnt)
        #print(gl)
        t = 0
        for i in cnt:
            if i == gl:
                t+=1
        print(t)
        total+=t

        gl= 0
        cnt = count.copy()
    else:
        gl+=1
        for c in line:
            cnt[ord(c)-97] +=1

print("total: {}".format(total))

