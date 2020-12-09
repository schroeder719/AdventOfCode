import sys
data = """
2 LFPRM, 4 GPNQ => 2 VGZVD 
1 KXFHM, 14 SJLP => 8 MGRTM
2 HBXVT, 3 HNHC, 5 BDLV => 1 DKTW
2 MGRTM, 8 RVTB => 4 DFMW
2 SJLP => 9 PXTS
1 NXBG => 6 FXBXZ
32 LPSQ => 9 GSDXD
13 LZGTR => 4 ZRMJ
1 FTPQ, 16 CPCS => 5 HNHC
2 THQH, 2 NDJG, 5 MSKT => 4 LRZV
2 BDLV, 9 HBXVT, 21 NXBG => 7 PLRK
16 LNSKQ, 41 KXFHM, 1 DKTW, 1 NCPSZ, 3 ZCSB, 11 MGRTM, 19 WNJWP, 11 KRBG => 1 FUEL
5 FTPQ, 1 HBXVT => 4 BDLV
15 LSDX, 1 GFJW, 1 QDHJT => 4 NKHQV
9 CZHTP, 1 FRPTK => 6 SNBS
17 LFLVS, 2 WCFT => 8 KGJQ
6 CMHLP => 1 SJLP
144 ORE => 3 KQKXZ
3 GFJW, 1 RVTB, 1 GPNQ => 2 NXBG
4 BDLV => 5 CMHLP
2 LSDX => 1 LZGTR
156 ORE => 3 NDJG
136 ORE => 8 MSKT
4 BDLV, 1 NKHQV, 1 RVTB => 7 LNSKQ
1 LRZV, 3 WCFT => 2 HBXVT
5 KGJQ, 1 SWBSN => 7 QHFX
2 DQHBG => 4 LPSQ
6 GSDXD => 3 LSDX
11 RWLD, 3 BNKVZ, 4 PXTS, 3 XTRQC, 5 LSDX, 5 LMHL, 36 MGRTM => 4 ZCSB
8 CPCS => 2 FRPTK
5 NDJG => 3 WCFT
1 GDQG, 1 QHFX => 4 KXFHM
160 ORE => 3 THQH
20 GFJW, 2 DQHBG => 6 RVTB
2 FXBXZ, 1 WNJWP, 1 VGZVD => 5 RWLD
3 DQHBG => 7 SWBSN
7 QHFX => 8 CPCS
14 HBXVT => 3 VCDW
5 FRPTK => 7 NGDX
1 HWFQ => 4 LFLVS
2 CPCS => 6 ZTKSW
9 KGJQ, 8 ZTKSW, 13 BDLV => 6 GDQG
13 LMHL, 1 LZGTR, 18 BNKVZ, 11 VCDW, 9 DFMW, 11 FTPQ, 3 RWLD => 4 KRBG
1 XRCH => 7 GPNQ
3 WCFT => 9 DQHBG
1 FTPQ => 8 CZHTP
1 PBMR, 2 ZTKSW => 2 BNKVZ
2 PLRK, 3 CPCS => 8 ZSGBG
3 NGDX, 3 XRCH => 6 XTRQC
6 ZTKSW, 11 HNHC, 22 SNBS => 9 WNJWP
5 KQKXZ => 8 HWFQ
23 WCFT => 7 PBMR
1 LRZV, 1 QDHJT => 2 GFJW
1 ZSGBG, 5 CGTHV, 9 ZRMJ => 3 LMHL
1 DQHBG => 9 XRCH
1 GDQG, 17 RWLD, 2 KGJQ, 8 VCDW, 2 BNKVZ, 2 WNJWP, 1 VGZVD => 3 NCPSZ
19 SJLP, 3 ZTKSW, 1 CZHTP => 4 LFPRM
14 SNBS => 8 CGTHV
3 DQHBG, 4 WCFT => 1 FTPQ
3 MSKT, 3 NDJG => 5 QDHJT"""

