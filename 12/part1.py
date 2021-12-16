f = open('inputs/input1.txt', 'r')
lines = [[y.strip() for y in x.split('-')] for x in f.readlines()]
starts = list(filter(lambda x: 'start' in x, lines))
possibles = list(filter(lambda x: 'start' not in x, lines))
final_paths = []
current_paths = []
next_gen_paths = []

for s in starts:
    a, b = s if s[0] == 'start' else reversed(s)
    current_paths.append([a, b])

while len(current_paths) != 0:
    next_gen_paths = []
    for cp in current_paths:
        for p in possibles:
            a, b = p if p[0] == cp[-1] else reversed(p)
            new_path = cp[:]
            last = new_path[-1]
            if b not in cp or b.lower() != b:
                if last == a:
                    new_path.append(b)
                    if b == 'end':
                        final_paths.append(new_path)
                    else:
                        next_gen_paths.append(new_path)
    current_paths = next_gen_paths

print('Paths', len(final_paths))
