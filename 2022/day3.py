from collections import defaultdict
from typing import List

with open("d3.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def get_number(character: str) -> int:

    if character.isupper():
        return ord(character) - ord("A") + 27
    return ord(character) - ord("a") + 1


def find_duplicate_code(line: str) -> int:
    first_rucsack = {line[i] for i in range(len(line) // 2)}
    for i in range(len(line) // 2, len(line)):
        char = line[i]
        if char not in first_rucsack:
            continue
        return get_number(char)

def find_badge(elfs: List[str]) -> int:
    chars = defaultdict(int)

    for elf in elfs:
        for char in set(elf):
            chars[char] += 1
            if chars[char] != 3:
                continue
            return get_number(char)
    

def get_chunks(iterable, chunk_size = 3):
    for start_index in range(0, len(iterable), chunk_size):
        yield iterable[start_index : start_index + chunk_size]

total = 0
for chunk in get_chunks(lines):
    total += find_badge(chunk)
print(total)