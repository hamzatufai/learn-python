text = "  Hello Hamza123! Welcome to Python.  "

# Convert to lowercase
print(text.lower())  # hello hamza123! welcome to python.

# Convert to uppercase
print(text.upper())  # HELLO HAMZA123! WELCOME TO PYTHON.

# Remove spaces from both sides
print(text.strip())  # "Hello Hamza123! Welcome to Python."

# Remove from left side only
print(text.lstrip())  # "Hello Hamza123! Welcome to Python.  "

# Remove from right side only
print(text.rstrip())  # "  Hello Hamza123! Welcome to Python."

# Replace a word or character
print(text.replace("Hamza123", "User"))  # "  Hello User! Welcome to Python.  "

# Split string into list (default by space)
print(text.split())  # ['Hello', 'Hamza123!', 'Welcome', 'to', 'Python.']

# Split string using custom separator
print("name,email,phone".split(","))  # ['name', 'email', 'phone']

# Join list items into a string
print("-".join(["2025", "07", "08"]))  # 2025-07-08

# Find index of first occurrence
print(text.find("Hamza"))  # 8

# Count how many times something appears
print(text.count("o"))  # 4

# Check if string starts with something
print(text.strip().startswith("Hello"))  # True

# Check if string ends with something
print(text.strip().endswith("Python."))  # True

# Check if all characters are digits
print("12345".isdigit())  # True

# Check if all characters are letters
print("Hamza".isalpha())  # True

# Check if all characters are alphanumeric
print("Hamza123".isalnum())  # True

# Check if all characters are lowercase
print("hello".islower())  # True

# Check if all characters are uppercase
print("HELLO".isupper())  # True

# Capitalize first letter only
print("hello world".capitalize())  # "Hello world"

# Title case (first letter of each word)
print("hello world".title())  # "Hello World"

# Check if string is only whitespace
print("   ".isspace())  # True

# Center text with padding
print("Hamza".center(20, "-"))  # -------Hamza--------

# Check if string is valid identifier (for variables)
print("user_name".isidentifier())  # True

# Swap upper and lower case
print("Hamza123".swapcase())  # hAMZA123
