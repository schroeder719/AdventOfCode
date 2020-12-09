import queue
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

class Intcode():
    code = []
    input_que = None
    output_que = None
    debug = False
    relative_base = 0
    program_counter = 0

    NO_ERROR = 0
    COMPLETE = 5
    INPUT_NEEDED = 10
    OUTPUT_AVAILABLE = 20

    def __init__(self, code):
        self.code = code + 5000 * [0,]
        self.relative_base = 0
        self.program_counter = 0
        self.input_que = queue.Queue()
        self.output_que = queue.Queue()
        self.debug=True

    def input(self, val):
        self.input_que.put_nowait(val)

    def output(self):
        return self.output_que.get()

    def run(self):
        blocked = False 
        while not blocked:
            rc = self.cycle()
            if rc in [self.INPUT_NEEDED, self.OUTPUT_AVAILABLE, self.COMPLETE]:
                blocked = True
        return rc

    def cycle(self):
        code = self.code
        debug = self.debug
        p = self.program_counter
        return_code = self.NO_ERROR
        if debug: print("p: {} RB:{}".format(p,self.relative_base))
        code_str = str(code[p]).zfill(5)
        if debug: print(code_str)
        op = int(code_str[3])*10 + int(code_str[4])
        m1 = int(code_str[2])
        m2 = int(code_str[1])
        m3 = int(code_str[0])

        if m1 == 0:   o1 = code[p+1]                    # Position Mode
        elif m1 == 2: o1 = self.relative_base + code[p+1]    # Relative Mode
        else:         o1 = p+1                          # Imediate Mode
            
        if m2 == 0:   o2 = code[p+2]
        elif m2 == 2: o2 = self.relative_base + code[p+2]
        else:         o2 = p+2

        if m3 == 0:   o3 = code[p+3]
        elif m3 == 2: o3 = self.relative_base + code[p+3]
        else:         o3 = p+3

        if debug: 
            print("Op: {} m1: {} m2: {} m3: {}".format(op,m1,m2,m3))
            prettyprint(code, p)
        for i in code:
            if type(i) != type(int(1)):
                print("Type error in intcode!!!")
        if op == 1: #add
            if debug: print("+++ Add +++")
            d = o3
            if debug: print("o1={} o2={} d={}  cod[d]={}".format(o1,o2,d,code[d]))
            code[d] = int(code[o1]) + int(code[o2])
            p+=4

        elif op == 2: #multiply
            if debug: print("+++  multiply  +++")
            d = o3
            if debug: print("o1={} o2={} d={}  cod[d]={}".format(o1,o2,d,code[d]))            
            code[d] = code[o1] * code[o2]
            p+=4

        elif op == 3: #input
            if debug: print("+++  Input  +++")
            if self.input_que.empty():
                return_code = self.INPUT_NEEDED
            else:
                val = self.input_que.get()
                #val = input("$: ")
                d = o1
                if debug: print("o1={} code[o1]={} d={}  code[d]={}".format(o1,code[o1],d,code[d]))
                code[d] = int(val)
                p+=2
        elif op == 4: #output
            if debug: print("+++  Output  +++")
            self.output_que.put_nowait(code[o1])
            return_code = self.OUTPUT_AVAILABLE
            #print("output: {}".format(code[o1]))
            p+=2
        elif op == 5: #jump-if-true
            if debug: print("+++  jump-if-true  +++")
            if debug: print("{} {} {} {}".format(o1,o2,code[o1], code[o2]))              
            if code[o1] is not  0:
                p = code[o2]
            else:
                p+=3
        elif op == 6: #jump-if-false
            if debug: print("+++  jump-if-false  +++")
            if debug: print("{} {} {} {}".format(o1,o2,code[o1], code[o2]))    
            
            if code[o1] is 0:
                p = code[o2]
            else:
                p+=3
        elif op == 7: #less than
            if debug: print("+++  less than   +++")           
            d = o3
            if debug: print("o1={} o2={} d={}  cod[d]={}".format(o1,o2,d,code[d]))

            if code[o1] < code[o2]:
                code[d] = 1
            else:
                code[d] = 0
            
            p+=4
            
        elif op == 8: #equals
            if debug: print("+++  equals  +++")
            d = o3
            if debug: print("o1={} o2={} d={}  cod[d]={}".format(o1,o2,d,code[d]))
        
            if code[o1] == code[o2]:
                code[d] = 1
            else:
                code[d] = 0
            p+=4
        elif op == 9: #adjust relative base
            if debug: print("+++  adjust relative base  ++++")
            if debug: print("{} {}".format(o1,code[o1]))           
            self.relative_base+=  code[o1]
            if debug: print("rb: {}->{}".format(self.relative_base-code[o1],self.relative_base))
            p+=2
        elif code[p] == 99:
            return_code = self.COMPLETE
        else:
            print("error")
            return -1
        if debug: print(" ")
        
        self.program_counter = p
        return return_code

