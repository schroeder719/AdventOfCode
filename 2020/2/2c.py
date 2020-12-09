import os
from colorama import Fore, Back, Style, init
import re

class Password:
    def __init__(self, line):
        #cre = re.compile(r"^(\d+)-(\d+) ([a-z]{1}): ([a-z]+)")
        #result = cre.match(string=line)
        result = re.match(r"^(\d+)-(\d+) ([a-z]{1}): ([a-z]+)", line)
        if result:
            #print("{} matches".format(result.groups()))
            self.one = int(result.group(1))
            self.two = int(result.group(2))
            self.reqchr = result.group(3)
            self.pass_string = result.group(4)
        else:
            print(line)
            print("no match")
            exit(1)

        #print("Must have between {} and {} {}'s in {}".format(self.min, self.max,self.reqchr,self.pass_string))

    def test(self):
        #count = self.pass_string.count(self.reqchr)
        first = self.pass_string[self.one-1] == self.reqchr
        second = self.pass_string[self.two-1] == self.reqchr

        if first and second:
            return 0
        elif first or second:
            return 1
        else:
            return 0
    
    def print(self):
        for i in range(0,len(self.pass_string)-1):
            found = False
            if i == self.one-1:
                if self.pass_string[i] == self.reqchr:
                    print(Fore.GREEN + self.pass_string[i],end="")
                    found = True
                else:
                    print(Fore.YELLOW + self.pass_string[i],end="")
            elif i == self.two-1:
                if self.pass_string[i] == self.reqchr:
                    if found:
                        print(Fore.RED + self.pass_string[i],end="")
                    else:
                        print(Fore.GREEN + self.pass_string[i],end="")
                elif not found:
                    print(Fore.RED + self.pass_string[i],end="")
            else:
                print(self.pass_string[i],end="")
        print("")

total_valid = 0
total = 0
init(autoreset=True)
with open(os.path.join(os.getcwd(), "2020\\2\\input_2a.txt")) as f:
    for line in f:
        total+=1
        p = Password(line)
        total_valid += p.test()
        p.print()

print("{} are valid of {}".format(total_valid,total))
        

# data.sort()

# end = len(data)-1
# print ("End is {}".format(end))
# while solved == False:
#     res = data[x] + data[y] + data[z]
#     a = data[x]
#     b = data[y]
#     c = data[z]
#     #print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#     if res == 2020:
#         solved = True
#         print("{},{},{}:{}+{}+{}=2020".format(x,y,z,a,b,c))
#         print("{}x{}x{}={}".format(a,b,c,a*b*c))

#     # else:
#     #     if x == end-2:
#     #         print("not found")
#     #         exit(1)
#     #     elif y == end-1:
#     #         x+=1
#     #         y= x+1
#     #         z= y+1
#     #     elif z == end:
#     #         y+=1
#     #         z=y+1
#     #     else:
#     #         z+=1

#     elif res > 2020:
#         print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#         y+=1
#         z=y+1
#         print("next y")
#         print("({},{},{})".format(x,y,z))   
#     else:
#         print("{},{},{}:{}+{}+{}={}".format(x,y,z,a,b,c,res))
#         z+=1
#     if z == end:
#         if y == end-1:
#             x+=1
#             y=x+1
#             z=y+1
#             print("next x - b")
#         else:
#             y+=1
#             z=y
#             print("next y") 
    

