f = open('inputs/input1.txt', 'r')
lines = [x.strip() for x in f.readlines()]
score = 0
for l in lines:
    for _ in range(1000):
        l = l.replace('()', '')
        l = l.replace('<>', '')
        l = l.replace('{}', '')
        l = l.replace('[]', '')
    for _ in range(1000):
        l = l.replace('(', '')
        l = l.replace('<', '')
        l = l.replace('{', '')
        l = l.replace('[', '')
    if len(l) != 0:
        x = l[0]
        if x == ')':
            score += 3
        if x == ']':
            score += 57
        if x == '}':
            score += 1197
        if x == '>':
            score += 25137
print('Score', score)
