def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def print_fibonacci(n):
    a = 0
    b = 1
    for i in range(n+1):
        print(a, end=' ')
        sum = a + b
        a = b
        b = sum
    print("\n---")
result = fibonacci(6)
series = print_fibonacci(6)
print(result)