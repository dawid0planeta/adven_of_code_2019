from Proc import Proccessor


def read_file(filename: str) -> list:
    with open(filename, 'r') as f:
        memory = [int(elem) for elem in f.readline().split(',')]
    return memory


memory = read_file("new_input.txt")
proc = Proccessor(memory)
out = proc.run()
while out[0] != "HALT":
    if out[0] == "INPUT":
        out = proc.run(2)
        continue
    elif out[0] == "OUTPUT":
        print(out[1])
    out = proc.run()