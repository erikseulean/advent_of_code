from collections import Counter
from collections import defaultdict

transitions = {}
initial = defaultdict(int)
with open("d14.txt") as f:
    line = f.readline().rstrip()
    for i in range(len(line) - 1):
        initial[line[i : i + 2]] += 1
    f.readline()
    for line in f:
        what, where = line.strip().split(" -> ")
        transitions[what] = where


for iteration in range(40):
    chain = defaultdict(int)
    for pair in initial:
        transition = transitions[pair]
        chain[pair[0] + transition] += initial[pair]
        chain[transition + pair[1]] += initial[pair]
    initial = chain

first = defaultdict(int)
second = defaultdict(int)
for pair in initial:
    first[pair[0]] += initial[pair]
    second[pair[1]] += initial[pair]

maxval = max(max(first[letter], second[letter]) for letter in first.keys())
minval = min(max(first[letter], second[letter]) for letter in first.keys())

print(maxval - minval)
