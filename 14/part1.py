f = open('inputs/input1.txt', 'r')
template = f.readline().strip()
f.readline()
rules = dict(list(map(lambda x: [x[0], x[2]], [[y for y in x.split()] for x in f.readlines()])))
pairs = []
for _ in range(10):
    for i in range(len(template) - 1):
        pairs.append(template[i:i + 2])
    for i, p in enumerate(pairs):
        r = rules.get(p)
        pairs[i] = p[0] + r
    template = ''.join(pairs) + template[-1]
    pairs = []

    counts = []
    for l in set(template):
        counts.append(template.count(l))
    print('===>', max(counts) - min(counts))

