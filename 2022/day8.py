from typing import List
from typing import Set


m = []
with open("d8.txt") as f:
    for line in f.readlines():
        numbers = [int(nr) for nr in line.strip()]
        m.append(numbers)


def is_higher(row: int, column: int, m: List[List[str]], highest_value: int):
    return (
            row == 0 or 
            column == 0 or 
            row == len(m) - 1 or 
            column == len(m[row]) - 1 or
            highest_value < m[row][column]
        )

def find_higher_trees(fixed: int, visible_trees: Set, m: List[List[int]], range_values):

    highest_column = -1
    highest_row = -1
    for index in range_values:
        if is_higher(index, fixed, m, highest_row):
            visible_trees.add((index, fixed))
        
        if is_higher(fixed, index, m, highest_column):
            visible_trees.add((fixed, index))
        highest_column = max(highest_column, m[fixed][index])
        highest_row = max(highest_row, m[index][fixed])


def check_trees(index, visible_trees, m):

    find_higher_trees(index, visible_trees, m, range(len(m)))
    find_higher_trees(index, visible_trees, m, range(len(m) - 1, -1, -1))


def find_visible_trees(m: List[List[int]]) -> int:

    visible_trees = set()
    for row in range(len(m)):
        check_trees(row, visible_trees, m)
    
    return len(visible_trees)


def find(row: int, column: int, m):

    val = m[row][column]
    L = R = U = D = 0
    for x in range(column - 1, -1, -1):
        L += 1
        if m[row][x] >= val:
            break
    for x in range(column + 1, len(m[row])):
        R += 1
        if m[row][x] >= val:
            break
    for x in range(row - 1, -1, -1):
        U += 1
        if m[x][column] >= val:
            break
    for x in range(row + 1, len(m)):
        D += 1
        if m[x][column] >= val:
            break
    return U * D * L * R

def find_tree_points(m):

    max_value = 0
    for row in range(len(m)):
        for col in range(len(m[row])):
            max_value = max(max_value, find(row, col, m))
    return max_value
    

print(find_tree_points(m))