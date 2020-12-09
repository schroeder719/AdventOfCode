import os
#from colorama import Fore, Back, Style, init
import re


class Passport:
    def __init__(self, data):
        self.fields = {}
        self.load(data)
        print(self.fields)
        

    def load(self,data):
        print(data)
        res = data.split(" ")
        for i in res:
            try:
                res2 = i.split(':')
                self.fields[res2[0]] = res2[1]
                #print(self.fields)
            except:
                print("except:")
                print(data)
                print(res)
                print(res2)
                print(i)
    

    def test(self):
        #rint(self.fields)
        if 'byr' in self.fields and 'iyr' in self.fields and 'eyr' in self.fields and 'hgt' in self.fields and 'hcl' in self.fields and 'ecl' in self.fields and 'pid' in self.fields:
            return True
        return False

    def fulltest(self):
        if not self.test():
            return False

        #byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not re.match(r"\d{4}", self.fields['byr']):
            print("byr0: {}".format(self.fields['byr']))
            return False
        if int(self.fields['byr']) < 1920 or int(self.fields['byr']) > 2002:
            print("byr1: {}".format(self.fields['byr']))
            return False

        #iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not re.match(r"\d{4}", self.fields['iyr']):
            print("iyr0: {}".format(self.fields['iyr']))
            return False
        if int(self.fields['iyr']) < 2010 or int(self.fields['iyr']) > 2020:
            print("iyr1: {}".format(self.fields['iyr']))
            return False
        #eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not re.match(r"\d{4}", self.fields['eyr']):
            print("eyr0: {}".format(self.fields['eyr']))
            return False
        if  int(self.fields['eyr']) < 2020 or int(self.fields['eyr']) > 2030:
            print("eyr1: {}".format(self.fields['eyr']))            
            return False

        #hgt (Height) - a number followed by either cm or in:
        hgt = re.match(r"^(\d+)(cm|in)", self.fields['hgt'])
        if hgt:
            if hgt.group(2) == "cm":
                #If cm, the number must be at least 150 and at most 193.
                if int(hgt.group(1)) > 193 or int(hgt.group(1)) < 150:
                    print("hgt1: {} {} {}".format(hgt, hgt.group(1), hgt.group(2)))
                    return False
            elif hgt.group(2) == "in":
                #If in, the number must be at least 59 and at most 76.
                if int(hgt.group(1)) > 76 or int(hgt.group(1)) < 59:
                    print("hgt2: {}".format(hgt))
                    return False
        else:
            print("hgt3: {}".format(hgt))
            return False

        #hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.match(r"#[0-9a-f]{6}$", self.fields['hcl']):
            print("hcl: {}".format(self.fields['hcl']))
            return False
        
        #ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if not re.match(r"(amb|blu|brn|gry|grn|hzl|oth)", self.fields['ecl']):
            print("ecl: {}".format(self.fields['ecl']))
            return False
        #else:
         #   print("ecl pass: {}".format(self.fields['ecl']))
        #pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not re.match(r"[0-9]{9}$", self.fields['pid']):
            print("pid: {}".format(self.fields['pid']))
            return False
        #cid (Country ID) - ignored, missing or not.
        print(self.fields)
        return True

        
        
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)


class Passports:
    pp=[]

    def __init__(self, filename):
        self.load(filename)


    def load(self, filename):
        with open(filename) as f:
            entry = ""
            for line in f:
                if line.rstrip() == "":
                    if entry != "":
                        p = Passport(entry.strip())
                        self.pp.append(p)
                    entry = ""
                else:
                    entry += ' ' + line.rstrip()
            if entry != "":
                p = Passport(entry.strip())
                self.pp.append(p)

    def Count(self):
        print("There are {} Passports".format(len(self.pp)))
        #print(self.pp)

    def TestAndCountAll(self):
        total = 0
        total_valid = 0
        for p in self.pp:
            total+=1
            r = p.fulltest()
            if r == True:
                total_valid+=1
            elif r != False:
                print("unexpected return")
                exit(1)
        print("Of {} passports, {} are valid".format(total, total_valid))
    
    def show(self):
        for p in self.pp:
            print(p)


    # def display(self):
    #     for y in self.map:
    #         print("".join(y))
                
    
    # def move(self):
    #     self.x+=self.move_x
    #     self.y+=self.move_y
    #     if self.x > self.w-1:
    #         #print("{},{}->".format(self.x,self.y), end='')
    #         self.x -= self.w
    #         #self.y +=1
    #         #print("{},{}".format(self.x,self.y))
    #         #self.display()
    #         #print("")
            
    #     if self.y > self.h-1:
    #         return False,0
        
    #     try:
    #         current = self.map[self.y][self.x]
    #     except:
    #         print("{},{}".format(self.x,self.y))
    #         exit(1)
    #     #print(current,end="")
    #     if current  == '#' or current == 'X':
    #         self.map[self.y][self.x] = 'X'
    #         return True,1
    #     elif current == '.' or current == 'O':
    #         self.map[self.y][self.x] = 'O'
    #         return True,0
    #     else:
    #         print("unexpected: {} at {},{}".format(current,self.x,self.y))
    #         exit(1)
        

    # def run(self):
    #     c = True
    #     trees = 0
    #     while (c):
    #         c, r = self.move()
    #         trees+=r
    #         #if trees > 20:
    #         #    c=False
    #     print("")
    #     print("total trees for {},{}: {} ".format(self.move_x,self.move_y, trees))
    #     return trees
            
            
                


total_valid = 0
total = 0
#init(autoreset=True)
passports = Passports(os.path.join(os.getcwd(), "2020\\4\\input.txt"))
passports.show()
passports.Count()
passports.TestAndCountAll()


