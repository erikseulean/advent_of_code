from collections import defaultdict, Counter

edges = defaultdict(list)
paths = 0

with open("d12.txt") as f:
    for line in f:
        node1, node2 = line.rstrip().split("-")
        if node2 != "start":
            edges[node1].append(node2)
        if node1 != "start":
            edges[node2].append(node1)


def visit(node, path_so_far, max_reached):
    if node == "end":
        global paths
        paths = paths + 1
        return

    for next_node in edges[node]:
        if next_node.islower() and next_node in path_so_far and max_reached:
            continue
        path_so_far[next_node] += 1
        visit(next_node, path_so_far, max_reached or (next_node.islower() and path_so_far[next_node] == 2))
        path_so_far[next_node] -= 1
        if path_so_far[next_node] == 0:
            path_so_far.pop(next_node)


path_so_far = defaultdict(int)
visit("start", path_so_far, False)
print(paths)
