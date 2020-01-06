class Proccessor():
    def __init__(self, memory):
        self.memory = memory
        self.pointer = 0
        self.asking_for_input = False
        self.opcode_dict = {
            1: (self.add, 3),
            2: (self.multiply, 3),
            3: (self.save, 1),
            4: (self.output, 1),
            5: (self.jit, 2),
            6: (self.jif, 2),
            7: (self.less_than, 3),
            8: (self.equals, 3),
            99: "halt"
        }


    def read_instruction(self):
        self.curr_instruction = self.memory[self.pointer]


    def decode(self):
        self.curr_opcode = self.curr_instruction % 100
        self.curr_modes = [int(i) for i in list(str(self.curr_instruction))][-3::-1]


    def execute(self, save=None):
        self.read_instruction()
        self.decode()

        try:
            if self.curr_opcode == 99:
                return ("HALT", 0)
            elif self.curr_opcode == 3 and self.asking_for_input == False:
                self.asking_for_input = True
                return ("INPUT", 0)
            else: 
                self.func, self.num_of_args = self.opcode_dict[self.curr_opcode]
                self.curr_modes.extend([0] * (self.num_of_args-len(self.curr_modes)))
                self.args = [i if self.curr_modes[j] == 1 else self.memory[i] for i, j in zip(self.memory[self.pointer+1: self.pointer+self.num_of_args+1], range(self.num_of_args))]
                if self.curr_opcode == 3:
                    if save == None:
                        print("tutaj")
                    self.func(save)
                    self.asking_for_input = False
                    return ("SAVED", 0)
                else:
                    output = self.func()
                    if output is not None:
                        return ("OUTPUT", output)
                    return ("RUNNING", output)

        except KeyError:
            print("opcode: ", self.curr_opcode, " nie istnieje")
        


    def add(self):
        self.memory[self.memory[self.pointer+3]] = self.args[0] + self.args[1]
        self.pointer += 4
        return None 


    def multiply(self):
        self.memory[self.memory[self.pointer+3]] = self.args[0] * self.args[1]
        self.pointer += 4
        return None


    def save(self, save=None):
        self.memory[self.memory[self.pointer+1]] = save
        self.pointer += 2
        return None 

    
    def output(self):
        if self.curr_modes[0] == 0:
            output = self.memory[self.memory[self.pointer+1]]
        else:
            output = self.memory[self.pointer+1]
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
            self.memory[self.memory[self.pointer+3]] = 1
        else:
            self.memory[self.memory[self.pointer+3]] = 0
        self.pointer += 4
        return None

    def equals(self):
        if self.args[0] == self.args[1]:
            self.memory[self.memory[self.pointer+3]] = 1
        else:
            self.memory[self.memory[self.pointer+3]] = 0
        self.pointer += 4
        return None 


