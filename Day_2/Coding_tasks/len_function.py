def length(s):
    count = 0
    for char in s:
        count += 1
    return count

s = "Hello, World!"
print("Length of the string is:", length(s))