matrix = []
with open("d11.txt") as f:
    for row in f:
        r = [int(nr) for nr in row.rstrip()]
        matrix.append(r)


def increment(matrix):
    flash = set()

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] += 1
            if matrix[row][col] > 9:
                flash.add((row, col))

    return flash


def find_additional_flashes(matrix, already_flashed):
    flash = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 9 and (row, col) not in already_flashed:
                flash.add((row, col))
    return flash


def flash_point(matrix, row, col):
    if not (row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix)):
        return

    matrix[row][col] += 1


def flash_around(matrix, row, col):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            flash_point(matrix, row + i, col + j)


def flash_all(matrix, flashes):
    already_flashed = set()

    while len(flashes) != 0:
        for row, col in flashes:
            flash_around(matrix, row, col)
            already_flashed.add((row, col))
        flashes = find_additional_flashes(matrix, already_flashed)

    for row, col in already_flashed:
        matrix[row][col] = 0

    return len(already_flashed)


def show(matrix):
    for row in matrix:
        print(" ".join([str(nr) for nr in row]))


total = 0

for _ in range(1000):
    flashes = increment(matrix)
    this_round = flash_all(matrix, flashes)
    if this_round == len(matrix) ** 2:
        print(_ + 1)
        break
    total += this_round

print(total)
