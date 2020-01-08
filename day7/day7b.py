import sys
sys.path.append("..")
from tools.Proc import Proccessor
from itertools import cycle, permutations 


def read_file(filename: str) -> list:
    with open(filename, 'r') as f:
        memory = [int(elem) for elem in f.readline().split(',')]
    return memory

def try_sequence(seq: tuple, memory: list) -> int:
    proccesor_list = [Proccessor(memory, known_inputs=[each]) for each in seq]
    amps = cycle(proccesor_list)
    input_num = 0
    halted_num = 0
    while True:
        output = run(next(amps), input_num)
        input_num = output[1]
        if output[0] == "HALTED":
            halted_num += 1
        if halted_num == 5:
            break
    return proccesor_list[4].last_output

def run(amp: "Proc object", save: int) -> tuple:
    out = amp.run()
    while out[0] != "HALT":
        if out[0] == "INPUT":
            out = amp.run(save)
            continue
        else:
            return ("RUNNING", out[1])
        out = amp.run()
    return ("HALTED", 0)
    


def solution(filename: str) -> int:
    memory = read_file(filename)
    phase_sequences = permutations([5,6,7,8,9])
    max = 0
    for each in phase_sequences:
        out = try_sequence(each, memory)
        if out > max:
            max = out
    return max


print(solution("input.txt"))
        

