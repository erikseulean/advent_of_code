def calc_sum_q1(numbers, median):
    nr = [abs(number - median) for number in numbers]
    return sum(nr)

def calc_sum_q2(numbers, optim):
    nr = [abs(number - optim) * (abs(number - optim) + 1) // 2 for number in numbers]
    return sum(nr)

with open("d7.txt") as f:
    numbers = sorted([int(nr) for nr in f.readline().split(",")])
    print(calc_sum_q1(numbers, numbers[len(numbers)//2]))
    mean = round(sum(numbers)/len(numbers))
    print(calc_sum_q2(numbers, mean))
    print(calc_sum_q2(numbers, mean-1))