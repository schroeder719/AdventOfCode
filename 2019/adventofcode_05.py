def prettyprint(code, p, n=10):
    if n is 0:
        start = 0
        end = len(code)
    else:
        start = max(p-n, 0)
        end = min(len(code), p+n)
    
    print("[",end="")
    for i in range (start,end):
        if i == p: print("({})".format(i), end="\t")
        else: print("{}".format(i), end="\t")
        
    print("]")
    print("[",end="")
    for i in range (start,end):
        print("{},".format(code[i]), end="\t")
    print("]")

def intcode(code):
    debug = False
    p = 0
    if debug: prettyprint(code,0,0)
    done = False
    while not done:
        if debug: print("p: {}".format(p))
        code_str = str(code[p]).zfill(5)
        if debug: print(code_str)
        op = int(code_str[3])*10 + int(code_str[4])
        m1 = int(code_str[2])
        m2 = int(code_str[1])
        m3 = int(code_str[0])
        if debug: 
            print("Op: {} m1: {} m2: {} m3: {}".format(op,m1,m2,m3))
            prettyprint(code, p)
        for i in code:
            if type(i) != type(int(1)):
                print("Type error in intcode!!!")
        if op == 1: #add
            if debug: print("Add")
            d = code[p+3]
            
            if m1 == 0:
                o1 = int(code[p+1])
            else:
                o1 = p+1
                
            if m2 == 0:
                o2 = int(code[p+2])
            else:
                o2 = p+2

            code[d] = int(code[o1]) + int(code[o2])
            p+=4
        elif op == 2: #multiply55
            if debug: print("multiply")
            d = code[p+3]
            
            if m1 == 0:  o1 = int(code[p+1])
            else:        o1 = p+1
                
            if m2 == 0:  o2 = int(code[p+2])
            else:        o2 = p+2    

            code[d] = code[o1] * code[o2]
            if debug: print("o1={} o2={} d={}  cod[d]={}".format(o1,o2,d,code[d]))
            p+=4
        elif op == 3: #input
            if debug: print("Input: ")
            val = input("$: ")
            d = code[p+1]
            code[d] = int(val)
            p+=2
        elif op == 4: #output
            if debug: print("Output")
            if m1 == 0:
                #print("a")
                val = code[code[p+1]]
            else:
                #print("b")
                val = code[p+1]
            #print(code)
            print("output: {}".format(val))
            p+=2
        elif op == 5: #jump-if-true
            if debug: print("jump-if-true")
            if m1 == 0:
                o1 = code[p+1]
            else:
                o1 = p+1
            
            if m2 == 0:
                o2 = code[p+2]
            else:
                o2 = p+2
            if debug: print("{} {} {} {} d:{}".format(o1,o2,code[o1], code[o2],d))    
            
            if code[o1] is not  0:
                p = code[o2]
            else:
                p+=3
        elif op == 6: #jump-if-false
            if debug: print("jump-if-false")
            if m1 == 0:
                o1 = code[p+1]
            else:
                o1 = p+1
            
            if m2 == 0:
                o2 = code[p+2]
            else:
                o2 = p+2
            if debug: print("{} {} {} {} d:{}".format(o1,o2,code[o1], code[o2],d))    
            
            if code[o1] is  0:
                p = code[o2]
            else:
                p+=3
        elif op == 7: #less than
            if debug: print("less than")
            if m1 == 0:
                o1 = code[p+1]
            else:
                o1 = p+1
                
            if m2 == 0:
                o2 = code[p+2]
            else:
                o2 = p+2
            
            d = code[p+3]
            
            if code[o1] < code[o2]:
                code[d] = 1
            else:
                code[d] = 0
             
            p+=4
            
        elif op == 8: #equals
            if debug: print("equals")
            if m1 == 0:
                o1 = int(code[p+1])
            else:
                o1 = p+1
                
            if m2 == 0:
                o2 = int(code[p+2])
            else:
                o2 = p+2
            
            d = code[p+3]
            #print("{} {} {} {} d:{}".format(o1,o2,code[o1], code[o2],d))
            if int(code[o1]) == int(code[o2]):
                code[d] = 1
                #print("a")
            else:
                #print("b")
                code[d] = 0
            p+=4
        elif code[p] == 99:
            done = True
        else:
            print("error")
            return -1

    return code[0]
print("1. AOC 5b Test 1")
print("2. AOC 5b Test 2")
print("3. AOC 5b Test 3")
print("4. AOC 5b Test 4")
print("5. AOC 5b Test 5")
print("6. AOC 5b Test 6")
print("7. AOC 5b Test 7")
print("8. AOC 5b puzzle - enter 0 at prompt")

codebank = [
    [],
    [3,9,8,9,10,9,4,9,99,-1,8], # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not)
    [3,9,7,9,10,9,4,9,99,-1,8], # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    [3,3,1108,-1,8,3,4,3,99], #  Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    [3,3,1107,-1,8,3,4,3,99], # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    #Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:
    [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], #(using position mode)
    [3,3,1105,-1,9,1101,0,0,12,4,12,99,1], #(using immediate mode)
    [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31, # The above example program uses an input instruction to ask for a single number. 
    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,   # The program will then output 999 if the input value is below 8, output 1000 
    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99],    # if the input value is equal to 8, or output 1001 if the input value is greater than 8.
    [3,225,1,225,6,6,1100,1,238,225,104,0,1101,61,45,225,102,94,66,224,101,-3854,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,
    224,223,1101,31,30,225,1102,39,44,224,1001,224,-1716,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,92,41,225,101,90,
    40,224,1001,224,-120,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,51,78,224,101,-129,224,224,4,224,1002,223,8,223,1001,
    224,6,224,1,224,223,223,1,170,13,224,101,-140,224,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,14,58,225,1102,58,29,225,
    1102,68,70,225,1002,217,87,224,101,-783,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,19,79,225,1001,135,42,224,1001,
    224,-56,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,2,139,144,224,1001,224,-4060,224,4,224,102,8,223,223,101,1,224,224,1,223,
    224,223,1102,9,51,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,
    1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,
    0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,102,2,223,223,1006,
    224,329,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,107,677,677,224,1002,223,2,223,1005,224,359,101,1,223,
    223,1107,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,1007,677,
    677,224,1002,223,2,223,1006,224,404,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,419,1001,223,1,223,8,226,226,224,102,2,223,
    223,1006,224,434,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,464,
    101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,494,101,1,223,223,7,677,
    226,224,102,2,223,223,1005,224,509,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,524,101,1,223,223,8,226,677,224,1002,223,2,223,
    1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,569,1001,
    223,1,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,226,
    677,224,102,2,223,223,1006,224,614,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,107,226,226,224,1002,223,
    2,223,1006,224,644,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,107,677,226,224,102,2,223,223,1005,224,674,
    1001,223,1,223,4,223,99,226]]

val = int(input("$: "))
#code_test = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
intcode(codebank[val])
        