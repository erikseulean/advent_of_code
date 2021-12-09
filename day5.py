from collections import defaultdict


def expand_coordinates(x1, x2, all_cords):
    min_x, max_x = min(x1[0], x2[0]), max(x1[0], x2[0])
    min_y, max_y = min(x1[1], x2[1]), max(x1[1], x2[1])

    cords = []
    if min_x == max_x:
        for z in range(min_y, max_y + 1):
            all_cords[(min_x, z)] += 1
    elif min_y == max_y:
        for z in range(min_x, max_x + 1):
            all_cords[(z, min_y)] += 1
    elif abs(x1[0] - x2[0]) == abs(x1[1] - x2[1]):
        sign_x = -1 if x1[0] > x2[0] else 1
        sign_y = -1 if x1[1] > x2[1] else 1
        current_x, current_y = x1[0], x1[1]
        for steps in range(abs(x1[0] - x2[0]) + 1):
            all_cords[(current_x, current_y)] += 1
            current_x += 1 * sign_x
            current_y += 1 * sign_y


def format(cord):
    cord = cord.split(",")
    cord = (int(cord[0]), int(cord[1]))
    return cord


covered = defaultdict(int)
with open("d5.txt") as f:
    for line in f:
        c1, _, c2 = line.split()
        c1, c2 = format(c1), format(c2)
        expand_coordinates(c1, c2, covered)

count = 0
for item in covered.values():
    count += item >= 2

print(count)
