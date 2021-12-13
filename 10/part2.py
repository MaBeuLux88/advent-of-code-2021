f = open('inputs/input2.txt', 'r')
lines = [x.strip() for x in f.readlines()]
score = 0
for l in lines:
    for _ in range(1000):
        l = l.replace('()', '')
        l = l.replace('<>', '')
        l = l.replace('{}', '')
        l = l.replace('[]', '')
    if not any(x in [')', ']', '}', '>'] for x in l):
        for c in reversed(l):
            

print('Score', score)
