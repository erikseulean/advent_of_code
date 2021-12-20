def get(i, j, matrix):
    return (
        ("0" if first_run else algo[0]) if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) else matrix[i][j]
    )


def get_bit(i, j, algo, matrix):
    bitmap = [
        get(i - 1, j - 1, matrix),
        get(i - 1, j, matrix),
        get(i - 1, j + 1, matrix),
        get(i, j - 1, matrix),
        get(i, j, matrix),
        get(i, j + 1, matrix),
        get(i + 1, j - 1, matrix),
        get(i + 1, j, matrix),
        get(i + 1, j + 1, matrix),
    ]
    return algo[int("".join(bitmap), 2)]


def find_bits(algo, matrix):
    result = []
    for i in range(-2, len(matrix) + 2):
        row = [get_bit(i, j, algo, matrix) for j in range(-2, len(matrix) + 2)]
        result.append(row)
    return result


with open("d20.txt") as f:
    algo = f.readline().rstrip()
    f.readline()
    initial = [line.rstrip() for line in f]

first_run = True
for _ in range(50):
    initial = find_bits(algo, initial)
    first_run = not first_run

count = sum(int(nr) for row in initial for nr in row)
print(count)
