with open("d9.txt") as f:
    lines = [line.strip() for line in f.readlines()]

def move_tail(H, T):

    if abs(H[0] - T[0]) < 2 and abs(H[1] - T[1]) < 2:
        return T

    if abs(H[0] - T[0]) >= 2 and abs(H[1] - T[1]) >= 2: 
        return (
        H[0] - 1 if T[0] < H[0] else H[0] + 1,
        H[1] - 1 if T[1] < H[1] else H[1] + 1
    )

    if abs(H[1] - T[1]) >= 2:
        return (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
        
    if abs(H[0] - T[0]) >= 2:
        return (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])

def move_up(H):
    return (H[0] - 1, H[1])

def move_down(H):
    return (H[0] + 1, H[1])

def move_left(H):
    return (H[0], H[1] - 1)

def move_right(H):
    return (H[0], H[1] + 1)

movements = {
    "U": move_up,
    "D": move_down,
    "L": move_left,
    "R": move_right,
}
        
def find_locations(lines):

    positions = set([(0, 0)])
    positions2 = set([(0, 0)])
    H = (0, 0)
    T = [(0, 0) for _ in range(9)]


    for line in lines:
        where, steps = line.split()
        steps = int(steps)

        for _ in range(steps):
            H = movements[where](H)
            T[0] = move_tail(H, T[0])
            
            for rope_index in range(1, 9):
                T[rope_index] = move_tail(T[rope_index - 1], T[rope_index])
            
            positions.add(T[0])
            positions2.add(T[-1])
        
    return len(positions2)


print(find_locations(lines))