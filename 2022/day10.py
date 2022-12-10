from typing import Dict
from typing import List
from typing import Tuple

with open("d10.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

def is_match(sprite, X) -> bool:
    return sprite - 1 == X or sprite == X or sprite + 1 == X

def get_panel_number(cycle_number: int) -> int:
    return cycle_number // 40

def draw(X: int, pixel: int, current_cycle: int, panels: List[List[str]]) -> None:
    
    if not is_match(X, pixel):
        return
    
    panel_number = get_panel_number(current_cycle)
    panels[panel_number].add(pixel)

def handle_noop(cycles: Dict[str, int], current_cycle: int, X: int, panels: List[set]) -> Tuple[Dict[str, int], int, int]:
    pixel = (current_cycle - 1) % 40
    cycles[current_cycle] = X

    draw(X, pixel, current_cycle, panels)

    return cycles, current_cycle + 1, X

def handle_add(cycles: Dict[str, int], current_cycle: int, X: int, value: int, panels) -> Tuple[Dict[str, int], int]:

    for cycle in [current_cycle, current_cycle + 1]:
        cycles[cycle] = X
        pixel = (cycle - 1) % 40    
        draw(X, pixel, cycle - 1, panels)

    return cycles, current_cycle + 2, X + value


def get_register_values(instructions: List[str]) -> Tuple[Dict[int, int], List[List[str]]]:
    X = 1
    current_cycle = 1
    panels = [set() for _ in range(6)]
    cycles = {current_cycle: X}
    for instruction in instructions:
        instruction = instruction.split()
        if instruction[0] == "noop":
            cycles, current_cycle, X = handle_noop(cycles, current_cycle, X, panels)
        else:
            cycles, current_cycle, X = handle_add(cycles, current_cycle, X, int(instruction[1]), panels)

    return cycles, panels


cycles, panels = get_register_values(instructions)
values = [20, 60, 100, 140, 180, 220]

sum = 0 
for value in values:
    sum += cycles[value] * value
print(sum)


for line in range(6):
    l = ["#" if index in panels[line] else "." for index in range(40)]
    print("".join(l))
