import sys

def replace_with_comma(filename1: str, filename2: str):
    lines = open(filename1, "r").readlines()
    output = ""
    for i in range(len(lines) - 1):
        if len(lines[i]) > 1:
            output += lines[i][:-1]
            output += ", "
    output += lines[-1][:-1]
    f = open(filename2, "w")
    f.write(output)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python {} input.txt output.txt".format(__file__))
        exit(1)
    replace_with_comma(sys.argv[1], sys.argv[2])
    exit(0)