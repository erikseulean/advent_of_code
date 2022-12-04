with open("d4.txt") as f:
    lines = f.readlines()


def a_contains_b(start_a, end_a, start_b, end_b) -> bool:
    return (
        start_b >= start_a and 
        start_b <= end_a and 
        end_b >= start_a and 
        end_b <= end_a
    )

def is_intersect(p1: str, p2: str) -> bool:
    start_p1, end_p1 = [int(nr) for nr in p1.split("-")]
    start_p2, end_p2 = [int(nr) for nr in p2.split("-")]

    return (
        start_p2 <= start_p1 <= end_p2 or 
        start_p2 <= end_p1 <= end_p2 or
        start_p1 <= start_p2 <= end_p1 or
        start_p1 <= end_p2 <= end_p1
    )


def is_contained(p1: str, p2: str) -> bool:

    start_p1, end_p1 = [int(nr) for nr in p1.split("-")]
    start_p2, end_p2 = [int(nr) for nr in p2.split("-")]

    return a_contains_b(start_p1, end_p1, start_p2, end_p2) or \
        a_contains_b(start_p2, end_p2, start_p1, end_p1)

total = 0
for line in lines:
    p1, p2 = line.strip().split(",")
    total += is_intersect(p1, p2)

print(total)