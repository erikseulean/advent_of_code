from collections import defaultdict

scanners = defaultdict(set)
scanner_locations = {}

with open("d19.txt") as f:

    for line in f:
        line = line.rstrip()
        if line == "":
            continue
        if "---" in line:
            scanner_index = int(line.split()[2])
            continue

        x, y, z = tuple(line.split(","))
        x, y, z = int(x), int(y), int(z)
        scanners[scanner_index].add((x, y, z))


def rotate_coordinates(cords):
    rotations = []

    x, y, z = cords
    # can do these with permutations but will think about it later
    return [
        (x, y, z),
        (z, x, y),
        (y, z, x),
        (-x, z, y),
        (y, -x, z),
        (z, y, -x),
        (-y, x, z),
        (z, -y, x),
        (x, z, -y),
        (y, x, -z),
        (-z, y, x),
        (x, -z, y),
        (x, -y, -z),
        (-z, x, -y),
        (-y, -z, x),
        (-x, -y, z),
        (z, -x, -y),
        (-y, z, -x),
        (-x, y, -z),
        (y, -z, -x),
        (-z, -x, y),
        (-z, -y, -x),
        (-y, -x, -z),
        (-x, -z, -y),
    ]


def tuple_diff(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1], t1[2] - t2[2])


def tuple_add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], t1[2] + t2[2])


def manhattan(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1]) + abs(d1[2] - d2[2])


def determine_position(first_scanner, unknown_scanner):
    # we need all rotations of all beacons together
    # eg, we need to apply first rotation, second, etc to all
    # at the same time.
    for beacons in zip(*(rotate_coordinates(beacon) for beacon in scanners[unknown_scanner])):
        for b1 in scanners[first_scanner]:
            for b2 in beacons:
                diff = tuple_diff(b1, b2)
                update = {tuple_add(b, diff) for b in beacons}
                if len(scanners[first_scanner].intersection(update)) >= 12:
                    # keep them relative to the found scanner
                    scanners[unknown_scanner] = set(tuple(b) for b in beacons)
                    location = tuple_add(scanner_locations[first_scanner], diff)
                    scanner_locations[unknown_scanner] = location
                    return True


queue = [0]
scanner_locations[0] = (0, 0, 0)
while queue:
    not_found = [scanner for scanner in scanners.keys() if scanner not in scanner_locations]
    next_discovered_scanner = queue.pop()
    for undiscovered_scanner in not_found:
        found = determine_position(next_discovered_scanner, undiscovered_scanner)
        if found:
            queue.append(undiscovered_scanner)


all_beacons = set()
for scanner, beacons in scanners.items():
    locations = {tuple_add(beacon, scanner_locations[scanner]) for beacon in beacons}
    all_beacons.update(locations)

max_val = 0

for v1 in scanner_locations.values():
    for v2 in scanner_locations.values():
        if v1 == v2:
            continue
        max_val = max(manhattan(v1, v2), max_val)

print(len(all_beacons))
print(max_val)
