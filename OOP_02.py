## ======= del Keyword ==========:
class Student:
    def __init__(self, name):
        self.name = name


# s1 = Student("Hamza")
# print(s1.name)
# del s1.name
# print(s1.name)

## Private Attribute and Method:  
class Student:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset(self):
        print(self.__acc_pass)

    
# s1 = Student("1234", "hamz123")
# print(s1.acc_no)
# print(s1.reset())

    
## +++++++++++++++++++++++++++
class Person:
    __name = "Anonymous"

    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()
        return self.__name

p1 = Person()
print(p1.welcome())
print(p1._Person__name)



        