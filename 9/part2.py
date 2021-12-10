from math import prod


def find_bassin_around(pos, set, lines, max_height, max_length):
    i, j = pos
    if lines[i][j] == 9:
        return set
    set.add((i, j))
    if i > 0 and (i - 1, j) not in set:
        find_bassin_around([i - 1, j], set, lines, max_height, max_length)
    if i < max_height - 1 and (i + 1, j) not in set:
        find_bassin_around([i + 1, j], set, lines, max_height, max_length)
    if j > 0 and (i, j - 1) not in set:
        find_bassin_around([i, j - 1], set, lines, max_height, max_length)
    if j < max_length - 1 and (i, j + 1) not in set:
        find_bassin_around([i, j + 1], set, lines, max_height, max_length)
    return set


def main():
    f = open('inputs/input1.txt', 'r')
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]

    max_length = len(lines[0])
    max_height = len(lines)

    locs = []
    for i in range(max_height):
        for j in range(max_length):
            value = lines[i][j]
            neighbors = [10] * 4
            if i > 0:
                neighbors[0] = lines[i - 1][j]
            if i < max_height - 1:
                neighbors[1] = lines[i + 1][j]
            if j > 0:
                neighbors[2] = lines[i][j - 1]
            if j < max_length - 1:
                neighbors[3] = lines[i][j + 1]
            if value < min(neighbors):
                locs.append([i, j])

    bassins = []
    for loc in locs:
        bassins.append(len(find_bassin_around(loc, set(), lines, max_height, max_length)))
    print(prod(sorted(bassins)[-3:]))


if __name__ == '__main__':
    main()
