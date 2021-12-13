from re import sub

f = open('inputs/input1.txt', 'r')
lines = [x.strip() for x in f.readlines()]
scores = []
for l in lines:
    for _ in range(20):  # 11 would be enough but magic number is magic
        l = sub(r'\(\)|\[]|{}|<>', '', l)
    if not any(x in [')', ']', '}', '>'] for x in l):
        score = 0
        for c in reversed(l):
            score = score * 5 + {'(': 1, '[': 2, '{': 3, '<': 4}.get(c)
        scores.append(score)
print('Score', sorted(scores)[len(scores) // 2])
