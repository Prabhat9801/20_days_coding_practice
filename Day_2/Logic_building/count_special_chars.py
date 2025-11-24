def count_special_chars(s):
    count = 0
    for char in s:
        if not (char.isalnum() or char.isspace()):
            count += 1
    return count