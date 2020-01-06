import numpy as np


def read_data(filename: str) -> 'np.array':
    with open(filename) as f:
        data = np.array(f.read().split('\n')).astype('int32')
    return data


def solve(filename: str) -> int:
    data = read_data(filename)
    return np.sum(data//3-2)


print(solve('input.txt'))