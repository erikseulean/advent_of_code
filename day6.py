from collections import defaultdict

q = defaultdict(int)
with open("d6.txt") as f:
    for nr in f.readline().split(","):
        q[int(nr)] += 1

for _ in range(256):
    next_day_q = defaultdict(int)
    for fish, fish_count in q.items():
        if fish == 0:
            next_day_q[6] += fish_count
            next_day_q[8] += fish_count
        else:
            next_day_q[fish - 1] += fish_count
    q = next_day_q

print((sum(q.values())))
