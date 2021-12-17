f = open('inputs/input1.txt', 'r')
matrix = [[int(y) for y in x.strip()] for x in f.readlines()]

matrix_max_x = len(matrix[0])
matrix_max_y = len(matrix)
paths_risks = [{'path': [[0, 0]], 'risk': 0}]
new_paths = []
solutions = []

draft_risk = [0, 0]
for i in range(matrix_max_x - 1):
    draft_risk[0] += matrix[i][i + 1] + matrix[i + 1][i + 1]
    draft_risk[1] += matrix[i + 1][i] + matrix[i + 1][i + 1]
best_risk = min(draft_risk)

loop_again = True
while loop_again:
    loop_again = False
    new_paths = []
    for pr in paths_risks:
        path = pr.get('path')
        risk = pr.get('risk')
        x, y = path[-1]
        if x + 1 < matrix_max_x:
            loop_again = True
            new_path = path[:]
            new_path.append([x + 1, y])
            new_paths.append({'path': new_path, 'risk': risk + matrix[x + 1][y]})
        if y + 1 < matrix_max_y:
            loop_again = True
            new_path = path[:]
            new_path.append([x, y + 1])
            new_paths.append({'path': new_path, 'risk': risk + matrix[x][y + 1]})
        if x > 1:
            loop_again = True
            new_path = path[:]
            new_path.append([x - 1, y])
            new_paths.append({'path': new_path, 'risk': risk + matrix[x - 1][y]})
        if y > 1:
            loop_again = True
            new_path = path[:]
            new_path.append([x, y - 1])
            new_paths.append({'path': new_path, 'risk': risk + matrix[x][y - 1]})

    new_paths = sorted(new_paths, key=lambda x: x.get('path')[-1][0] + x.get('path')[-1][1], reverse=True)[:500]
    new_paths = sorted(new_paths, key=lambda x: x.get('risk'))
    winning_paths = []
    points = []
    for np in new_paths:
        path = np.get('path')
        risk = np.get('risk')
        last = path[-1]
        if risk > best_risk:
            continue
        if last not in points and len(path) == len(set([tuple(x) for x in path])) and [matrix_max_x - 1, matrix_max_y - 1] != last:
            winning_paths.append(np)
            points.append(last)
        if [matrix_max_x - 1, matrix_max_y - 1] == last:
            solutions.append(np)
            break
    paths_risks = winning_paths
    best_risk = min([x.get('risk') for x in solutions], default=best_risk)
print('Solution', best_risk)
