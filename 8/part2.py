def read_line(f):
    return [int(x) for x in f.readline().split(',')]


def main():
    f = open("inputs/input1.txt", "r")
    lines = f.readlines()
    numbers = []
    for line in lines:
        input_txt, output_txt = line.split('|')
        inp = [''.join(list(sorted(x))) for x in input_txt.split()]
        out = [''.join(list(sorted(x))) for x in output_txt.split()]
        for i in inp:
            if len(i) == 2:
                one = i
            if len(i) == 3:
                seven = i
            if len(i) == 4:
                four = i
            if len(i) == 7:
                eight = i
        for i in inp:
            if len(i) == 6 and not (one[0] in i and one[1] in i):
                six = i
        for i in inp:
            if len(i) == 5 and all(x in six for x in i):
                five = i
        for i in inp:
            if len(i) == 6 and all(x in i for x in one) and all(x in i for x in five):
                nine = i
        for i in inp:
            if len(i) == 6 and i not in [six, nine]:
                zero = i
        for i in inp:
            if len(i) == 5 and i not in [zero, one, four, five, six, seven, eight, nine] and all(x in i for x in one):
                three = i
        for i in inp:
            if i not in [zero, one, three, four, five, six, seven, eight, nine]:
                two = i
        final = ''
        for i in out:
            if i == zero:
                final += '0'
            elif i == one:
                final += '1'
            elif i == two:
                final += '2'
            elif i == three:
                final += '3'
            elif i == four:
                final += '4'
            elif i == five:
                final += '5'
            elif i == six:
                final += '6'
            elif i == seven:
                final += '7'
            elif i == eight:
                final += '8'
            elif i == nine:
                final += '9'
        numbers.append(int(final))
    print(sum(numbers))


if __name__ == "__main__":
    main()
