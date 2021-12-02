# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth, 
# and so they have the opposite result of what you might expect.


# Your horizontal position and depth both start at 0. The steps above would then 
# modify them as follows:

# forward 5 adds 5 to your horizontal position, a total of 5.
# down 5 adds 5 to your depth, resulting in a value of 5.
# forward 8 adds 8 to your horizontal position, a total of 13.
# up 3 decreases your depth by 3, resulting in a value of 2.
# down 8 adds 8 to your depth, resulting in a value of 10.
# forward 2 adds 2 to your horizontal position, a total of 15.


# Q2

# Based on your calculations, the planned course doesn't seem to make any sense. 
# You find the submarine manual and discover that the process is actually slightly 
# more complicated.

# In addition to horizontal position and depth, you'll also need to track a third value,
# aim, which also starts at 0. The commands also mean something entirely different than 
# you first thought:

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

res = {
    "up": 0,
    "down": 0,
    "forward": 0
}

aim = 0
depth = 0
forward = 0

with open("d2.txt") as f:
    for line in f:
        instruction, number = line.split()
        number = int(number)
        
        res[instruction] = res[instruction] + number

        if instruction == "down":
            aim += number
        elif instruction == "up":
            aim -= number
        else:
            forward += number
            depth += aim * number

print((res["down"] - res["up"]) * res["forward"])
print(forward * depth)
