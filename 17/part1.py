from re import findall


def read_target():
    f = open('inputs/input1.txt', 'r')
    return findall(r'-?[0-9]{2,3}', f.readline())


def main():
    x1, x2, y1, y2 = read_target()
    20
    19
    17
    14
    10
    5
    -1


if __name__ == '__main__':
    main()
