# This report indicates that, scanning outward from the submarine, the sonar sweep found
# depths of 199, 200, 208, 210, and so on.

# The first order of business is to figure out how quickly the depth increases, just so you
# know what you're dealing with - you never know if the keys will get carried into deeper
# water by an ocean current or a fish or something.

# To do this, count the number of times a depth measurement increases from the previous
# measurement.


current = None
count = 0

elem = []
with open("d1.txt") as f:
    current = int(f.readline().rstrip())
    for line in f:
        line = int(line.rstrip())
        elem.append(line)
        count += line > current
        current = line
print(count)


# Considering every single measurement isn't as useful as you expected: there's just too much
# noise in the data.

# Instead, consider sums of a three-measurement sliding window.

# Start by comparing the first and second three-measurement windows. The measurements in the
# first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second
# window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second
# window is larger than the sum of the first, so this first comparison increased.

# Your goal now is to count the number of times the sum of measurements in this sliding
# window increases from the previous sum. So, compare A with B, then compare B with C, then C
# with D, and so on. Stop when there aren't enough measurements left to create a new
# three-measurement sum.

count2 = sum((elem[index] - elem[index - 3] > 0) for index in range(3, len(elem)))
print(count2)
