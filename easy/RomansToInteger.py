def romanToInt(s):
    romans_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
    total = 0
    prev_value = 0

    for i in reversed(s):
        value = romans_dict[i]
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total

romans = "MCMXCIV"
print(romanToInt(romans))