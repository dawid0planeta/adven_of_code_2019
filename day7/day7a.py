import sys
sys.path.append("..")
from tools.Proc import Proccessor
from itertools import cycle, permutations 


def read_file(filename: str) -> list:
    with open(filename, 'r') as f:
        memory = [int(elem) for elem in f.readline().split(',')]
    return memory

def try_sequence(seq: tuple, memory: list) -> int:
    amps = [Proccessor(memory, known_inputs=[each]) for each in seq]
    input_num = 0
    for index in range(len(seq)):
        output = run(amps[index], input_num)
        input_num = output
    return output

def run(amp: "Proc object", save: int) -> int:
    out = amp.run()
    while out[0] != "HALT":
        if out[0] == "INPUT":
            out = amp.run(save)
            continue
        else:
            return out[1]
        out = amp.run()

def solution(filename: str) -> int:
    memory = read_file(filename)
    phase_sequences = permutations([0,1,2,3,4])
    max = 0
    for each in phase_sequences:
        out = try_sequence(each, memory)
        if out > max:
            max = out
    return max


print(solution("input.txt"))
        

