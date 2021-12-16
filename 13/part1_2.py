def read_inputs():
    f = open('inputs/input1.txt', 'r')
    dots = []
    folds = []
    dot = f.readline()
    while dot.strip() != '':
        dots.append([int(x) for x in dot.split(',')])
        dot = f.readline()

    read_folds = [[x for x in y.split()] for y in f.readlines()]

    for f in read_folds:
        x, y = f[2].split('=')
        folds.append([x, int(y)])
    return dots, folds


def generate_map(dots, x, y):
    lines = []
    for y in range(y):
        lines.append(['.'] * x)
    for d in dots:
        x, y = d
        lines[y][x] = '#'
    return lines


def print_map(my_map):
    for l in my_map:
        print(''.join(l))


def fold_x(dots, v):
    res = []
    for d in dots:
        x, y = d
        res.append(d if x < v else [2 * v - x, y])
    return res


def fold_y(dots, v):
    res = []
    for d in dots:
        x, y = d
        res.append(d if y < v else [x, 2 * v - y])
    return res


def fold(fold_props, dots):
    axis, v = fold_props
    if axis == 'y':
        return fold_y(dots, v)
    else:
        return fold_x(dots, v)


def main():
    dots, folds = read_inputs()

    init_max_x = max([d[0] for d in dots]) + 1
    init_max_y = max([d[1] for d in dots]) + 1

    x = init_max_x
    y = init_max_y
    for f in folds:
        dots = fold(f, dots)
        uniq_dots = []
        for d in dots:
            if d not in uniq_dots:
                uniq_dots.append(d)
        print('Nb unique dots after fold', f, ':', len(uniq_dots))
        axis, v = f
        if axis == 'x':
            x = v
        else:
            y = v

    my_map = generate_map(dots, x, y)
    print_map(my_map)


if __name__ == '__main__':
    main()
