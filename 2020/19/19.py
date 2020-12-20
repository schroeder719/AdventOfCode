import os
import re
import common.util as u
index = 0
data = u.readfile(u.AOC_2020 + "\\19\\input.txt")

R_TRUE = 1
R_FALSE = 0
R_INDEX = 2

def run(data, rules, rnum):
    global index
    global tracec
    global tracev
    global matched

    rule = rules[rnum]
    tracev.append(rnum)
    # if index >= len(data):
    #     #print(rule)
    #     return R_INDEX
    if "a" in rule:
        try:
            if data[index] == "a":
                #print(data[index],end="")
                matched.append('a')
                index+=1
                tracec.append(rnum)
                return R_TRUE
            else:
                return R_FALSE
        except IndexError:
            return R_INDEX
    elif "b" in rule:
        try:
            if data[index] == "b":
                matched.append('b')
                index+=1
                tracec.append(rnum)
                return R_TRUE
            else:
                return R_FALSE
        except IndexError:
            return R_INDEX
    elif "|" in rule:
        r = rule.split("|")
        ra = r[0].strip().split(" ")
        rb = r[1].strip().split(" ")
        cnt = 0
        try_b = False
        index_before = index
        for r in ra:
            r = int(r.strip())
            rtn = run(data,rules,r)
            if  rtn == R_FALSE: #else run next rule
                try_b = True
                break
            elif rtn == R_INDEX:
                tracec.append(rnum)
                return R_INDEX
            
        if try_b:
            t = index-index_before
            index = index_before
            for j in range(t):
                matched.pop()
             
            assert index == index_before
            for r2 in rb:
                r2 = int(r2.strip())
                rtn = run(data,rules,r2)
                if rtn == R_FALSE:
                    return R_FALSE
                elif rtn == R_INDEX:
                    tracec.append(rnum)
                    return R_INDEX
        tracec.append(rnum)
        return R_TRUE
    else:
        ra = rule.strip().split(" ")
        for r in ra:
            r = int(r.strip())
            rtn = run(data,rules,r)
            if rtn == R_FALSE:
                return R_FALSE
            elif rtn == R_INDEX:
                tracec.append(rnum)
                return R_INDEX
        tracec.append(rnum)
        return R_TRUE
    
def report(line,trace, matched, count,result,file=None):
    if file is None:
        print(line)
        print("".join(matched), end="")
        print(" {} {}".format(result, count))
        print(trace)
    else:
        file.write(line + "\n")
        file.write("".join(matched))
        file.write(" {} {}\n".format(result, count))
        file.write(str(trace) + "\n")


phase = 0
rules = {}
count = 0
count2 =0
matched = []
with open(u.AOC_2020 + "\\19\\out_good.txt","w") as fg:
    with open(u.AOC_2020 + "\\19\\out_bad.txt","w") as fb:
        with open(u.AOC_2020 + "\\19\\out_index.txt","w") as fi:
            for line in data:
                if line == "":
                    phase = 1
                elif phase == 0:
                    r = line.split(":")
                    rules[int(r[0].strip())] = r[1]
                elif phase == 1:
                    index = 0
                    tracec = []
                    tracev = []
                    matched = []
                    rtn = run(line,rules,0)
                    if rtn == R_TRUE:
                        count+=1

                        report(line,tracev,matched,count,"TRUE",fg)
                    elif rtn == R_INDEX:
                        if index >= len(line):
                            if  tracec[-2:] == [31,11] or tracec[-3:] == [31,11,0]:
                                count+=1
                            else:
                                #print(index, len(line))
                                print(tracev[-4:], end="")
                                print(" " + str(tracec[-4:]))
                            
                            #fortytwo = [i for i, x in enumerate(tracec[:-2]) if x == 42]
                            #thirtyone = [i for i, x in enumerate(tracec[:-2]) if x == 31]
#                            if fortytwo[-1] > thirtyone[-1]:
#                                count+=1
#                                pass
                                report(line,tracec,matched,0,"TRUE-INDEX", fi)    
                            # else:
                            #     print(tracev[-10:])
                            #     report(line,tracev,matched,1,"TRUE-INDEX",fi)
                                #report(line,trace,matched,count,"FALSE-INDEX")
                            #    pass

                        else:
                            #report(line,trace,matched,count,"FALSE INDEX >")
                            pass

                    else:
                        #report(line,trace,matched,count,"FALSE")
                        pass
print("count: {}".format(count))
print("count2: {}".format(count2))
            
