from PIL import Image
import numpy as np


def read_file(filename: str) -> list:
    """ returns list of layers """
    with open(filename, "r") as f:
        string_all_layers = f.read().rstrip() 
        layers = [string_all_layers[i : i + 150] for i in range(0, len(string_all_layers), 150)]
    return layers


def solution(filename: str) -> list:
    layers = read_file(filename)
    pixels = [[int(layers[i][j]) for i in range(len(layers))] for j in range(len(layers[0]))]
    visible_pixels = []
    for pixel in pixels:
        for each in pixel:
            if each == 0 or each == 1:
                visible_pixels.append(each)
                break
    black_and_white = [visible_pixels[i:i+25] for i in range(0, len(visible_pixels), 25)]
    print(black_and_white)
    rgb = []
    for line in black_and_white:
        new_line = []
        for pixel in line:
            new_line.append((pixel*255, pixel*255, pixel*255))
        rgb.append(new_line)

    return np.array(rgb, dtype=np.uint8)


solution_array = solution("input.txt")
print(solution_array)
img = Image.fromarray(solution_array, "RGB")
img.show()
img.save("output.png")