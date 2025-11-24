def count_spaces(s):
    count = 0
    for char in s:
        if char == ' ':
            count += 1
    return count