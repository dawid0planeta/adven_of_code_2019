from collections import Counter


def read_file(filename: str) -> list:
    """ returns list of layers """
    with open(filename, "r") as f:
        string_all_layers = f.read().rstrip() 
        layers = [string_all_layers[i : i + 150] for i in range(0, len(string_all_layers), 150)]
    return layers


def solution(filename: str) -> int:
    layers = read_file(filename)
    fewest_zeros = Counter(layers[0])["0"]
    for layer in layers:
        count = Counter(layer)
        zero_count = count["0"]
        if zero_count < fewest_zeros:
            fewest_zeros = zero_count 
            ones = count["1"]
            twos = count["2"]
    return ones * twos


print(solution("input.txt"))