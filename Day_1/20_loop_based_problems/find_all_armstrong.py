# Armstrong Numbers in a Range:
# Problem: Find and print all Armstrong numbers that fall between 1 and 500.
def is_armstrong(number):
    num_str = str(number)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum = sum + int(digit) ** num_len
    return sum == number

def find_armstrong_numbers(start, end):
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=' ')

find_armstrong_numbers(1, 500)