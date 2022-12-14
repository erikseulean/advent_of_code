from typing import Iterator
from typing import List


def find_list_ends(elements, start, end):
    
    counter = 0
    for i in range(start, end):
        if elements[i] == "]":
            counter -= 1
        elif elements[i] == "[":
            counter += 1
        
        if counter == 0:
            return i

def find_number_end(elements, start, end):

    while start < len(elements) and start < end and elements[start] != ",":
        start += 1
    
    return start

def parse_input(elements, start, end):
    #breakpoint()
    if not elements:
        return
    current = start
    result = []
    while current < end:
        if elements[current] == "[":
            list_end = find_list_ends(elements, current, end)
            result.extend([parse_input(elements, current + 1, list_end)])
            start = list_end + 2
            current = list_end + 2
            continue
        else:
            number_end = find_number_end(elements, start, end)
            number = int(elements[start: number_end])
            result.append(number)
            start = number_end + 1
            current = number_end + 1

    return result
    

with open("d13.txt") as f:
    lines = [line.strip() for line in f.readlines()]


def get_pairs(lines: List[str]) -> Iterator[str]:

    for index in range(0, len(lines), 2):
        yield lines[index: index + 2]


def compare(left, right):

    if isinstance(left, int):
        if isinstance(right, int):
            return left - right
        else:
            return compare([left], right)
    else:
        if isinstance(right, int):
            return compare(left, [right])

    for left_v, right_v in zip(left, right):
        value = compare(left_v, right_v)
        if value:
            return value   

    return len(left) - len(right)

result = []
for line in lines:
    lists = parse_input(line, 0, len(line))
    if not lists:
        continue
    result.append(lists[0])

    
index = 1
sum = 0
for pairs in get_pairs(result):
    in_order = compare(pairs[0], pairs[1])
    if in_order < 0:
        sum += index
    index += 1
print(sum)

result.append([[2]])
result.append([[6]])

from functools import cmp_to_key
result = sorted(result, key=cmp_to_key(compare))

indices = [index + 1 for index, value in enumerate(result) if value == [[6]] or value == [[2]]]
print(indices[0] * indices[1])