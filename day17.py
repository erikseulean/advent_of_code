with open("d17.txt") as f:
    line = f.readline().rstrip().split(",")
    x = line[0].split()[-1].split("=")[1].split("..")
    x_min, x_max = int(x[0]), int(x[1])
    y = line[1].split()[-1].split("=")[1].split("..")
    y_min, y_max = int(y[0]), int(y[1])


def find_max(x, y, x_min, x_max, y_min, y_max):
    max_value = 0
    current_x = 0
    current_y = 0
    in_range = False
    while True:
        max_value = max(max_value, current_y)
        if current_x >= x_min and current_x <= x_max and current_y >= y_min and current_y <= y_max:
            in_range = True
        if current_x > x_max or current_y < y_min:
            break
        current_x += x
        current_y += y
        y -= 1
        if x == 0:
            continue
        x = (x + 1 if x < 0 else x - 1)

    return in_range

max_value = 0

for x in range(-500, 500):
    for y in range(-500, 500):
        if find_max(x, y, x_min, x_max, y_min, y_max):
            dist.add((x,y))
            max_value += 1
            print(x, y, max_value)