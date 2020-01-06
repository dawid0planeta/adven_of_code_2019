import numpy as np


def read_data(filename: str) -> list:
    with open(filename, 'r') as f:
        data = list(np.array(f.read().split(",")).astype('int32'))
    return data


def decode_and_run_opcode(opcode: int, a1: int, a2: int) -> int:
    if opcode == 1:
        return a1 + a2
    elif opcode == 2:
        return a1 * a2
    else:
        return -1       # works as a stop because input is positive

def computer(data: list) -> int:
    i = 0
    while (i < len(data)):
        run = decode_and_run_opcode(data[i], data[data[i+1]], data[data[i+2]])
        if run == -1:
            break
        data[data[i+3]] = run 
        i += 4
    return data[0]

def solve(filename: str) -> int:
    data = read_data(filename)
    copy = data.copy()
    for i in range(0, 100):
        for j in range(0, 100):
            data = copy.copy()
            data[1] = i
            data[2] = j
            output = computer(data) 
            if output == 19690720:
                return 100*i + j


print(solve('input.txt'))