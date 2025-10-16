def func():
    user_input = input("Enter something: ")
    vowels = user_input.lower()
    if (
        vowels.count("a") > 0
        or vowels.count("e") > 0
        or vowels.count("i") > 0
        or vowels.count("o") > 0
        or vowels.count("u") > 0
    ):
        print("Vowels exist in this input. ")
    else:
        print("Vowels does't exist. ")
func()


user_input = input("Enter something: ")
reversed_str = ""
for char in user_input:
    reversed_str = char + reversed_str
print(reversed_str)

# Check for Uppercase Letters:
found = False
user_input = input("Enter something: ")
for char in user_input:
    if char.isupper():
        found = True
        break
print(found)

# Count the Letter 'e':
input_str = input("Enter something: ")
count_e = input_str.count("e")
print(f"The letter 'e' appears {count_e} times.")


#  Alphanumeric Check:
user = input("Enter something: ")
if  user.isalnum():
    print("Valid. ")
    exit()
else:
    print("Invalid. ")


# Reverse and Uppercase:
user = input("Enter something: ")
reverse_str = user[::-1]
print(reverse_str)
reverse_str_upper = reverse_str.upper()
print(reverse_str_upper)

# ++++++ 0R ++++++++++:
user = input("Enter something: ")
for i in user:
    reverse_str = i + reverse_str

upper_reverse_str = reverse_str.upper()
print(upper_reverse_str)


# Find a Substring
user = input("Enter a sentence: ")
word_search = input("Enter a word to search in the sentence: ")
if user.find(word_search) != -1:
    print(f"Yes {word_search} is exist.")
else:
    print("Not found. ")

+++++++++++++++++++ 0R +++++++++++++++++++++++++++++


user = input("Enter a sentence: ")
word_search = input("Enter a word to search in the sentence: ")
if word_search in user:
    print(f"Yes {word_search} is exist. ")
else:
    print("Not found. ")


#  Replace a Word
user = input("Enter a sentence: ")
replace_word = input("Which word you wanna replace? ")
new_sentence = user.replace(replace_word, "user")
print(new_sentence)

# Check for Gmail Address
user = input("Enter you email: ")
if user.endswith("@gmail.com"):
    print("Valid Gmail. ")
else:
    print("Invalid Gmail. ")

# Capitalize Full Name
user = input("Enter full name: ")
title = user.title()
print(title)    

# Validate Digits Only
user = input("Enter full name: ")
check = user.isdigit()
print(check)