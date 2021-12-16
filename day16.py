binaries = []

hexbin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def convert(hex):
    return "".join([hexbin[c] for c in hex])


def combine_numbers(numbers, operation):
    operation = int(operation, 2)
    if operation == 0:
        return sum(numbers)
    if operation == 1:
        prod = 1
        for nr in numbers:
            prod = prod * nr
        return prod
    if operation == 2:
        return min(numbers)
    if operation == 3:
        return max(numbers)
    if operation == 5:
        return int(numbers[0] > numbers[1])
    if operation == 6:
        return int(numbers[0] < numbers[1])
    if operation == 7:
        return int(numbers[0] == numbers[1])


def find_end(binary, start):

    nr = []
    while binary[start] != "0":
        nr.append(binary[start + 1 : start + 5])
        start = start + 5
    nr.append(binary[start + 1 : start + 5])
    return start + 5, int("".join(nr), 2)


def decode_package(binary, start):
    package_version = binary[start : start + 3]
    package_type = binary[start + 3 : start + 6]

    if int(package_type, 2) == 4:
        end, number = find_end(binary, start + 6)
        return int(package_version, 2), end, number

    package_length = binary[start + 6]
    if package_length == "0":
        nr_bits = int(binary[start + 7 : start + 22], 2)
        numbers = []
        total = 0
        versions = 0
        initial_start = start + 22
        while total != nr_bits:
            version, end, number = decode_package(binary, initial_start)
            numbers.append(number)
            total += end - initial_start
            initial_start = end
            versions += version
        return versions + int(package_version, 2), end, combine_numbers(numbers, package_type)

    nr_packages = int(binary[start + 7 : start + 18], 2)
    current_package = 0
    versions = 0
    initial_start = start + 18
    numbers = []
    while current_package != nr_packages:
        version, end, number = decode_package(binary, initial_start)
        initial_start = end
        numbers.append(number)
        versions += version
        current_package += 1
    return versions + int(package_version, 2), end, combine_numbers(numbers, package_type)


with open("d16.txt") as f:
    binary = convert(f.readline().rstrip())

print(decode_package(binary, 0))
