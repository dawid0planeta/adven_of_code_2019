from Proc import Proccessor


def read_file(filename: str) -> list:
    with open(filename, 'r') as f:
        memory = [int(elem) for elem in f.readline().split(',')]
    return memory


def main(filename: str) -> None:
    memory = read_file(filename)
    proc = Proccessor(memory)
    out = proc.execute()
    while out[0] != "HALT":
        if out[0] == "INPUT":
            out = proc.execute(int(input("Podaj input: ")))
        else:
            if out[0] == "OUTPUT":
                print(out[1])
            out = proc.execute()
        

    




main("input.txt")
