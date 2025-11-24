# Sum of Even Fibonacci Numbers:
# Problem: Generate the Fibonacci sequence up to a certain limit (e.g., 1000), but only keep a running total of the numbers in that sequence that are even.

def sum_even_fibonacci(n):
    a = 0
    b = 1
    even_sum=0
    while a<=n:
        if a%2==0:
            even_sum=even_sum + a
        sum = a + b
        a = b
        b = sum
    return even_sum
result = sum_even_fibonacci(1000)
print("Sum of even Fibonacci numbers up to 1000 is:", result)