class Pos:
    x = 0
    y = 0
    
    DIR_NORTH = 1
    DIR_SOUTH = 2
    DIR_WEST  = 3
    DIR_EAST  = 4
    
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def north(self):
        self.y-=1
    def south(self):
        self.y+=1
    def east(self):
        self.x+=1
    def west(self):
        self.x-=1
    def move(self,direction):
        if direction == self.DIR_NORTH:
            self.north()
        elif direction == self.DIR_SOUTH:
            self.south()
        elif direction == self.DIR_EAST:
            self.east()
        elif direction == self.DIR_WEST:
            self.west()

class Board:
    width = 0
    height = 0
    buffer = []
    current_pos = None
    under_robot = 0
    TILE_NONE = 0
    TILE_FLOOR = 1
    TILE_WALL = 2
    TILE_ROBOT = 3
    TILE_OXYGEN = 4
    TILE_UNKNOWN = 5

    RESULT_WALL = 0
    RESULT_MOVE = 1
    RESULT_OXY  = 2

    DIR_NORTH = 1
    DIR_SOUTH = 2
    DIR_WEST  = 3
    DIR_EAST  = 4
    

    tile_map = {TILE_NONE:' ', TILE_FLOOR:'.', TILE_WALL:'#',TILE_ROBOT:'D', TILE_OXYGEN:'O', TILE_UNKNOWN:'?'}

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.under_robot = self.TILE_FLOOR
        #print("{},{}".format(self.width,self.height))
        self.buffer = [[self.TILE_UNKNOWN for i in range(self.width)] for j in range(self.height)]
        self.current_pos = Pos(int(self.width/2),int(self.height/2))
        

    def draw_to_screen(self, screen, draw_format):
        #print("{},{}".format(len(self.buffer[0]),len(self.buffer)))
        for y in range(len(self.buffer)):
            for x in range(len(self.buffer[y])):
                #print("{},{}".format(x,y))
                c = self.buffer[y][x]
                text_window.addstr(y,x,self.tile_map[c])
        text_window.addnstr(int(self.current_pos.y),self.current_pos.x,self.tile_map[self.TILE_ROBOT], draw_format)
    
    def move(self, direction, result):
        
        if result == self.RESULT_WALL:
            if direction == self.DIR_NORTH:
                self.buffer[self.current_pos.y-1][self.current_pos.x] = self.TILE_WALL
            elif direction == self.DIR_SOUTH:
                self.buffer[self.current_pos.y+1][self.current_pos.x] = self.TILE_WALL
            elif direction == self.DIR_EAST:
                self.buffer[self.current_pos.y][self.current_pos.x+1] = self.TILE_WALL
            elif direction == self.DIR_WEST:
                self.buffer[self.current_pos.y][self.current_pos.x-1] = self.TILE_WALL
            
        elif result == self.RESULT_MOVE:
            self.buffer[self.current_pos.y][self.current_pos.x] = self.under_robot
            self.current_pos.move(direction)
            self.buffer[self.current_pos.y][self.current_pos.x] = self.TILE_ROBOT
            self.under_robot = self.TILE_FLOOR
        elif result == self.RESULT_OXY:
            self.buffer[self.current_pos.y][self.current_pos.x] = self.under_robot
            if direction == self.DIR_NORTH:
                self.buffer[self.current_pos.y-1][self.current_pos.x] = self.TILE_ROBOT
            elif direction == self.DIR_SOUTH:
                self.buffer[self.current_pos.y+1][self.current_pos.x] = self.TILE_ROBOT
            elif direction == self.DIR_EAST:
                self.buffer[self.current_pos.y][self.current_pos.x+1] = self.TILE_ROBOT
            elif direction == self.DIR_WEST:
                self.buffer[self.current_pos.y+1][self.current_pos.x-1] = self.TILE_ROBOT
            self.under_robot = self.TILE_OXYGEN