data_test_1 = """
157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

data_test_2 = """
2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF
"""

import multiprocessing as mp
import os

class Recipie:
    def __init__(self, formula):
        self.formula = formula
        self.takes = []
        self.makes = []
        self.output = ""
        self.load(self.formula)
        
        
        
    def load(self,str_formula):
        r = line.split("=>")
        if len(r) != 2:
            print("error in split")
        in_elements_str = r[0]
        out_elements_str = r[1]

        in_elements2 = in_elements_str.split(",")
        out_elements2 = out_elements_str.split(",")
        
        for ele in in_elements2:
            self.takes.append(ele.strip().split(" "))
            
        for ele in out_elements2:
            self.makes.append(ele.strip().split(" "))
        self.output = self.makes[0][1]
        #print("added {}".format(self.output))

class Recipies:
    def __init__(self):
        self.recipies = {}
    
    def add(self,r):
        self.recipies[r.output] = r
        
    def print_all(self):
        for k,v in self.recipies.items():
            print("{} => {}".format(v.takes,v.makes))
    def items(self):
        return self.recipies.items()

    
    def get(self, recipie):
        return self.recipies[recipie]

import threading
import time

class Packet():
    ident = 0
    inv = {}
    def __init__(self, ident, inv):
        self.ident = 0
        self.inv = inv.copy()


class Factory():
    inv = {}
    recipies = {}
    ident = 0
    process = None
    collecting = False
    
    def __init__(self, recipies, ore, ident):
        mp.Process.__init__(self)
        self.inv = {}
        self.recipies = recipies
        self.ORE_STARTED = ore
        self.clear_inventory()
        self.inv["ORE"] = self.ORE_STARTED    
        self.ident = ident
        self.exit = mp.Event()
        #self.inv["ORE"] = 1000000000000
        
    #@classmethod
    #def from_recipies(cls, recipies) -> Factory:
    #    c = cls()
    #    c.recipies = recipies
    #    # we start with an empty inventory
    #    c.clear_inventory()
    #    return c
   
    def clear_inventory(self):
        for k,v in self.recipies.items():
            for i in v.takes:
                self.inv[i[1]] = 0
            for i in v.makes:
                self.inv[i[1]] = 0

    def print_inventory(self):
        for k,v in self.inv.items():
            print("{}:{}".format(k,v))
    
    def print_ore_used(self):
        print("Ore Consumed: {}",self.ORE_STARTED-self.inv["ORE"])
        
    def make(self, resource, debug=False):
        # get needed materials
        if debug: print("Making: " + resource)
        recipie = self.recipies.get(resource)
        for r in recipie.takes:
            while self.inv[r[1]] < int(r[0]):
                self.make(r[1])
            self.inv[r[1]] = self.inv[r[1]] - int(r[0])
        self.inv[recipie.output] = self.inv[recipie.output] + int(recipie.makes[0][0])
        
    def printline(self,in_string):        
        print('\r', end='')                     # use '\r' to go back
        print(in_string, end='')
    
    def make_all(self, resource, queue = None, debug=False):
        try:
            while self.inv["ORE"] > 0:
                self.make("FUEL")
                if int(self.inv["FUEL"]) % 100 == 0:
                    print("{} has made {}".format(self.ident,self.inv["FUEL"]))
        except:
            pass
        print("Total {} made: {}".format(self.ident,self.inv["FUEL"]))
        if queue is not None:
            done = False
            while not done:
                try:
                    
                    p = Packet(self.ident, self.inv)
                    queue.put(p,timeout=1)
                    #print(inv)
                    #print("{} putting inventory".format(self.ident))
                    done = True
                except:

                    time.sleep(2)
            
        
    def set_inv(self, element, val):
        self.inv[element] = val
        print("Set {} to {}".format(element,val))
        
    def start(self, resource, queue=None):
        print("{} has {} ore and is starting".format(self.ident, self.inv["ORE"]))
        self.process = mp.Process(target=self.make_all,args=(resource,queue))
        self.process.start()

    def collect(self,queue):      
        while not self.exit.is_set():
            try:
                p = queue.get(timeout=1)
                print("LF: Recived from {}".format(p.ident))
                self.add_inventory(p.inv)
            except:
                pass
        p = Packet(self.ident, self.inv)
        queue.put(p)

    def start_collecting(self,queue):
        self.process = mp.Process(target=self.collect,args=(queue,))
        self.process.start()

    def stop_collecting(self):
        self.exit.set()
            
    def join(self):
        self.process.join()
        print(str(self.ident) + " done")
        
    
    def get_inventory(self):
        return self.inv
    
    def add_inventory(self, new_inv):
        #print(new_inv)
        for k,v in new_inv.items():
            self.inv[k] = self.inv[k] + new_inv[k]
        #print(self.inv)



if __name__ == '__main__':
    print("started")
    mp.set_start_method('spawn')
    recipies = Recipies()
    for line in data.split('\n'):
        
        if len(line) < 2:
            continue
        
        recipies.add(Recipie(line))

    target_ore = 1000000000000
    num_factories = 20
    factories = []
    #manager = mp.Manager()
    queue = mp.Queue()

    not_ready = True


    last_factory = Factory(recipies, 0, 100)
    last_factory.start_collecting(queue)


    # target_ore_per_factory = target_ore / num_factories
    # if target_ore_per_factory * num_factories != target_ore:
    #     print("math error")
    #     sys.exit(0)
    
    # print("all good")
    
    
    # for f in factories:
    #     last_factory.add_inventory(f.get_inventory())
    #    #last_factory.print_inventory()
    # last_factory.make_all("FUEL")

    # for f in range(num_factories):
    #     factories.append(Factory(recipies, (target_ore / num_factories), f))
                               
    # for f in factories:
    #     print("Starting factory {}".format(f.ident))
    #     f.start("FUEL", queue)
                        
    # for f in factories:
    #    f.join()
    # time.sleep(6)
    # last_factory.stop_collecting()
    # last_factory.join()
    # p = queue.get()
    # print("Recivied from {}".format(p.ident))
    i = {}
    # i["ORE"] = 14368680.0
    # i["NZVS"]= 80
    # i["DCFZ"]= 0
    # i["XJWVT"]= 0
    # i["KHKGT"]= 120
    # i["HKGWZ"]=60
    # i["QDVJ"]= 60
    # i["GPVTF"] =20
    # i["FUEL"]= 82891560
    # i["PSHF"]= 120

    i["LFPRM"]= 50
    i["GPNQ"]= 125
    i["VGZVD"]= 0
    i["KXFHM"]= 25
    i["SJLP"]= 0
    i["MGRTM"]= 100
    i["HBXVT"]= 25
    i["HNHC"]= 0
    i["BDLV"]= 50
    i["DKTW"]= 0
    i["RVTB"]= 75
    i["DFMW"]= 50
    i["PXTS"]= 25
    i["NXBG"]= 0
    i["FXBXZ"]= 100
    i["LPSQ"]= 0
    i["GSDXD"]= 0
    i["LZGTR"]= 0
    i["ZRMJ"]= 50
    i["FTPQ"]= 0
    i["CPCS"]= 75
    i["THQH"]= 50
    i["NDJG"]= 50
    i["MSKT"]= 75
    i["LRZV"]= 25
    i["PLRK"]= 125
    i["LNSKQ"]= 0
    i["NCPSZ"]= 25
    i["ZCSB"]= 50
    i["WNJWP"]= 75
    i["KRBG"]= 50
    i["FUEL"]= 1993250
    i["LSDX"]= 25
    i["GFJW"]= 25
    i["QDHJT"]= 25
    i["NKHQV"]= 0
    i["CZHTP"]= 125
    i["FRPTK"]= 0
    i["SNBS"]= 0
    i["LFLVS"]= 25
    i["WCFT"]= 50
    i["KGJQ"]= 75
    i["CMHLP"]= 50
    i["ORE"]= 11024100
    i["KQKXZ"]= 0
    i["SWBSN"]= 25
    i["QHFX"]= 0
    i["DQHBG"]= 175
    i["RWLD"]= 100
    i["BNKVZ"]= 0
    i["XTRQC"]= 0
    i["LMHL"]= 50
    i["GDQG"]= 25
    i["VCDW"]= 0
    i["NGDX"]= 25
    i["HWFQ"]= 0
    i["ZTKSW"]= 25
    i["XRCH"]= 125
    i["PBMR"]= 50
    i["ZSGBG"]= 50
    i["CGTHV"]= 50

    print(i)

    last_factory.print_inventory()
    #print("")
    last_factory.add_inventory(i)
    last_factory.make_all("FUEL")
    #result = 1000000000000 - last_factory.inv['ORE']
    last_factory.print_inventory()

    print("Done.")
