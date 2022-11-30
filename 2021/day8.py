unique = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

all_letters = set(["a", "b", "c", "d", "e", "f", "g"])
correct = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def find_a(one, seven):
    letters_map["a"] = seven.difference(one).pop()
    letters_map_reverse[letters_map["a"]] = "a"


def find_e_and_g(one, four, seven, eight):
    common = set(one)
    common.update(four)
    common.update(seven)

    return eight.difference(common)


def define_e_and_g(e_and_g, eight, unknown_digits):

    for digit in unknown_digits:
        if len(digit) != 6:
            continue
        diff = list(set(eight).difference(digit))
        if diff[0] not in e_and_g:
            continue

        e = diff[0]
        e_and_g.remove(e)
        g = e_and_g.pop()

        letters_map["g"] = g
        letters_map_reverse[g] = "g"
        letters_map["e"] = e
        letters_map_reverse[e] = "e"
        return


def define_c(one, unknown_digits):
    one = set(one)
    for digit in unknown_digits:
        if len(digit) != 6:
            continue
        if len((diff := one.difference(digit))) == 1:
            c = diff.pop()
            letters_map["c"] = c
            letters_map_reverse[c] = "c"
            return


def define_f(seven):
    letters_map["f"] = seven.difference(letters_map_reverse.keys()).pop()
    letters_map_reverse[letters_map["f"]] = "f"


def define_b_and_d(unknown_digits):
    known = set(letters_map.values())

    for digit in unknown_digits:
        if len(digit) != 5:
            continue
        if len((diff := digit.difference(known))) == 1:
            d = diff.pop()
            letters_map["d"] = d
            letters_map_reverse[d] = "d"
            break

    missing = all_letters.difference(set(letters_map.keys()))
    missing = missing.pop()
    missing_wrong = all_letters.difference(set(letters_map_reverse.keys()))
    missing_wrong = missing_wrong.pop()
    letters_map[missing] = missing_wrong
    letters_map_reverse[missing_wrong] = missing


def decode(wrong):
    l = []
    for letter in wrong:
        l.append(letters_map_reverse[letter])

    return correct["".join(sorted(l))]


count = 0
s = 0
with open("d8.txt") as f:
    for line in f:
        unknown_digits = []
        digit_to_code = {}

        letters_map = {}
        letters_map_reverse = {}

        digits = line.split("|")
        result = digits[1].split()
        digits = digits[0].split()
        for digit in digits:
            if len(digit) in unique:
                digit_to_code[unique[len(digit)]] = digit
            else:
                unknown_digits.append(set(digit))
            count += 1

        find_a(set(digit_to_code[1]), set(digit_to_code[7]))
        e_g = find_e_and_g(digit_to_code[1], digit_to_code[4], digit_to_code[7], set(digit_to_code[8]))
        define_e_and_g(e_g, digit_to_code[8], unknown_digits)
        define_c(digit_to_code[1], unknown_digits)
        define_f(set(digit_to_code[7]))
        define_b_and_d(unknown_digits)

        nr = 0
        for i in range(4):
            nr += 10 ** (3 - i) * decode(result[i])
        s += nr
print(count)
print(s)
