
all_cords = []
min_x = 500000
max_x = 0
max_y = 0

with open("d14.txt") as f:

    for line in f.readlines():
        line = line.strip().split(" -> ")
        cord_line = []
        for coordinates in line:
            x, y = coordinates.split(",")
            x = int(x)
            y = int(y)
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            cord_line.append((x, y))
        all_cords.append(cord_line)
dimension_x, dimension_y = max_x - min_x + 1, max_y + 1

matrix = [["." for _ in range(dimension_x)] for __ in range(dimension_y)]

for cord_line in all_cords:
    for i in range(len(cord_line) - 1):
        c1, c2 = cord_line[i], cord_line[i + 1]
        extra_x = 1 if c1[0] <= c2[0] else -1
        extra_y = 1 if c1[1] <= c2[1] else -1
        for x in range(c1[0] - min_x, c2[0] - min_x + extra_x, extra_x):
            for y in range(c1[1], c2[1] + extra_y, extra_y):
                matrix[y][x] = "#"


for index in range(len(matrix)):
    matrix[index] = ["."] * 165 + matrix[index] + ["."] * 165

matrix.append(["." for _ in range(len(matrix[0]))])
matrix.append(["#" for _ in range(len(matrix[0]))])


for row in matrix:
    print(" ".join(row))


def find_next(current_x, current_y, matrix):

    if current_x + 1 == len(matrix):
        return -1 
    
    if matrix[current_x + 1][current_y] == ".":
        return current_x + 1, current_y
    
    if current_y - 1 < 0:
        print("GOT OUTSIDE", len(matrix))
        raise Exception()
    
    if matrix[current_x + 1][current_y - 1] == ".":
        return current_x + 1, current_y - 1

    if current_y + 1 == len(matrix[0]):
        print("GOT OUTSIDE", len(matrix))
        raise Exception()

    if matrix[current_x + 1][current_y + 1] == ".":
        return current_x + 1, current_y + 1

    return 1

def fall_sand(matrix):

    current_y = 500 - min_x + 160
    current_x = 0

    initial_x, initial_y =  current_x, current_y
    while True:
        next = find_next(current_x, current_y, matrix)
        if next == -1:
            return 0
        if next == 1:
            if initial_x == current_x and initial_y == current_y:
                return 0
            matrix[current_x][current_y] = "o"
            return 1
        if next[0] == current_x and next[1] == current_y:
            return 1
        current_x, current_y = next[0], next[1]

        if initial_x == current_x and initial_y == current_y:
           return 0

index = 1
while fall_sand(matrix):
    print(f"Step {index}") 
    index += 1


for row in matrix:
    print("".join(row))