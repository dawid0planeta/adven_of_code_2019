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
    
def find_trace_to_com(starting: "node_object") -> list:
    trace = []
    curr_object = starting
    while curr_object.name != "COM":
        curr_object = curr_object.parent
        trace.append(curr_object.name)
    trace.reverse()
    return trace

def solution(filename: str) -> int:
    data = read_file(filename)
    tree_dict = create_tree_dict(data)
    you_trace = find_trace_to_com(tree_dict["YOU"])
    san_trace = find_trace_to_com(tree_dict["SAN"])
    cut_you_trace = []
    for i in range(len(you_trace)):
        if i >= len(san_trace):
            cut_you_trace.append(you_trace[i])
        elif you_trace[i] != san_trace[i]:
            cut_you_trace.append(you_trace[i])

    cut_san_trace = []
    for i in range(len(san_trace)):
        if i >= len(you_trace):
            cut_san_trace.append(san_trace[i])
        elif san_trace[i] != you_trace[i]:
            cut_san_trace.append(san_trace[i])

    return len(cut_san_trace) + len(cut_you_trace)


print(solution("input.txt"))