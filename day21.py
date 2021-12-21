from functools import cache
from itertools import product
p1 = 4
p2 = 8


def solve1():
    p1_score = 0
    p2_score = 0
    die = 1
    p1_next = True

    rounds = 0
    while p1_score < 1000 and p2_score < 1000:
        print(p1_score, p2_score)
        rounds += 3
        total = die + die + 1+ die + 2
        total = total if total <= 10 else total % 10
        die = die + 3
        if p1_next:
            p1 += total
            p1 = p1 if p1 <= 10 else p1 - 10
            p1_score += p1
        else:
            p2 += total
            p2 = p2 if p2 <= 10 else p2 - 10
            p2_score += p2

        p1_next = not p1_next


@cache
def solve(p1, p1_score, p2, p2_score, p1_turn):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    wins = (0, 0)
    for die_scores in product([1,2,3], repeat=3):
        total = sum(die_scores)
        if p1_turn:
            p1_new = p1 + total
            p1_new = p1_new if p1_new <= 10 else p1_new - 10
            p1_new_score = p1_score + p1_new
            w1 = solve(p1_new, p1_new_score, p2, p2_score, not p1_turn)
            wins = (w1[0] + wins[0], w1[1] + wins[1])
        else:
            p2_new = p2 + total
            p2_new = p2_new if p2_new <= 10 else p2_new - 10
            p2_new_score = p2_score + p2_new
            w1 = solve(p1, p1_score, p2_new, p2_new_score, not p1_turn)
            wins = (w1[0] + wins[0], w1[1] + wins[1])
    return wins

print(max(solve(10, 0, 1, 0, True)))