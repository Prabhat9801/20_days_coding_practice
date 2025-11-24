def check(string):
    if string == string[::-1]:
        return True
    else:
        return False
result = check("madaam")
if result == True:
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")