# class AutoBot:
#     path = []
#     RESULT_WALL = 0
#     RESULT_MOVE = 1
#     RESULT_OXY  = 2
    
#     DIR_NORTH = 1
#     DIR_SOUTH = 2
#     DIR_WEST  = 3
#     DIR_EAST  = 4
    
#     next_command = 0
#     last_command = 0


#     def __init__(self, breadthFirst):        
#         next_command = DIR_WEST

#     def getCommand():
#         return next_command

#     def putResult(result):
#         if result == RESULT_WALL:
#             if last_command == DIR_WEST:
#                 next_command = DIR_NORTH
#             elif last_command == DIR_NORTH:
#                 next_command = DIR_EAST
#             elif last_command == DIR_EAST:
#                 next_command = DIR_SOUTH
#             elif last_command == DIR_SOUTH:
#                 val = self.path.pop()
                

#         elif result == RESULT_MOVE:
#             pass

codebank = [
    [],
    [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99],
    [1102,34915192,34915192,7,4,7,99,0],
    [104,1125899906842624,99],
    [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,0,1020,1101,0,23,1010,1102,1,31,1009,1101,34,0,1019,1102,38,1,1004,1101,29,0,1017,1102,1,25,1018,1102,20,1,1005,1102,1,24,1008,1101,897,0,1024,1101,0,28,1016,1101,1,0,1021,1101,0,879,1028,1102,1,35,1012,1101,0,36,1015,1101,311,0,1026,1102,1,37,1011,1101,26,0,1014,1101,21,0,1006,1102,1,32,1002,1102,1,33,1003,1102,27,1,1001,1102,1,667,1022,1101,0,892,1025,1101,664,0,1023,1101,30,0,1000,1101,304,0,1027,1101,22,0,1013,1102,1,874,1029,1102,1,39,1007,109,12,21108,40,41,1,1005,1013,201,1001,64,1,64,1106,0,203,4,187,1002,64,2,64,109,5,1205,4,221,4,209,1001,64,1,64,1106,0,221,1002,64,2,64,109,5,21108,41,41,-5,1005,1017,243,4,227,1001,64,1,64,1106,0,243,1002,64,2,64,109,-30,2101,0,8,63,1008,63,30,63,1005,63,269,4,249,1001,64,1,64,1105,1,269,1002,64,2,64,109,15,2101,0,-5,63,1008,63,35,63,1005,63,293,1001,64,1,64,1106,0,295,4,275,1002,64,2,64,109,28,2106,0,-8,1001,64,1,64,1105,1,313,4,301,1002,64,2,64,109,-22,1205,7,329,1001,64,1,64,1106,0,331,4,319,1002,64,2,64,109,-12,1208,6,37,63,1005,63,351,1001,64,1,64,1106,0,353,4,337,1002,64,2,64,109,-3,2108,21,8,63,1005,63,375,4,359,1001,64,1,64,1106,0,375,1002,64,2,64,109,14,1201,-5,0,63,1008,63,39,63,1005,63,401,4,381,1001,64,1,64,1105,1,401,1002,64,2,64,109,17,1206,-9,419,4,407,1001,64,1,64,1105,1,419,1002,64,2,64,109,-10,21101,42,0,-4,1008,1015,42,63,1005,63,445,4,425,1001,64,1,64,1105,1,445,1002,64,2,64,109,-5,1206,7,457,1105,1,463,4,451,1001,64,1,64,1002,64,2,64,109,-6,2107,34,-5,63,1005,63,479,1105,1,485,4,469,1001,64,1,64,1002,64,2,64,109,-8,2102,1,5,63,1008,63,23,63,1005,63,505,1106,0,511,4,491,1001,64,1,64,1002,64,2,64,109,5,2102,1,1,63,1008,63,21,63,1005,63,537,4,517,1001,64,1,64,1105,1,537,1002,64,2,64,109,15,21107,43,44,-6,1005,1014,555,4,543,1106,0,559,1001,64,1,64,1002,64,2,64,109,-6,1207,-7,38,63,1005,63,579,1001,64,1,64,1106,0,581,4,565,1002,64,2,64,109,-17,1201,4,0,63,1008,63,28,63,1005,63,601,1106,0,607,4,587,1001,64,1,64,1002,64,2,64,109,14,2107,31,-9,63,1005,63,625,4,613,1105,1,629,1001,64,1,64,1002,64,2,64,109,15,21102,44,1,-7,1008,1019,44,63,1005,63,651,4,635,1106,0,655,1001,64,1,64,1002,64,2,64,109,3,2105,1,-6,1106,0,673,4,661,1001,64,1,64,1002,64,2,64,109,-14,21101,45,0,2,1008,1017,42,63,1005,63,693,1105,1,699,4,679,1001,64,1,64,1002,64,2,64,109,5,21107,46,45,-8,1005,1012,719,1001,64,1,64,1105,1,721,4,705,1002,64,2,64,109,-19,2108,21,7,63,1005,63,737,1106,0,743,4,727,1001,64,1,64,1002,64,2,64,109,9,1207,-2,25,63,1005,63,761,4,749,1106,0,765,1001,64,1,64,1002,64,2,64,109,-10,1208,1,27,63,1005,63,783,4,771,1106,0,787,1001,64,1,64,1002,64,2,64,109,5,1202,4,1,63,1008,63,29,63,1005,63,807,1106,0,813,4,793,1001,64,1,64,1002,64,2,64,109,8,21102,47,1,0,1008,1013,50,63,1005,63,833,1106,0,839,4,819,1001,64,1,64,1002,64,2,64,109,-12,1202,8,1,63,1008,63,31,63,1005,63,865,4,845,1001,64,1,64,1105,1,865,1002,64,2,64,109,34,2106,0,-7,4,871,1105,1,883,1001,64,1,64,1002,64,2,64,109,-18,2105,1,7,4,889,1105,1,901,1001,64,1,64,4,64,99,21101,0,27,1,21101,915,0,0,1106,0,922,21201,1,13801,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21102,942,1,0,1106,0,922,21201,1,0,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21202,-2,1,-2,109,-3,2106,0,0],
    [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,101,0,1034,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1001,1034,0,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,101,0,1037,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,101,0,1035,1040,1002,1038,1,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,33,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1101,0,2,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,0,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,68,1044,1105,1,224,1101,0,0,1044,1106,0,224,1006,1044,247,101,0,1039,1034,102,1,1040,1035,1001,1041,0,1036,102,1,1043,1038,101,0,1042,1037,4,1044,1105,1,0,30,84,39,21,27,93,20,65,45,95,19,6,71,25,33,13,80,53,60,70,65,80,45,65,53,62,93,13,19,72,33,49,54,92,9,29,25,69,7,46,9,96,97,70,8,69,71,97,3,75,94,49,96,11,76,24,29,84,87,99,33,76,83,83,21,62,97,82,63,71,78,74,29,94,90,34,92,58,75,44,66,99,28,37,84,18,18,94,86,50,4,74,3,96,74,39,99,55,93,44,94,55,40,78,2,88,70,6,69,67,87,40,4,93,76,30,1,42,40,87,23,83,89,24,73,19,62,88,43,92,94,50,71,53,19,75,22,9,82,46,65,84,92,63,99,57,23,62,93,61,14,87,67,84,90,38,96,83,33,63,40,80,75,10,79,89,52,14,97,32,87,72,57,79,7,79,6,93,66,77,50,19,97,78,65,96,24,94,80,12,10,70,9,60,77,67,17,83,76,36,79,27,43,91,6,72,77,49,4,47,56,85,81,11,46,96,93,33,82,44,69,49,34,98,77,95,38,19,85,1,62,73,49,95,39,62,36,83,23,93,34,32,21,94,89,30,85,76,13,92,87,3,84,43,3,74,39,81,6,85,16,69,89,21,56,80,65,92,84,97,7,63,23,8,87,37,70,54,75,92,95,96,51,83,34,24,86,39,59,48,89,45,34,89,72,3,77,63,98,38,70,39,38,98,97,85,46,96,53,81,89,27,83,75,31,81,71,39,81,62,79,11,78,18,90,94,1,91,1,79,77,74,64,20,73,55,75,78,2,77,24,92,56,55,25,70,21,38,69,49,81,19,34,92,97,74,61,79,18,77,51,76,62,92,10,85,83,87,39,90,31,98,95,61,32,63,82,59,75,65,53,72,91,17,75,75,54,85,57,32,13,39,70,48,86,59,50,96,32,23,84,61,85,48,59,92,33,15,58,83,95,48,80,70,84,58,69,70,37,99,18,73,79,32,71,22,41,75,26,71,25,55,73,31,5,53,71,95,65,87,50,62,95,80,54,95,73,79,20,94,65,83,33,26,88,3,11,99,76,93,28,97,67,49,90,94,19,85,28,10,96,70,55,84,17,75,33,47,91,44,88,96,1,6,89,40,69,27,58,98,61,25,77,79,43,83,38,13,72,44,99,20,33,69,8,5,47,72,78,24,53,94,78,39,99,87,9,63,82,52,69,64,48,93,46,48,89,22,84,32,69,7,36,99,80,4,27,92,54,14,85,56,19,99,93,99,49,67,82,90,23,10,77,77,37,79,67,78,27,81,79,34,67,81,40,88,76,89,94,64,80,73,79,57,72,22,14,93,3,88,84,88,41,12,29,4,97,57,83,38,93,51,55,20,75,57,78,22,76,22,24,85,91,79,27,19,46,90,18,71,3,39,28,26,94,87,83,31,35,73,56,99,83,35,65,92,45,98,93,2,73,88,15,90,62,85,95,20,96,75,52,4,62,81,78,49,67,69,20,5,85,72,79,45,34,73,89,20,37,60,79,97,6,41,78,40,70,42,29,89,21,76,88,44,82,17,9,73,52,71,73,25,89,71,30,82,85,26,86,61,43,7,71,13,99,72,40,95,79,39,67,39,65,90,91,14,96,20,73,98,66,13,92,70,1,93,2,86,45,54,85,73,30,62,14,97,89,39,77,99,40,89,76,49,97,42,60,97,62,82,35,98,49,80,15,91,34,87,65,77,44,93,65,87,76,82,20,78,46,90,18,81,73,98,47,99,48,69,2,82,90,90,47,85,49,94,37,81,76,90,0,0,21,21,1,10,1,0,0,0,0,0,0],
    [1,330,331,332,109,3300,1102,1182,1,15,1101,1455,0,24,1002,0,1,570,1006,570,36,101,0,571,0,1001,570,-1,570,1001,24,1,24,1106,0,18,1008,571,0,571,1001,15,1,15,1008,15,1455,570,1006,570,14,21102,58,1,0,1106,0,786,1006,332,62,99,21101,333,0,1,21102,1,73,0,1105,1,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,102,1,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21101,0,340,1,1105,1,177,21101,477,0,1,1105,1,177,21102,1,514,1,21101,176,0,0,1106,0,579,99,21101,0,184,0,1105,1,579,4,574,104,10,99,1007,573,22,570,1006,570,165,101,0,572,1182,21101,0,375,1,21102,211,1,0,1106,0,579,21101,1182,11,1,21102,222,1,0,1106,0,979,21102,1,388,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21102,1,244,0,1106,0,979,21101,0,401,1,21102,255,1,0,1106,0,579,21101,1182,33,1,21101,0,266,0,1106,0,979,21102,1,414,1,21101,277,0,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21101,313,0,0,1105,1,622,1005,575,327,1101,0,1,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,44,2,0,109,4,2101,0,-3,587,20101,0,0,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2105,1,0,109,5,2101,0,-4,630,20102,1,0,-2,22101,1,-4,-4,21101,0,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,652,21002,0,1,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1105,1,786,21201,-1,-1,-1,1105,1,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,1,731,0,1105,1,786,1106,0,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,0,756,0,1105,1,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21102,1,774,0,1105,1,622,21201,-3,1,-3,1105,1,640,109,-5,2106,0,0,109,7,1005,575,802,20101,0,576,-6,21001,577,0,-5,1105,1,814,21102,0,1,-1,21102,1,0,-5,21101,0,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,45,-3,22201,-6,-3,-3,22101,1455,-3,-3,1202,-3,1,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21101,1,0,-1,1106,0,924,1205,-2,873,21101,35,0,-4,1105,1,924,2101,0,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1102,2,1,0,1202,-3,1,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,921,21001,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,45,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,41,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1102,1,1,575,21102,973,1,0,1105,1,786,99,109,-7,2106,0,0,109,6,21101,0,0,-4,21102,0,1,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1106,0,1041,21101,0,-4,-2,1105,1,1041,21102,1,-5,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2102,1,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2102,1,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21102,439,1,1,1105,1,1150,21101,477,0,1,1106,0,1150,21101,514,0,1,21102,1,1149,0,1105,1,579,99,21101,0,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,1202,-5,1,1176,1201,-4,0,0,109,-6,2105,1,0,6,9,36,1,7,1,36,1,7,1,23,7,6,1,7,1,23,1,12,1,7,1,23,1,12,1,7,1,23,1,12,5,3,1,11,13,16,1,3,1,11,1,24,11,9,1,24,1,3,1,3,1,1,1,9,1,24,1,3,1,3,1,1,1,9,1,24,1,3,1,3,1,1,1,9,1,24,1,3,1,3,13,24,1,3,1,5,1,34,7,3,1,38,1,1,1,3,1,38,1,1,1,3,1,38,1,1,1,3,1,38,7,40,1,44,1,44,1,44,1,11,7,26,1,11,1,5,1,22,11,5,1,5,1,22,1,3,1,5,1,5,1,5,1,14,13,5,1,5,1,5,1,3,1,10,1,7,1,9,1,5,1,5,1,3,1,10,1,7,1,5,13,3,1,3,1,10,1,7,1,5,1,3,1,5,1,1,1,3,1,3,1,10,1,5,13,5,1,1,1,3,1,3,1,10,1,5,1,1,1,5,1,9,1,1,1,3,1,3,1,10,1,5,1,1,1,5,1,9,11,10,1,5,1,1,1,5,1,11,1,3,1,14,7,1,7,11,1,3,5,36,1,7,1,36,1,7,1,36,1,7,1,36,1,7,1,36,1,7,1,36,9,10]
    ]


