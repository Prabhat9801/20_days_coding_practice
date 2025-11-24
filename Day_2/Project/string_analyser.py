import sys
import os

# Add the Day_2 directory to the Python path
day_2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, day_2_path)

from Logic_building.count import count_all

print("Welcome to String Analyser")
s = input("Please Enter the String: ")
print("1. Analye the String: ")
print("2. Reverse String: ")

print("3. Find Substring: ")
print("4. To Exit")
user = int(input("Choose the option to analyse the string: "))

if user == 1:
    count_all(s)
   
elif user == 2:
    reversed_string = s[::-1]
    print("Reversed String:", reversed_string)
elif user == 3:
    substring = input("Enter the substring to find: ")
    count = s.count(substring)
    print(f"The substring '{substring}' appears {count} times in the string.")
elif user == 4:
    print("Exiting the program.")
    os._exit(0)
    