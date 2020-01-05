import numpy as np


def read_data(filename: str) -> 'np.array':
    with open(filename) as f:
        data = np.array(f.read().split('\n')).astype('int32')
    return data


def find_total_mass(mass: int) -> int:
    total_mass = 0
    mass = (mass//3)-2
    while mass > 0:
        total_mass += mass
        mass = (mass//3)-2
    return total_mass


def solve(filename: str) -> int:
    data = read_data(filename)
    vector_find = np.vectorize(find_total_mass)
    return np.sum(vector_find(data))


print(solve('input.txt'))