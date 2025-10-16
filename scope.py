# ------------------------------------------
# 🔹 Global vs Local Scope
# ------------------------------------------
username = "Hamza"


def func():
    # username = "chai"  # Uncomment this to make it local
    print("Inside func:", username)  # Uses global variable if local isn't declared


print("Global username:", username)
func()  # Output: Hamza


# ------------------------------------------
# 🔹 Decorator with Tuple Return
# ------------------------------------------
def pack(f):
    def wrap(x):
        return (f(x), x)  # Returns both output and input

    return wrap


@pack
def square(x):
    return x**2


print("Decorator test - input:", square(3)[1])  # Output: 3


# ------------------------------------------
# 🔹 Global Variable Access & Shadowing
# ------------------------------------------
x = 99


def func2(y):
    z = x + y  # Uses global x = 99
    return z


result = func2(1)
print("Global access:", result)  # Output: 100


# ------------------------------------------
# 🔹 Global Overwriting (Avoid unless needed)
# ------------------------------------------
def func3():
    global x  # Warning: Modifies global variable!
    x = 88


func3()
print("Global after overwrite:", x)  # Output: 88


# ------------------------------------------
# 🔹 Nested Function Accessing Outer Variable
# ------------------------------------------
def f1():
    # x = 88  # Uncomment to make local
    def f2():
        print("Nested access:", x)  # Uses outer/global x

    f2()


f1()  # Output depends on where x is defined


# ------------------------------------------
# 🔹 Closure: Function Returning Function
# ------------------------------------------
def chaicoder(num):
    def actual(x):
        return x**num  # Uses outer variable `num` even after outer function is done

    return actual


f = chaicoder(2)  # Squares: x^2
g = chaicoder(3)  # Cubes: x^3

print("Square of 3:", f(3))  # Output: 9
print("Cube of 3:", g(3))  # Output: 27