intcode = Intcode(codebank[6])

import os
os.system("mode con cols=240 lines=240")

intcode.debug = False
curses_on = False
if curses_on:

    WINDOW_SIZE_X = 120
    WINDOW_SIZE_Y = 120
    import curses

    stdscr = curses.initscr()

    #resize = curses.is_term_resized(WINDOW_SIZE_X,WINDOW_SIZE_Y)
    #if resize is True:
    #    stdscr.clear()
    #curses.resize_term(WINDOW_SIZE_X,WINDOW_SIZE_Y)
    #stdscr.refresh()

    # init the screen
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    #check for and begin color support
    if curses.has_colors(): curses.start_color()

    #initialize the color combinations we're going to use
    #                      Fore             back
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    stdscr.addstr("AOC Day 17", curses.A_REVERSE)
    stdscr.chgat(-1,curses.A_REVERSE)

    stdscr.addstr(curses.LINES-1,0,"(1)North (2)South (3)West (4)East  (Q) Quit")
    stdscr.addstr(curses.LINES-1,curses.COLS-14,"STATUS:  0")
    stdscr.addstr(curses.LINES-1,curses.COLS-32,"Last Key: 0")
    #change colors
    stdscr.chgat(curses.LINES-1,1,1,curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1,10,1,curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1,19,1,curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1,27,1,curses.A_BOLD | curses.color_pair(2))
    stdscr.chgat(curses.LINES-1,36,1,curses.A_BOLD | curses.color_pair(1))

    game_window = curses.newwin(curses.LINES-2,curses.COLS,1,0)

    text_window = game_window.subwin(curses.LINES-6,curses.COLS-4,3,2)

    buffer = []
    line = " "*(curses.COLS-5)
    line+="\n"
    #text_window.addstr(line)
    #board = Board(curses.COLS-5, curses.LINES-7)
    
    #board.draw_to_screen(text_window, curses.color_pair(1))

    game_window.box()
    stdscr.noutrefresh()
    game_window.noutrefresh()

    game_window.timeout(0)

    curses.doupdate()

    
    last_key = ""
    status = " "
    
    while True:
        c = int(game_window.getch())
        if c == ord('q') or c == ord('Q'):
            break
        elif c != -1:
            stdscr.addstr(curses.LINES-1,curses.COLS-22,chr(c), curses.color_pair(4))
            if chr(c) == 'w':
                c = ord('1')
            elif chr(c) == 's':
                c = ord('2')
            elif chr(c) == 'a':
                c = ord('3')
            elif chr(c) == 'd':
                c = ord('4')
            last_key = int(chr(c))

            if last_key == 'a':
                auto = True
                status = "A"
            else:
                intcode.input(last_key)

            
        
        result = intcode.cycle()
        if result == intcode.OUTPUT_AVAILABLE:
            val = intcode.output()
            board.move(direction=last_key, result=val)

        elif result == intcode.INPUT_NEEDED:
            status = "W" # waiting

        elif result == intcode.COMPLETE:
            status = "C" # complete
        elif result == intcode.NO_ERROR:
            status = "R"
        else:
            val = result
            text_window.addstr("Output: {}".format(val), curses.color_pair(3))
            status="?"
        
        stdscr.addstr(curses.LINES-1,curses.COLS-5,status, curses.color_pair(4))
        
        board.draw_to_screen(text_window, curses.color_pair(1))
        
        #curses.curs_set(0)   
        stdscr.noutrefresh()
        game_window.noutrefresh()
        text_window.noutrefresh()
        curses.doupdate()


    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)

    curses.endwin()
