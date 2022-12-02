
with open("d2.txt") as f:
    lines = f.readlines()


options_map = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

points = {
    "AA": 3,
    "AB": 6,
    "AC": 0,
    "BA": 0,
    "BB": 3,
    "BC": 6,
    "CA": 6,
    "CB": 0,
    "CC": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}


what_to_pick = {
    "X": {
        "A": "C",
        "B": "A",
        "C": "B"
    },
    "Y": {
        "A": "A",
        "B": "B",
        "C": "C",
    },
    "Z": {
        "A": "B",
        "B": "C",
        "C": "A",
    }
}


def p1(lines):
    total = 0 
    for line in lines:
        oponent, you = line.split()
        you = options_map[you]
        total += points[f"{oponent}{you}"] + points[f"{you}"]
    return total

def p2(lines):
    total = 0
    for line in lines:
        oponent, to_do = line.split()
        you = what_to_pick[to_do][oponent]
        total += points[f"{oponent}{you}"] + points[f"{you}"]
    return total
print(p2(lines))