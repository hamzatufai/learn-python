## ============== Single Class Inheritance ================
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped.")


class Toyota(Car):
    def __init__(self, type, brand):
        super().__init__(type)
        self.brand = brand
        super().start()


# car1 = Toyota("Petrol" ,"Swift")
# print(car1.type)
# print(car1.brand)

## ============== Multi-level Class Inheritance ================
class Patient:
    def  __init__(self, p_name, p_id ):
        self.p_name = p_name
        self.p_id = p_id

class Reception(Patient):
    @staticmethod
    def Greet():
        print("Welcome in Aga Khan Hospital. ")

class Hospital(Reception):
    @staticmethod
    def promise():
        print("Your health is our duty.")

# h1 = Hospital("Hamza", "1234")
# print(h1.p_name)
# print(h1.Greet())
# print(h1.promise())


## ============== Multiple Class Inheritance ================
class A:
    @staticmethod
    def hello():
        print("Hello World")
    
class B(A):
    @staticmethod
    def greet():
        print("Welcome Everyone. ")

class C(B, A):
    @staticmethod
    def call():
        print("Good Bye. ")

# c1 = C()
# c1.hello()


class X:
    var1 = "Welcome to class A."

class Y:
    var2 = "Welcome to class B. "

class Z(X, Y):
    var3 = "Welcome to class C."


# c1 = Z()
# print(c1.var1)

        
class Company:
    def __init__(self, t_lab, t_fac):
        self.t_lab = t_lab
        self.t_fac = t_fac
        

class Department:
    @staticmethod
    def greet():
        print("Welcome ")

class Office(Department ,Company):
    @staticmethod
    def hello():
        print("Selection will be start tomorrow.")

# o1 = Office("400", "8")
# print(o1.t_fac)
# print(o1.t_lab)
# print(o1.greet())
        

## ============== Class Method ===============
class Person:
    name = "Anonymous"

    # def changeName(self, name):
        # Person.name = name
        # self.__class__.name = "Hamza Tufail"

    @classmethod 
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Hamza tufail")
print(p1.name)
print(Person.name)
               