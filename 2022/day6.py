from typing import List

def find_start_of_unique_sequence(letters: List[str]):

    positions = dict()
    start = -1

    for i, character in enumerate(letters):
        if character in positions and positions[character] >= start:
            start = positions[character] + 1
        positions[character] = i

        if i - start == 14:
            return i


with open("d6.txt") as f:
    print(find_start_of_unique_sequence(f.readline()))
