bingo = []
all_matrices = []


def transform_matrix_into_bingo(matrix):
    bingos = []
    all_matrix = set()
    for line in matrix:
        bingos.append(set(line))
        all_matrix.update(bingos[-1])

    for j in range(5):
        column = set()
        for i in range(5):
            column.add(matrix[i][j])
        bingos.append(column)
    return bingos, all_matrix


with open("d4.txt") as f:
    numbers = f.readline()
    numbers = [int(nr) for nr in numbers.split(",")]
    matrix = []
    f.readline()
    for line in f:
        line = line.strip()
        if len(line) == 0:
            bingos, m = transform_matrix_into_bingo(matrix)
            bingo.append(bingos)
            all_matrices.append(m)
            matrix = []
        else:
            line = line.split()
            matrix.append([int(nr) for nr in line])
    bingos, m = transform_matrix_into_bingo(matrix)
    bingo.append(bingos)
    all_matrices.append(m)


def find_bingo(bingo, numbers, until_last):
    last = None
    for number in numbers:
        for i in range(len(bingo)):
            if i not in boards:
                continue
            for j in range(10):
                if number not in bingo[i][j]:
                    continue

                all_matrices[i].discard(number)
                bingo[i][j].remove(number)
                if bingo[i][j]:
                    continue

                if not until_last:
                    return number, all_matrices[i]

                if not last or last != i:
                    last = i

                boards.discard(i)
                if not boards:
                    return number, all_matrices[last]


boards = set([i for i in range(len(all_matrices))])
number, matrix = find_bingo(bingo, numbers, False)
print(number * sum(matrix))


number, matrix = find_bingo(bingo, numbers, True)
print(number * sum(matrix))
