#        code_str = str(code[p]).zfill(5)
#        print(code_str)
#        op = int(code_str[3])*10 + int(code_str[4])
#        m1 = int(code_str[2])
#        m2 = int(code_str[1])
#        m3 = int(code_str[0])

#data = "59701570675760924481468012067902478812377492613954566256863227624090726538076719031827110112218902371664052147572491882858008242937287936208269895771400070570886260309124375604950837194732536769939795802273457678297869571088110112173204448277260003249726055332223066278888042125728226850149451127485319630564652511440121971260468295567189053611247498748385879836383604705613231419155730182489686270150648290445732753180836698378460890488307204523285294726263982377557287840630275524509386476100231552157293345748976554661695889479304833182708265881051804444659263862174484931386853109358406272868928125418931982642538301207634051202072657901464169114"
data="80871224585914546619083218645595"
data = data * 3
import time
def getPattern(n,first=False):
    #print("np")
    base_pattern = [0,1,0,-1]
    out_pattern = []
    for i in base_pattern:
        for j in range(n):
            out_pattern.append(base_pattern[i])
    
    if first == True: 
        return out_pattern[1:]
    return out_pattern
# for i in range(len(data)):
#     out_pattern = getPattern(i)
#     print(out_pattern)


start = time.time()
elapsed = 0
prev_total_elapsed = 0
for phase in range(100):
    end = time.time()
    total_elapsed = end-start
    elapsed = total_elapsed - prev_total_elapsed 
    remaining = (99 - phase) * (elapsed)
    #print("phase {} starting. {} elapsed since last phase, est {} remaining".format(phase,elapsed,remaining))
    prev_total_elapsed = total_elapsed
    result = ""
    first = True
    for ele in range(1,len(data)+1): 
        sum = 0
        pat = getPattern(ele, True)
        pi = 0
        for d in data:
#            print("{}*{} + ".format(int(d),pat[pi]), end="")
            sum+= int(d)*pat[pi]
            pi+=1
            if len(pat) == pi:
                pi = 0
                pat = getPattern(ele)
        ssum = str(abs(sum)%10)
        #print("{}:{}".format(sum,ssum))
#        print("= {}({})".format(ssum,sum))
        result+= ssum[0]
        
    #print("{}:{}".format(phase,result))
    if (len(result) != len(data)):
        print("Size error!")
    data = result
for i in range(len(data)):
    if i%(int(len(data)/3))==0:
        print(" ", end="")
    print(i, end="")
    
print("")
offset = 0
for i in range(7):
    offset+= int(data[i])
print("offset: {}".format(offset))
print(data[offset:offset+8])