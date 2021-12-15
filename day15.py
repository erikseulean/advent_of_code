from heapq import heappop, heappush

initial = []
with open("d15.txt") as f:
    for line in f:
        initial.append([int(nr) for nr in line.strip()])


def find_path(paths, matrix):
    size_x = len(matrix)
    size_y = len(matrix[0])
    hp = [(0, 0, 0)]
    while hp:
        cost, x, y = heappop(hp)

        offset = x // size_x + y // size_y
        current = matrix[x % size_x][y % size_y] + offset

        current = current if current <= 9 else current - 9

        if (x, y) not in paths or current + cost < paths[(x, y)]:
            paths[(x, y)] = current + cost
        else:
            continue

        if x == size_x * 5 - 1 and y == size_y * 5 - 1:
            return paths[(size_x * 5 - 1, size_y * 5 - 1)]

        for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
            if new_x < 0 or new_x >= size_x * 5 or new_y < 0 or new_y >= size_y * 5:
                continue
            heappush(hp, (paths[(x, y)], new_x, new_y))


paths = {}
path_cost = find_path(paths, initial)
print(path_cost - initial[0][0])
