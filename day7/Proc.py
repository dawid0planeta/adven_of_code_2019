from collections import defaultdict


class Proccessor():
    def __init__(self, memory, known_inputs=[]):
        memory = [(key, value) for key, value in zip(range(len(memory)), memory)]
        self.memory = defaultdict(int, memory)
        self.known_inputs = known_inputs
        self.pointer = 0
        self.args = []
        self.relative_base = 0
        self.opcode_dict = {
            1: (self.add, 3),
            2: (self.multiply, 3),
            3: (self.put, 1),
            4: (self.output, 1),
            5: (self.jit, 2),
            6: (self.jif, 2),
            7: (self.less_than, 3),
            8: (self.equals, 3),
            9: (self.adjust_rel_base, 1),
            99: "halt"
        }

    
    def run(self, input_num=None):
        if input_num is not None:
            self.known_inputs.append(input_num)
        
        out = self.execute()
        while out[0] == "RUNNING":
            out = self.execute()
        
        if out[0] == "OUTPUT":
            return ("OUTPUT", out[1])
        elif out[0] == "HALT":
            return ("HALT", 0)
        elif out[0] == "INPUT":
            return ("INPUT", 0)

    def read_instruction(self):
        self.curr_instruction = self.memory[self.pointer]


    def decode(self):
        self.curr_opcode = self.curr_instruction % 100
        self.curr_modes = [int(i) for i in list(str(self.curr_instruction))][-3::-1]

    def set_args(self):
        self.args.clear()
        pointer = self.pointer
        memory = self.memory
        num_of_args = self.num_of_args
        for index in range(num_of_args):
            mode = self.curr_modes[index]
            if mode == 0:     #position
                self.args.append(memory[memory[pointer+index+1]])
            elif mode == 1:   #immediate
                self.args.append(memory[pointer+index+1])
            elif mode == 2:   #relative
                self.args.append(memory[memory[pointer+index+1] + self.relative_base])
        
        target_mode = self.curr_modes[-1]
        if target_mode == 0:  #position
            self.target = memory[pointer+num_of_args]
        elif target_mode == 2: #relatice
            self.target = memory[pointer+num_of_args] + self.relative_base

        return None
        
        


    def execute(self):
        self.read_instruction()
        self.decode()

        try:
            if self.curr_opcode == 99:
                return ("HALT", 0)

            else: 
                self.func, self.num_of_args = self.opcode_dict[self.curr_opcode]
                self.curr_modes.extend([0] * (self.num_of_args-len(self.curr_modes)))
                self.set_args()

                if self.curr_opcode == 3:
                    if len(self.known_inputs) != 0:
                        input_num = self.known_inputs.pop()
                    else:
                        return ("INPUT", 0)
                    self.put(input_num)
                else:
                    output = self.func()
                    if output is not None:
                        self.last_output = output
                        return ("OUTPUT", output)
                return ("RUNNING", 0)

        except KeyError:
            print("opcode: ", self.curr_opcode, " nie istnieje")
        


    def add(self):
        self.memory[self.target] = self.args[0] + self.args[1]
        self.pointer += 4
        return None 

    def multiply(self):
        self.memory[self.target] = self.args[0] * self.args[1]
        self.pointer += 4
        return None

    def put(self, input_num):
        self.memory[self.target] = input_num 
        self.pointer += 2
        return None 
    
    def output(self):
        output = self.args[0]
        self.pointer += 2
        return output

    def jit(self):
        if self.args[0] != 0:
            self.pointer = self.args[1]
        else: 
            self.pointer += 3
        return None

    def jif(self):
        if self.args[0] == 0:
            self.pointer = self.args[1]
        else:
            self.pointer += 3
        return None

    def less_than(self):
        if self.args[0] < self.args[1]:
            self.memory[self.target] = 1
        else:
            self.memory[self.target] = 0
        self.pointer += 4
        return None

    def equals(self):
        if self.args[0] == self.args[1]:
            self.memory[self.target] = 1
        else:
            self.memory[self.target] = 0
        self.pointer += 4
        return None 

    def adjust_rel_base(self):
        self.relative_base += self.args[0]
        self.pointer += 2
        return None