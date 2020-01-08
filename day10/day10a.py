import math
import numpy as np
import time
from cachetools import cached, LFUCache
from functools import lru_cache
from collections import OrderedDict

def read_data(filename: str) -> dict:
    with open(filename, "r") as f:
        output_list = [list(line.rstrip()) for line in f]
        coors_set = set()
        for i in range(len(output_list)):
            for j in range(len(output_list[0])):
                if output_list[i][j] == "#":
                    coors_set.add((i, j))
        return coors_set

@lru_cache(maxsize=10000)
def gcd(a: int, b: int) -> int:
    a_divs = find_dividers(abs(a))
    b_divs = find_dividers(abs(b))
    inter = a_divs.intersection(b_divs)
    if len(inter) == 0:
        return 1
    return max(a_divs.intersection(b_divs))


@lru_cache(maxsize=100)
def find_dividers(a: int) -> set:
    divs = set()
    for each in range(int(math.sqrt(a)) + 1, 0, -1):
        if a % each == 0:
                divs.add(each)
                divs.add(a // each)
    return divs

def solution(filename: str) -> tuple:
    coors_set = read_data(filename)
    max_visible = 0
    for satel in coors_set:
        counter = 0
        for reciv in coors_set - set(satel):
            if not collides(satel, reciv, coors_set):
                counter += 1

        if counter > max_visible:
            max_visible = counter
            best_coors = satel
    return (max_visible, best_coors)

def collides(satel: tuple, reciv: tuple, coors_set: set):
    vectSE = (reciv[0] - satel[0], reciv[1] - satel[1])
    scale = gcd(*vectSE)
    if vectSE == (0, 0):
        return True
    elif vectSE[0] == 0:
        scale = abs(vectSE[1])
    elif vectSE[1] == 0:
        scale = abs(vectSE[0])
   

    scaled_vector = (vectSE[0]//scale, vectSE[1]//scale)

    for _ in range(scale-1):
        satel = (satel[0] + scaled_vector[0], satel[1] + scaled_vector[1])
        if satel in coors_set:
            return True
    return False
     



def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

@timing
def check_find_dividers(n: int) -> "time":
    for i in range(n):
        find_dividers(i)

@timing
def check_gcd(n: int) -> "time":
    for i in range(1, n):
        for j in range(1, n):
            gcd(i, j)




print(solution("input.txt"))
print(solution("test_input.txt"))
print(find_dividers(0))
