from .count_vowels import count_vowels
from .count_consonants import count_consonants
from .count_digit import count_digit
from .count_spaces import count_spaces
from .count_special_chars import count_special_chars

def count_all(s):
    vowels_count = count_vowels(s)
    consonants_count = count_consonants(s)
    digits_count = count_digit(s)
    spaces_count = count_spaces(s)
    special_chars_count = count_special_chars(s)
    
    print("String Analysis:")
    print(f"Vowels: {vowels_count}")
    print(f"Consonants: {consonants_count}")
    print(f"Digits: {digits_count}")
    print(f"Spaces: {spaces_count}")
    print(f"Special Characters: {special_chars_count}")


