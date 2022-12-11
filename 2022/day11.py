from typing import Dict
from typing import Iterator
from typing import List

from collections import defaultdict


with open("d11.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def get_monkey_lines(lines: List[str]) -> Iterator[str]:

    for index in range(0, len(lines), 7):
        yield lines[index: index + 6]


def parse_monkey_lines(lines):
    index = int(lines[0][len("Monkey "):].split(":")[0])
    items =  [int(item) for item in lines[1][len("Starting items: "):].split(",")]
    formula = lines[2][len("Operation: new = "):]
    divisible_by = int(lines[3][len("Test: divisible by "): ])
    true_throw_to = int(lines[4][len("If true: throw to monkey "):])
    false_throw_to = int(lines[5][len("If false: throw to monkey "):])

    return index, {
        "items": items,
        "formula": formula,
        "divisible_by": divisible_by,
        True : true_throw_to,
        False: false_throw_to
    }

monkeys = {}

for l in get_monkey_lines(lines):
    monkey_index, monkey = parse_monkey_lines(l)
    monkeys[monkey_index] = monkey


def play_round(item_counts, modulo):

    for monkey_index in range(len(monkeys)):
        monkey = monkeys[monkey_index]
        for old in monkey["items"]:
            new = eval(monkey["formula"])
            new = new % modulo
            # new = new // 3
            throw_to = monkey[new % monkey["divisible_by"] == 0]
            monkeys[throw_to]["items"].append(new)
        item_counts[monkey_index] += len(monkey["items"])
        monkeys[monkey_index]["items"] = []


modulo = 1
for monkey in monkeys.values():
    modulo *= monkey["divisible_by"]

  
item_counts = defaultdict(int)
for round in range(10000):
    play_round(item_counts, modulo)
items = sorted(item_counts.values(), reverse=True)
print(items[0] * items[1])
