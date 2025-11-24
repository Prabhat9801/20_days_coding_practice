def count_digit(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count