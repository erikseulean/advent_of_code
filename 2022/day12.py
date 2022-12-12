from queue import Queue

start = None
end = None
elevations = []
with open("d12.txt") as f:
    for line in f.readlines():
        line = line.strip()
        elevation = []
        for index, char in enumerate(line):
            if char == "S":
                start = (len(elevations), index)
                elevation.append(0)
                continue
            if char == "E":
                end = (len(elevations), index)
                elevation.append(25)
                continue
            elevation.append(ord(char) - ord("a"))
        elevations.append(elevation)


def can_go(x, y, current_elevation, elevations):
    return x >= 0 and x < len(elevations) and y >= 0 and y < len(elevations[x]) and elevations[x][y] >= 0 and elevations[x][y] - current_elevation <= 1


def update_cache(path, cache, cache_value = 0):

    for index, pos in enumerate(path[::-1]):
        cache[pos] = index + cache_value


def find_path(elevations, start, end, cache):

    q = Queue()
    q.put((start[0], start[1], 0, [start]))

    while not q.empty():
        x, y, steps, path = q.get()

        if (x, y) in cache:
            cache_value = cache[(x, y)]
            if cache_value == -1:
                continue

            update_cache(path, cache, cache_value)
            return steps + cache_value - 1
        current_elevation = elevations[x][y]
        elevations[x][y] = -1
        if (x, y) == end:
            update_cache(path, cache, 0)
            return steps
        for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not can_go(new_x, new_y, current_elevation, elevations):
                continue
            new_path = list(path)
            new_path.append((new_x, new_y))
            q.put((new_x, new_y, steps + 1, new_path))
    cache[start] = -1
# steps = find_path(elevations, start, end, cache)
# print(steps)

cache = dict()

best_min = 100000
for row in range(len(elevations)):
    for column in range(len(elevations)):
        if elevations[row][column] != 0:
            continue
        breakpoint()
        steps = find_path([x[:] for x in elevations], (row, column), end, cache)
        if steps is None:
            continue
        best_min = min(best_min, steps)
        print(best_min)
breakpoint()
print(best_min)