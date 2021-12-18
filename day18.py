import json

expressions = []
with open("d18.txt") as f:
    expressions = [json.loads(line.rstrip()) for line in f]


class Node:
    def __init__(self, value, parent, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


def construct_tree(expression, parent):

    if isinstance(expression, int):
        return expression

    p_next = Node("*", parent)
    p_next.left = construct_tree(expression[0], p_next)
    p_next.right = construct_tree(expression[1], p_next)

    return p_next


def increment_first_left(current, value, node):
    prev = node
    while current is not None and (current.left is None or current.left == prev):
        prev = current
        current = current.parent
    if current == None:
        return

    if not isinstance(current.left, int):
        current = current.left

        while not isinstance(current.right, int):
            current = current.right
        current.right += value
        return

    current.left += value


def increment_first_right(current, value, node):
    prev = node
    while current is not None and (current.right is None or current.right == prev):
        prev = current
        current = current.parent

    if current == None:
        return

    if not isinstance(current.right, int):
        current = current.right
        while not isinstance(current.left, int):
            current = current.left
        current.left += value
        return
    current.right += value


def explode(tree, depth):
    depth = 0
    stack = []
    has_changes = False
    while not isinstance(tree, int):
        stack.append((tree, depth))
        depth += 1
        tree = tree.left

    while stack:
        node, depth = stack.pop()
        if isinstance(node, int):
            continue

        if depth < 4:
            t = node.right
            depth = depth + 1
            while isinstance(t, Node):
                stack.append((t, depth))
                depth += 1
                t = t.left
            continue

        if isinstance(node.left, int) and isinstance(node.right, int):
            has_changes = True
            parent = node.parent
            left_value = node.left
            right_value = node.right
            increment_first_left(parent, left_value, node)
            increment_first_right(parent, right_value, node)

            if parent.right == node:
                parent.right = 0
            else:
                parent.left = 0


def split(tree, depth):
    has_changes = False
    if isinstance(tree, int):
        return has_changes
    if isinstance(tree.left, int) and tree.left > 9:
        left = int(tree.left / 2)
        right = tree.left - left
        tree.left = Node("*", tree, left, right)
        return True
    else:
        has_changes = has_changes or split(tree.left, depth + 1)
        if has_changes:
            return has_changes

    if isinstance(tree.right, int) and tree.right > 9:
        left = int(tree.right / 2)
        right = tree.right - left
        tree.right = Node("*", tree, left, right)
        return True

    return has_changes or split(tree.right, depth + 1)


def get_magnitude(tree):
    if isinstance(tree, int):
        return tree

    return 3 * get_magnitude(tree.left) + 2 * get_magnitude(tree.right)


def get_as_list(tree):
    if isinstance(tree, int):
        return tree

    return [get_as_list(tree.left), get_as_list(tree.right)]


def get_final_tree(tree):
    split_happened = True
    while split_happened:
        explode(tree, 0)
        has_changes = True
        split_happened = False
        while has_changes:
            has_changes = split(tree, 0)
            explode(tree, 0)
            split_happened = split_happened or has_changes
    return tree


def put_all_together(expressions):
    magnitudes = []
    for e1 in expressions:
        for e2 in expressions:
            if e1 == e2:
                continue
            magnitudes.append(get_magnitude(get_final_tree(construct_tree([e1, e2], None))))
            magnitudes.append(get_magnitude(get_final_tree(construct_tree([e2, e1], None))))

    print(max(magnitudes))


put_all_together(expressions)
