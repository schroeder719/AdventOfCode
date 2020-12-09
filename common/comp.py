
class Computer:
    def __init__(self):
        self.code = []
        self.pc = 0
        self.acc = 0

    def load_run(self,data):
        self.load(data)
        return self.run()

    def load(self,data):
        self.code = data
        self.cl = len(data) # code length

    def run(self):
        result = True
        running = True
        rv = None
        mv = 0
        pc = 0
        acc = 0
        history = []
            #print("total: {}".format(tl))
        while(running):
            #print(history)
            if pc in history:
                print("acc: {}".format(acc))
                result = False
                rv = 0
                running = False
            elif pc >= self.cl:
                print("acc: {}".format(acc))
                result = True
                rv = acc
                running = False
            else:
                history.append(pc)
                cmd = self.code[pc].split(" ")
                d = int(cmd[1])
                #print(cmd)
                if cmd[0] == 'acc':
                    acc+= d
                    mv = 1
                elif cmd[0] == 'jmp':
                    mv = d
                elif cmd[0] == 'nop':
                    mv = 1
            pc =  pc + mv
            #print(pc)

        return result,rv
    