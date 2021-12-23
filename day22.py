from typing import Tuple
from collections import defaultdict, Counter
from dataclasses import dataclass

intervals = []
with open("d22.txt") as f:
    for line in f:
        t, cords = line.rstrip().split()
        x, y, z = cords.split(",")
        x = x.split("..")
        y = y.split("..")
        z = z.split("..")
        intervals.append(
            (
                int(x[0].split("=")[1]),
                int(x[1]),
                int(y[0].split("=")[1]),
                int(y[1]),
                int(z[0].split("=")[1]),
                int(z[1]),
                t,
            )
        )


def intersect_singular(a, b, c, d):
    lbound = max(a, c)
    ubound = min(b, d)

    return None if lbound > ubound else (lbound, ubound)


def intersect(c1, c2):
    x = intersect_singular(c1[0], c1[1], c2[0], c2[1])
    y = intersect_singular(c1[2], c1[3], c2[2], c2[3])
    z = intersect_singular(c1[4], c1[5], c2[4], c2[5])

    if (not x) or (not y) or (not z):
        return None

    return (x[0], x[1], y[0], y[1], z[0], z[1])


def get_sum(x):
    return (x[1] - x[0] + 1) * (x[3] - x[2] + 1) * (x[5] - x[4] + 1)


def calculate_intersections(intervals):
    processed = Counter()
    for interval in intervals:
        intersections = Counter()
        for current, times in processed.items():
            intersection = intersect(current, interval)
            if intersection is not None:
                intersections[intersection] -= times
        processed.update(intersections)
        if interval[-1] == "on":
            processed[interval] += 1

    return sum(get_sum(interval) * count for interval, count in processed.items())


def check_condition(interval):
    def check(cords):
        return abs(cords) <= 50

    return all(check(nr) for nr in interval[:-1])


total = calculate_intersections([interval for interval in intervals])
print(total)
