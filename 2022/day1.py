

with open("d1.txt") as f:
    lines = f.readlines()


def most_calories(lines):

    total = 0 
    totals = []
    for line in lines:
        if line == "\n":
            totals.append(total)
            total = 0
            continue
        total += int(line)

    totals.append(total)
    totals = sorted(totals)
    return sum(totals[-3:])

print(most_calories(lines))