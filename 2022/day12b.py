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
    return x >= 0 and x < len(elevations) and y >= 0 and y < len(elevations[x]) and (elevations[x][y] >= current_elevation or current_elevation == elevations[x][y] + 1) 


def find_path(elevations, start):

    q = Queue()
    q.put((start[0], start[1], 0))
    initial = [x[:] for x in elevations]
    visited = set([start])
    while not q.empty():
        x, y, steps = q.get()
        for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (new_x, new_y) in visited:
                continue
            if not can_go(new_x, new_y, elevations[x][y], elevations):
                continue
            if elevations[new_x][new_y] == 0:
                return steps + 1
            visited.add((new_x, new_y))    
            q.put((new_x, new_y, steps + 1))
steps = find_path([x[:] for x in elevations], end)
print(steps)
