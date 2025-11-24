vowels = {'a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U'}
def count_vowels(string):
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
result = count_vowels("Hello World")
print(result)