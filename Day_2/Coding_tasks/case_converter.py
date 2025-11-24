def case_converter(s):
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for char in s:
        if char in lowercase:
            index = lowercase.index(char)
            result += uppercase[index]
        elif char in uppercase:
            index = uppercase.index(char)
            result += lowercase[index]
        else:
            result += char
    return result
s = "Hello World!"
converted = case_converter(s)
print("Converted string:", converted)