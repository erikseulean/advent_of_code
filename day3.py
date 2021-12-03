from collections import Counter
from collections import defaultdict

ones = defaultdict(int)
numbers = []

with open("d3.txt") as f:
    
    for line in f:
        line = line.rstrip()
        numbers.append(line)
        for i in range(len(line)):
            ones[11 - i] += int(line[i])
    
gamma = 0
epsilon = 0

for index in range(12):
    bit = ones[index] >= 500
    gamma += 2 ** (index) * bit
    epsilon += 2 ** (index) * (not bit)

print(gamma * epsilon)

def find_number(numbers, inverse = False):
    
    for index in range(12):
        counts = Counter(number[index] for number in numbers)
        bit = int(counts.most_common()[0][0]) if not inverse else not int(counts.most_common()[0][0])
        if counts["0"] == counts["1"]:
            bit = 1 if not inverse else 0
        numbers = [number for number in numbers if int(number[index]) == bit]
        if len(numbers) == 1:
            return int(numbers[0], 2)


oxygen = find_number(numbers)
co2 = find_number(numbers, True)

print(oxygen * co2)
