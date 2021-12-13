points = set()
folds = []
with open("d13.txt") as f:
    for line in f:
        line = line.rstrip().split(",")
        if line == [""]:
            continue
        if len(line) == 1:
            folds.append(line[0].split()[-1])
        else:
            points.add((int(line[0]), int(line[1])))


def fold_x(points, fold):
    remaining = set()
    for point in points:
        if point[0] < fold:
            remaining.add(point)
        elif 2 * fold - point[0] >= 0:
            remaining.add((2 * fold - point[0], point[1]))
    return remaining


def fold_y(points, fold):
    remaining = set()
    for point in points:
        if point[1] < fold:
            remaining.add(point)
        elif 2 * fold - point[1] >= 0:
            remaining.add((point[0], 2 * fold - point[1]))

    return remaining


for fold in folds:
    direction, location = fold.split("=")
    location = int(location)
    if direction == "x":
        points = fold_x(points, location)
    else:
        points = fold_y(points, location)

matrix = [["."] * 6 for _ in range(50)]
for point in points:
    matrix[point[0]][point[1]] = "#"

for row in matrix:
    print(row)

print(len(points))
