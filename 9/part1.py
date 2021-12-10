f = open('inputs/input1.txt', 'r')
lines = [[int(y) for y in x.strip()] for x in f.readlines()]

x = len(lines[0])
y = len(lines)

risks = []
for i in range(y):
    for j in range(x):
        value = lines[i][j]
        neighbors = [10] * 4
        if i > 0:
            neighbors[0] = lines[i - 1][j]
        if i < y - 1:
            neighbors[1] = lines[i + 1][j]
        if j > 0:
            neighbors[2] = lines[i][j - 1]
        if j < x - 1:
            neighbors[3] = lines[i][j + 1]
        if value < min(neighbors):
            risks.append(value + 1)
print('Risk', sum(risks))
