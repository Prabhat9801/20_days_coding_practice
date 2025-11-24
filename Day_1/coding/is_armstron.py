def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum = sum+int(digit) ** num_len
    return sum == number
number = 1643
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")