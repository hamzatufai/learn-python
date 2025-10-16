# 🧾 Python Dictionary Practice – My Learning Log (30 June 2025)

# Today I focused on mastering Python dictionaries.
# I worked with key-value pairs, performed updates, deletions,
#  nested dictionaries, dictionary comprehensions,
#  and explored useful methods like `.pop()`, `.popitem()`,
#  `.copy()`, and `dict.fromkeys()`.


## ✅ Creating & Accessing Dictionaries


# chai_types = {
#     "Masala": "spicy",
#     "Ginger": "Zesty",
#     "Green": "Fresh",
#     "Gree": "Fresh"
# }


# print(chai_types["Ginger"])
# chai_types.pop("Gree")   # remove key and value
# print(chai_types.popitem())  # remove last key and value
# print(chai_types)


# Accessing keys and values
# for chai in chai_types:
#     print(chai)

# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, value in chai_types.items():
#     print(key, value)


# ✅ Checking Key Existence
# if "Ginger" in chai_types:
#     print("Yes I have Ginger chai")  # Output: Yes I have Ginger chai

# ✅ Length of Dictionary
# print(len(chai_types))  # Output: 4

# ✅ Updating Values and Removing Keys
# chai_types["Gree"] = "Black"
# chai_types.pop("Gree")        # Removes 'Gree'
# chai_types.popitem()          # Removes last key-value pair
# del chai_types["Ginger"]      # Deletes key 'Ginger'


# ✅ Copying a Dictionary
# chai_types_copy = chai_types.copy()
# chai_types_copy ["Gree"] = "Bad"
# print(chai_types_copy)
# print(chai_types.copy())

# ✅ Nested Dictionary
# tea_shop = {
#     "chai": {"Masala": "Spicy", "Green": "Mild"},
#     "tea": {"Balck": "Strong", "Ginger": "Zesty"}
# }

# print(tea_shop["chai"])            # {'Masala': 'Spicy', 'Green': 'Mild'}
# print(tea_shop["chai"]["Masala"])   # Spicy


# ✅ Dictionary Comprehension
# squared_num = {x: x**2 for x in range(5)}
# print(squared_num)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# squared_num.clear()
# print(squared_num)  # {}


# ✅ Creating Dictionary with Default Values
# keys = ["Masala", "Ginger", "Lemon"]
# default_value = "Delicious"

# new_dict = dict.fromkeys(keys, default_value)
# print(new_dict)  # {'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}

# new_dict = dict.fromkeys(keys, keys) # {'Masala': ['Masala', 'Ginger', 'Lemon'], ...}
# print(new_dict)


## ++++++++++++++++++++++++++++++++++++++++++++
# students = {
#     "Ali": {"Math": 78, "Physics": 85, "English": 67},
#     "Sara": {"Math": 92, "Physics": 88, "English": 81},
#     "Hamza": {"Math": 56, "Physics": 62, "English": 70},
#     "Ahmed": {"Math": 45, "Physics": 50, "English": 39},
# }
# average = {}
# for name, subjects in students.items():
#     avg = sum(subjects.values()) / len(subjects)
#     average[name] = round(avg, 2)

#     print(f"{name} with average {avg:.2f}")
# print("Student who got avgerage > 60: ")
# for name, avg in average.items():
#     if avg > 60:
#         print("Student: ", name)

## +++++++++++++++++++++++++++++++++++++++++++++++++++
# employees = {
#     "Ali": {"Jan": 1200, "Feb": 1500, "Mar": 1000},
#     "Sara": {"Jan": 2500, "Feb": 2200, "Mar": 3000},
#     "Hamza": {"Jan": 1800, "Feb": 1600, "Mar": 1700},
#     "Ahmed": {"Jan": 800, "Feb": 950, "Mar": 1100},
# }
# sales = {}
# for name, sale in employees.items():
#     total_sale = sum(sale.values())
#     print(f"{name}: Total sale: {total_sale}")
#     sales[name] = round(total_sale, 2)

# topper = max(sales, key=sales.get)
# print(f"Highest sale: {topper} with {sales[topper]}")

# total = {name: sale for name, sale in sales.items() if sale > 4000}
# print("Customer bought > 4000 stuff:")
# for name, cost in total.items():
#     print(f"{name}: {cost}")

## +++++++++++++++++++++++++++++++++++++++++++++
# products = {
#     "Laptop": 120000,
#     "Mobile": 60000,
#     "Headphones": 5000,
#     "Keyboard": 3500,
#     "Monitor": 25000,
#     "Mouse": 2000,
# }

# sort_product = sorted(products.items(), key=lambda x: x[1], reverse=True)
# print(sort_product)

# above_5000 = {name:price for name, price in products.items() if price > 5000}
# print("Above 5000:",above_5000)

# most_expensive = max(products, key=products.get)
# print(f"Expensive product: {most_expensive} -> {products[most_expensive]}")

## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# students = [
#     {"name": "Ali", "marks": {"Math": 70, "English": 65, "Science": 80}},
#     {"name": "Sara", "marks": {"Math": 85, "English": 95, "Science": 90}},
#     {"name": "Hamza", "marks": {"Math": 40, "English": 55, "Science": 60}},
#     {"name": "Ahmed", "marks": {"Math": 75, "English": 50, "Science": 45}},
# ]

# avg_marks = {}
# m_total = 0
# e_total = 0
# s_total = 0
# for detail in students:
#     sub_marks = detail["marks"]

#     total_math = sub_marks["Math"]
#     total_eng = sub_marks["English"]
#     total_sci = sub_marks["Science"]

#     m_total += total_math
#     e_total += total_eng
#     s_total += total_sci

#     average = round(sum(sub_marks.values()) / len(sub_marks), 2)
#     name = detail["name"]
#     avg_marks[name] = average

# print("Name and marks:", avg_marks)
# above_60 = {name: avg for name, avg in avg_marks.items() if avg >= 60}
# print("Above 60: ", above_60)
# max_avg = max(avg_marks, key=avg_marks.get)
# print("\nMax avg:")
# print(f"{max_avg} with average {avg_marks[max_avg]}")

# count = len(students)

# print("\nSubject-wise Class Average:")
# avg_dict = {
#     "Math": round(m_total / count, 2),
#     "English": round(e_total / count, 2),
#     "Science": round(s_total / count, 2),
# }
# print(avg_dict)


