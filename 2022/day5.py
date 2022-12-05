from typing import Dict
from typing import List

with open("d5.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

stacks = lines[:9]
operations = lines[10:]


def create_stacks(stack_data: List[str]) -> Dict[int, List[str]]:

    stacks = {}

    for index, stack_values in enumerate(stack_data):
        stacks[index + 1] = [letter for letter in stack_values[::-1]]
    
    return stacks


stacks = create_stacks(stacks)

def handle_operation(from_index: int, to_index: int, how_many: int, stacks: List[str]) -> None:
    from_stack = stacks[from_index]
    to_stack = stacks[to_index]

    for _ in range(how_many):
        to_stack.append(from_stack.pop())


def handle_operation_p2(from_index: int, to_index: int, how_many: int, stacks: List[str]) -> None:
    
    to_move = stacks[from_index][-how_many:]
    stacks[from_index] = stacks[from_index][:-how_many]
    stacks[to_index].extend(to_move)
    

def get_result(stacks: List[str]) -> None:

    for i in range(1, len(stacks) + 1):
        print(stacks[i][-1] if stacks[i] else "")

for operation in operations:
    ops = operation.split(" ")
    how_many = int(ops[1])
    from_index = int(ops[3])
    to_index = int(ops[5])

    handle_operation_p2(from_index, to_index, how_many, stacks)

get_result(stacks)