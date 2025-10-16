# ## ************ Class ****************
# class Student:
#     # name = "Hamza"
#     collage_name = "ABC Collage"
#     # name = "Anonymous"  # class attr < obj attr precedence

#     # Default constructor
#     def __init__(self):
#         print("Adding new student in database..")

#     # Parametrized constructor
#     def __init__(self, name, marks):

#         # global name
#         # print(f"adding new student '{self.name}' in database..")

#         self.name = name
#         self.marks = marks
#         print("Adding new student in database..")


# s1 = Student("Hamza Tufail", 90)
# print(s1.name, s1.marks)

# s2 = Student("Taha Tufail", 89)
# print(s2.name, s2.marks),
# print(Student.collage_name)

# class Car:
#     color = "Blue"
#     model = "Audi"
#     def __init__(self):
#         # print(self)
#         print("Welcome! we have new brand in this year.")

# # c1 = Car()
# # print(c1.color)
# # print(c1.model)

## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class student:
#     collage_name = "ABC collage"

#     def __init__(self, name, lastname, marks):

#         self.name = name
#         self.lastname = lastname
#         self.marks = marks

#         print("Adding new student in DataBase..")

#     def welcome(self):
#             print("Welcome Student: ", self.name )

#     def get_marks(self):
#          return self.marks

# s1 =  student('Hamza', 'Tufail', 90)
# s1.welcome()
# print(s1.get_marks())


## =========================== Question ======================================
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello World")

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val

#         print("Hi", self.name, "your avg score is: ", sum / 3)

# s1 = student("Hamza", [78, 89, 90])
# s1.avg_marks()
# s1.name = "jhon clark"
# s1.avg_marks()

# s1.hello()

## +++++++++++++++++++++++++++++++++++++++++

# class Account:
#     def __init__(self, balane, acc_no):
#         self.balance = balane
#         self.acc_no = acc_no

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited.")
#         print("Total Amount: ", self.get_amount())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited.")
#         print("Total Amount: ", self.get_amount())

#     def get_amount(self):
#         return self.balance

# acc1 = Account(4500, "acc-01")
# acc1.debit(500)
# acc1.credit(1000)

## ======================= Abstraction ===========================

class Car:
    def __init__(self):
        
        self.acc = False
        self.fuel = False
        self.battery_charge = False
        self.brk = False

    def start(self):
        self.acc = True
        self.fuel = True
        self.battery_charge = True
        self.brk = True

        print("Car is Starting..")
        print("Fuel is level up.")
        print("Battery has been charged.")
        print("hang the hand break down side.")


c1 = Car()
c1.start()




