def find_max_num(numbers):
    max = 0
    for x in numbers:
        if x > max:
            max = x
    return max
