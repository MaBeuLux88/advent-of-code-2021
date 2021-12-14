def octo_print(octopus):
    for o in octopus:
        print(''.join(map(str, map(lambda x: 0 if x < 0 else x, o))))


def get_list_explosions(octopus):
    nb_lines = len(octopus)
    nb_column = len(octopus[0])

    explosions = []
    for l in range(nb_lines):
        for c in range(nb_column):
            if octopus[l][c] > 9:
                explosions.append([l, c])
    return explosions


def explosion(octopus, explo):
    l, c = explo
    nb_lines = len(octopus)
    nb_column = len(octopus[0])
    octopus[l][c] = -10
    for nl in range(-1, 2):
        for nc in range(-1, 2):
            if 0 <= l + nl < nb_lines and 0 <= nc + c < nb_column:
                octopus[l + nl][nc + c] += 1


def next_step(octopus):
    nb_lines = len(octopus)
    nb_column = len(octopus[0])
    for l in range(nb_lines):
        for c in range(nb_column):
            if octopus[l][c] < 0:
                octopus[l][c] = 0
            octopus[l][c] += 1


def main():
    f = open('inputs/input1.txt', 'r')
    octopus = [[int(y) for y in x.strip()] for x in f.readlines()]
    # print('Step 0')
    # octo_print(octopus)
    flashes = 0

    for step in range(101):
        explosions = get_list_explosions(octopus)
        flashes += len(explosions)
        while len(explosions) != 0:
            for explo in explosions:
                explosion(octopus, explo)
            explosions = get_list_explosions(octopus)
            flashes += len(explosions)

        # print('\nStep ' + str(step + 1))
        # octo_print(octopus)
        next_step(octopus)

    print('Flashes', flashes)


if __name__ == '__main__':
    main()