else:
    row = 0
    col = 0
    buffer = [["*" for i in range(46)] for j in range(500)]
    while True:
       
        
        result = intcode.run() # run until blocked
        if result == intcode.OUTPUT_AVAILABLE:
            val = intcode.output()
            print(chr(val), end="")
            buffer[row][col] = chr(val)
            if val == 10:
                row+=1
                col=0
            else:
                col+=1

        elif result == intcode.INPUT_NEEDED:
            #text_window.addstr(2,2,"W...", curses.color_pair(3))
            print("Input needed!")
            val = input("$")
            intcode.input(val)
        elif result == intcode.COMPLETE:
            print("Complete")
            break
        else:
            val = result
            print("Unknown: {}".format(val), curses.color_pair(3))
sum = 0
for r in range(len(buffer)):
    if buffer[r][0] == '*':
        print("done")
        break
    else:
        print("r {}: ".format(r), end="")
    for c in range(len(buffer[r])):
        print(buffer[r][c], end="")

for r in range(len(buffer)):
    if buffer[r][0] == '*':
        print("done")
        break
    for c in range(len(buffer[r])):
        if not(r  == 0 or r == row-1 or c == 0 or col == 44):
            if buffer[r][c] == '#' and buffer[r-1][c] == '#' and buffer[r+1][c] == '#' and buffer[r][c-1] == '#' and buffer[r][c+1] == '#':
                print("{}x{}={}".format(r,c,r*c))
                sum+= r*c
print("sum: {}".format(sum))



    # #print(len(codebank[4]))    
# running = True
# debug = False
# while running:
#     val = int(input("$: "))
#     if val in range(1,9):
#         intcode(codebank[val], debug)
#     elif val == 0:
#         debug = not debug
#         print("Debug: {}".format(debug))
#     else:
#         running = False
        
            