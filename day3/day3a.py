def read_data(filename: str) -> "tuple(list, list)":
    with open(filename, 'r') as f:
        lines = f.readlines()
        path1 = lines[0].rstrip().split(",")
        path2 = lines[1].rstrip().split(",")
    return (path1, path2)

def decode_instruction(instruction: str) -> "tuple(changing_coor, direction)":
    if instruction == "U":
        return (0, -1)
    elif instruction == "D":
        return (0, 1)
    elif instruction == "L":
        return (1, -1)
    else:
        return (1, 1)


def get_trail_list(pos: list, instruction: str) -> "tuple(list(coors), pos)":
    coors = []
    changing_coor, direction = decode_instruction(instruction[0])
    print(changing_coor, direction)
    for _ in range(int(instruction[1:])):
        pos[changing_coor] = pos[changing_coor] + direction
        coors.append(pos[:])
    return (coors, pos)


def make_path_dict(path: list) -> "dict of path coors":
    pos = [0, 0]
    path_dict = {}
    for instruction in path:
        trail_list, pos = get_trail_list(pos, instruction)
        for each in trail_list:
            path_dict[tuple(each)] = 1
    return path_dict


def make_subsequent_path_dict(path: list, other_path: dict) -> "tuple(dict of second path, list_of_collisions)":
    pos = [0, 0]
    path_dict = {}
    collisions = []
    for instruction in path:
        trail_list, pos = get_trail_list(pos, instruction)
        for each in trail_list:
            if tuple(each) in other_path:
                collisions.append(tuple(each))
            path_dict[tuple(each)] = 1
    return (path_dict, collisions)  

def mdist(coors: tuple) -> int:
    return abs(coors[0]) + abs(coors[1])

def solve(filename: str) -> int:
    trail1, trail2 = read_data(filename)
    trail1_dict = make_path_dict(trail1)
    trail2_dict, collisions = make_subsequent_path_dict(trail2, trail1_dict)
    smallest_distance = mdist(collisions[0]) 
    for collision in collisions:
        distance = mdist(collision)
        if distance < smallest_distance:
            smallest_distance = distance
    return smallest_distance




filename = 'input.txt'
print(solve(filename))


