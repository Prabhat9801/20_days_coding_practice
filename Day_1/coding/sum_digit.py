def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
    

result = sum(5)
print(result)  # Output: 15