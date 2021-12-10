import operator

illegals = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

match = {")": "(", "]": "[", "}": "{", ">": "<"}

open_brackets = {"{", "(", "[", "<"}

scores = []
with open("d10.txt") as f:
    for line in f:
        s = 0
        stack = []
        incomplete = True
        for c in line.rstrip():
            if c in open_brackets:
                stack.append(c)
                continue
            last = stack.pop()
            if last != match[c]:
                s += illegals[c]
                incomplete = False
            break
        if incomplete:
            for c in stack[::-1]:
                s = s * 5 + score[c]
            scores.append(s)

print(sorted(scores)[len(scores) // 2])
