import os

AOC_2021="AOC\\2021"
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