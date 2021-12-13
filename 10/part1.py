from re import sub

f = open('inputs/input1.txt', 'r')
lines = [x.strip() for x in f.readlines()]
score = 0
for l in lines:
    for _ in range(20):
        l = sub(r'\(\)|\[]|{}|<>', '', l)
    for _ in range(20):
        l = sub(r'[(\[{<]', '', l)
    if len(l) != 0:
        score += {')': 3, ']': 57, '}': 1197, '>': 25137}.get(l[0])
print('Score', score)
