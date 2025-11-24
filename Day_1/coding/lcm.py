def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    
    return abs(a * b) // gcd(a, b)
result = lcm(4, 5)
print(result)