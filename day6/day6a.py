from Node import Node

def read_file(filename: str) -> list:
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(line.rstrip())
    return data


def create_tree_dict(data: list) -> dict:
    tree_dict = {}
    for line in data:
        orbiter_name = line[4:]
        star_name = line[:3]
        if orbiter_name not in tree_dict:
            tree_dict[orbiter_name] = Node(orbiter_name)
        if star_name not in tree_dict:
            tree_dict[star_name] = Node(star_name)
        star = tree_dict[star_name]
        orbiter = tree_dict[orbiter_name]
        orbiter.give_parent(star)
        star.add_sibling(orbiter)

    return tree_dict
    
def solution(filename: str) -> int:
    data = read_file(filename)
    tree_dict = create_tree_dict(data)
    total = 0

    for value in tree_dict.values():
        total += value.depth
    
    return total


        

print(solution("input.txt"))
