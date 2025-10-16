# Basic Function Syntax

def square (number):
    print(number ** 2)
    return number ** 2


square(4)
result = square(7)
print(result)
print(square(7))


# function take two num in parameters and return Sum of two number


def sum(num1, num2):
    return num1 + num2

print(sum(10, 8))

# Function Multiply two numbers but can also accept string


def Multi(m1, m2):
    return m1 * m2

print(Multi(8, 9))
print(Multi('a', 9))
print(Multi(8, 'a'))


# Function return multiple values

import math
def circle(radius):
    area = math.pi * radius**2
    area1 = math.floor(area * 100) / 100
    circumference = 2 * math.pi * radius
    circumference1 = math.floor(circumference * 100) / 100
    return area1, circumference1

a, c = circle(8)
print(f"Area of circle : {a}\n Circumference of circle: {c}")

# Default Parameter Value

def str1(name = "Hamza"):
    return "preve'et " + "menya " + "zauv'ot " + name
# print(str1("Hamza"))
print(str1())


# Create a lamda fucntion to compute the cube of a number
def cube(a):
    return a ** 3
print(cube(4))

cube = lambda x : x ** 3
print(cube(3))

# Check is prime b/w 1000

nums = range(1, 1000)
def is_prime(num):
    for x in range(2, num):
        if (num % x) == 0:
            return False
    return True
primes = list(filter(is_prime, nums))
print(primes)


# Function with *arg

def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))


# Function **kwargs

def print_kwarge(**kwargs):
    # print(f"Name: {name}, Goal: {goal}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_kwarge(name="Hamza", goal="Buisnessman")
print_kwarge(name="Hamza")
print_kwarge(name="Hamza", goal="Buisnessman", enemy = "Dr jhon")

##we can flip orders if we accept perameters

# Generator Function with a Yield

def is_prime (limit):
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

for num in is_prime(1000):
    print(num, end=' ')


def generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

# Now print each yielded number
for i in generator(10):
    print(i)


# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# fabonachi
num = int(input("Enter number: ").strip())
def fabonachi(num):
    if num == 0:
        return num
    elif num == 1:
        return 1
    else:
        return fabonachi(num - 1) + fabonachi(num - 2)

for i in range(num):
    print(fabonachi(i), end=" ")

my_list = ["apple", "banana", "cherry"]
for index, item in enumerate(my_list):
    print(f"Index: {index}, Item: {item}")


l1 = [12, 13, 14, 15, 16, 17]
list_even = list(filter(lambda x: x % 2 == 0, l1))
# print(list_even)

from functools import reduce

l1 = [2, 4, 5, 64, 4, 78, 90]
new_list = list(filter(lambda x: (x % 3 == 0), l1))
my_list = list(map(lambda x: (x % 3 == 0), l1))

other_list = reduce(lambda x, y: x +(y if y % 2 == 0 else 0), l1, 0)
my_other_new_list = all(e % 2 == 0 for e in l1)
print(my_other_new_list)
