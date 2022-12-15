import re

regex = re.compile("-?\d+")

sensors = set()
beacons = set()

with open("d15.txt") as f:
    for line in f.readlines():
        sx, sy, bx, by = regex.findall(line)
        sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
        distance = abs(sx - bx) + abs(sy - by)
        sensors.add((sx, sy, distance))
        beacons.add((bx, by))

def is_valid(x, y):

    for sx, sy, distance in sensors:
        
        distance_to_coordinate = abs(sx - x) + abs(sy - y)
        if distance_to_coordinate <= distance:
            return False
    return True

Y = 2000000

# count = 0
# for x in range(-10000000, 10000000):
#     count += int(not is_valid(x, Y) and (x, Y) not in beacons)

# print(count)

found_p2 = False
checked = 0
for (sx,sy,d) in sensors:
    # for each sensor, look at all possible distances from x
    # coordinate, and then calculate the distance to y coordinate

    # then consider the x, y coordinates in all 4 possible
    # directions, and if they are in the given boundaries,
    # and a beacon can be there, it means it's the one you're
    # looking for.
    for dx in range(d+2):
        dy = (d+1)-dx
        for direction_x, direction_y in [(-1,-1),(-1,1),(1,-1),(1,1)]:
            checked += 1
            x = sx + (dx * direction_x)
            y = sy + (dy * direction_y)
            if not (0<=x<=4000000 and 0<=y<=4000000):
                continue
            if not is_valid(x,y):
                continue
            print(x*4000000 + y)
            exit(0)