matrix = []
visited = []


def basin(i, j):
    if matrix[i][j] == 9:
        return 0

    if visited[i][j]:
        return 0

    visited[i][j] = True

    return 1 + basin(i - 1, j) + basin(i + 1, j) + basin(i, j - 1) + basin(i, j + 1)


def add_row(new_row):
    r = [9]
    for nr in new_row:
        r.append(int(nr))
    r.append(9)
    visited.append([0] * (len(new_row) + 2))
    matrix.append(r)


with open("d9.txt") as f:
    first_line = f.readline().rstrip()
    matrix.append([9] * (len(first_line) + 2))
    visited.append([False] * (len(first_line) + 2))
    add_row(first_line)
    for line in f:
        add_row(line.rstrip())
    matrix.append([9] * (len(first_line) + 2))
    visited.append([False] * (len(first_line) + 2))

smallest_sum = 0
sums = []
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        if (
            matrix[i][j] < matrix[i - 1][j]
            and matrix[i][j] < matrix[i + 1][j]
            and matrix[i][j] < matrix[i][j - 1]
            and matrix[i][j] < matrix[i][j + 1]
        ):
            smallest_sum += matrix[i][j] + 1
            sums.append(basin(i, j))

sums = sorted(sums)
print(smallest_sum)
print(sums[-1] * sums[-2] * sums[-3])
