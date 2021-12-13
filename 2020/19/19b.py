import os
import regex
import common.util as u
index = 0
data = u.readfile(u.AOC_2020 + "\\19\\input.txt")
#data = u.readfile(u.AOC_2020 + "\\19\\input_ex.txt")


def buildRE(dataDict):
    def expand(value):
        if not value.isdigit(): return value
        return "(?:" + "".join(map(expand, dataDict[value].split())) + ")"
    r = regex.compile(expand("0"))

    return r


def test(re, line):
    return re.fullmatch(line)



step = 1
rules = {}
count = 0
for line in data:
    if line == "":
        step = 2
        # part2:
        rules["8"] = "42 +"
        rules["11"] = "(?P<R> 42 (?&R)? 31 )"

        re = buildRE(rules)
    elif step == 1:
        x = line.replace('"',"").split(": ")
        rules[x[0]] = x[1].strip()
    elif step == 2:
        if test(re,line):
            count += 1
print ("count: {}".format(count))