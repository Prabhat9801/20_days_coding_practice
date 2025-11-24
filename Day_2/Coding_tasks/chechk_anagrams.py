def check_anagrams(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(s1) == sorted(s2)
answer = check_anagrams("lissten", "silent")  # Example usage
if answer==True:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")