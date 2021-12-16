from copy import deepcopy

f = open('inputs/input1.txt', 'r')
template = f.readline().strip()
f.readline()
rules = dict(list(map(lambda x: [x[0], x[2]], [[y for y in x.split()] for x in f.readlines()])))
pairs = []

for i in range(len(template) - 1):
    pairs.append(template[i:i + 2])

count_pairs = {}
for r in rules:
    count_pairs[r] = pairs.count(r)

for loop in range(1, 41):
    next_count_pairs = deepcopy(count_pairs)
    for k, v in rules.items():
        k1 = k[0] + v
        k2 = v + k[1]
        new_value = count_pairs.get(k)
        next_count_pairs[k] -= new_value
        next_count_pairs[k1] += new_value
        next_count_pairs[k2] += new_value
    count_pairs = next_count_pairs

    if loop == 40:
        letter_count = {}
        for k, v in count_pairs.items():
            l1, l2 = k
            letter_count[l1] = letter_count.get(l1, 0) + v
        last_letter = template[-1]
        letter_count[last_letter] += 1
        print('Count', letter_count)
        values = letter_count.values()
        print('Solution', max(values) - min(values))
