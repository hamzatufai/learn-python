# def positive_only(func):
#     def wrapper(*args):
#         check_ispositive = all(arg > 0 for arg in args)
#         if check_ispositive == True:
#             return func(*args)
#         else:
#             print("Error: Only positive numbers are allowed. ")

#     return wrapper

# @positive_only
# def is_positive(a, b):
#     return a * b

# print(is_positive(2, 4))
# print(is_positive(0, 4))
# print(is_positive(3, -4))


## +++++++++++++++++++++++++++++++
# def limit_range(func):
#     def wrapper(*args):
#         check_range = all(isinstance(arg, int) and 1 <= arg <= 100 for arg in args)
#         if check_range == True:
#             return func(*args)
#         else:
#             print(f"Erro:{func.__name__} Number should be integer and must between 1 to 100. ")
#     return wrapper

# @limit_range
# def check_limit(*num):
#     return sum(num)
# print(check_limit(1,11))
# print(check_limit(0,9))
# print(check_limit("hello", 89))

## +++++++++++++++++++++++++++++++++++++
# def censor_bad_words(func):
#     def wrapper(*args):
#         bad_words = ["fool", "idiot", "fuck", "bloody fool", "go to hell", "crazy"]
#         sentence = args[0]

#         for word in bad_words:
#             sentence = sentence.replace(word, "***")

#         return func(sentence)
#     return wrapper


# @censor_bad_words
# def speak(sentence):
#     return sentence

# n = input("Enter your abuses sentence: ").lower()
# print(speak(n))

## +++++++++++++++++++++++++++++++

# def check_palindrome(func):
#     def wrapper(*args):
#         sentence = args[0]
#         cleaned = "".join(char.lower() for char in sentence if char.isalnum())
#         if cleaned == cleaned[::-1]:
#             print("It's a Palindrome. ")

#         else:
#             print("It's not a palindrome. ")

#         return func(*args)

#     return wrapper

# @check_palindrome
# def say(sentence):
#     return sentence

# n = input("Enter sentence(palindrome): ").lower()
# print(say(n))

## +++++++++++++++++++++++++++++++++++


def count_vowels(func):
    def wrapper(*args):

        sentence = args[0]
        vowel = "aeiouAEIOU"
        count = sum(1 for char in sentence if char in vowel)
        print(f"{sentence}: {count} time vowels appreas in sentence.")

        for alpha in vowel:
            sentence = sentence.replace(alpha, "*")
        print(f"Update sentence: {sentence}")

        cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
        if cleaned == cleaned[::-1]:
            print("Its a palindrome. ")
        else:
            print("Its not a plaindrome. ")

        return func(*args)

    return wrapper


@count_vowels
def vowels(sentence):
    return sentence


n = input("Enter any random sentence: ").lower()
print(vowels(n))
