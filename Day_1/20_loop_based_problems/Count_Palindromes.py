def count_palindromes(start , end):
    count = 0
    for number in range(start, end + 1):
        str_num = str(number)
        if str_num == str_num[::-1]:
            print(str_num, end=' ')
            count += 1
            
            
    return count
result = count_palindromes(1, 1000)
print("\nTotal palindromes:", end=' ')
print(result)
