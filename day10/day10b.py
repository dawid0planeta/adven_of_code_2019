import math
from collections import OrderedDict
from operator import itemgetter
import bisect

def read_data(filename: str) -> dict:
    with open(filename, "r") as f:
        output_list = [list(line.rstrip()) for line in f]
        coors_set = set()
        for i in range(len(output_list)):
            for j in range(len(output_list[0])):
                if output_list[i][j] == "#":
                    coors_set.add((i, j))
        return coors_set

def solution(filename: str, station_coors: tuple)  -> int:
    coors_set = read_data(filename) - set([station_coors])
    angles = {}
    for aster in coors_set:
        vect = (station_coors[0] - aster[0], station_coors[1] - aster[1])
        magn = math.sqrt(vect[0]**2 + vect[1]**2)
        angle = get_angle(vect)
        if angle in angles:
            angles[angle].append((magn, aster))
        else:
            angles[angle] = [(magn, aster)]
        angles[angle] = sorted(angles[angle], key=itemgetter(0))
        
    
    sorted_keys = sorted(list(angles.keys()))
    return(angles[sorted_keys[199]])





station_coors = (21, 20)
#station_coors = (13, 11)

def get_angle(coors: tuple):
    angle = math.atan2(coors[0], coors[1]) - math.atan2(1, 0)
    if (angle < 0): 
        angle += 2 * math.pi
    return angle
    

print(solution("input.txt", station_coors))