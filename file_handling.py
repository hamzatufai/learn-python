# import csv

# high_temp = float('-inf')
# low_temp = float('inf')
# days_count = 0
# total_temp = 0
# high_temp_day =""
# low_temp_day = ""

# with open('temperature.csv', 'r') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         temperature = float(row['Temperature'])
#         day = row['Day']
#         if temperature > high_temp:
#             high_temp = temperature
#             high_temp_day = day

#         if temperature < low_temp:
#             low_temp = temperature
#             low_temp_day = day

#         total_temp += temperature
#         days_count += 1

# avg_temp = total_temp / days_count

# print(f"Lowest Temperature: {low_temp:.2f} on '{low_temp_day}'")
# print(f"Highest Temerature: {high_temp:.2f} on '{high_temp_day}'")
# print(f"Average Temperature: {avg_temp:.2f}*C")

# ## +++++++++++++++++++++++++++++++++++++++++++
# with open("student.csv", "w") as f:
#     f.write("name,age,marks\n")
#     f.write("Hamza,20,85\n")
#     f.write("Ali,21,72\n")
#     f.write("Sara,22,90\n")
#     f.write("Ahmed,20,65\n")
#     f.write("Ayesha,21,95\n")

# with open("student.csv", "r") as f:
#     lines = f.readlines()
# students = []
# for line in lines[1:]:
#     name, age, marks = line.strip().split(",")
#     students.append((name, int(age), int(marks)))

# total_marks = sum(marks for _, _, marks in students)
# avg = total_marks / len(students)
# print(f"Average: {avg}")

# print("\nStudent marks > 85:")
# for name, age, marks in students:
#     if marks > 85:
#         print(f"{name} ({age} years) - {marks}")

# # +++++++++++++++++++++++++++++++++++++++++++++++++++++
# students = [(1, "Ali", 99), (2, "Hamza", 85), (3, "Sara", 92), (4, "Usman", 67)]


# highest_marks = students[0]
# for roll, name, marks in students:
#     if marks > highest_marks[2]:
#         highest_marks = (roll, name, marks)
# print(f"{highest_marks[1]} got {highest_marks[2]}")

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# students = [("Ali", 18, 75), ("Sara", 19, 82), ("Omar", 20, 67), ("Hina", 18, 90)]
# average_marks = sum(marks for _, _, marks in students) / len(students)
# average_age = sum(age for _, age, _ in students) / len(students)
# highest_marks = students[0]
# highest_marks = max(students, key=lambda x: x[2])
# lowest_marks = min(students, key=lambda x: x[2])


# print("---- Result -----")
# print(f"Average Marks: {average_marks}")
# print(f"Average Age: {average_age}")
# print(f"Highest Marks: {highest_marks[0]} got {highest_marks[2]}")
# print(f"Lowest Marks: {lowest_marks[0]} got {lowest_marks[2]}")


# # +++++++++++++++++++++++++++++++++++++++++
# def prime(num):
#     if num <= 1:
#         is_prime = False
#     else:
#         is_prime = True
#         for m in range(2, num):
#             if num % m == 0:
#                 is_prime = False
#                 break

#     print(f"{num} is prime? {is_prime}")


# prime(13)


# # ++++++++++++++++++++++++++++++++++++++++++
# def second_largest_number():
#     numbers = []
#     user_count = int(input("Enter number range to add in list: "))
#     for i in range(user_count):
#         user_input = int(input(f"Enter number {i + 1}: "))
#         numbers.append(user_input)

#     # numbers.sort(reverse=True)
#     # second_largest = numbers[1]
#     numbers.sort()
#     second_largest = numbers[-2]

#     print(f"Second largest number: {second_largest}")


# second_largest_number()


# # +++++++++++++++++++++++++++++++++++++++++++++
# def word_frequency(text):
#     break_sentence = text.split()
#     freq = {}
#     for word in break_sentence:
#         freq[word] = freq.get(word, 0) + 1
#     print(freq)


# word_frequency("hello its me hamza hamza ")


# # +++++++++++++++++++++++++++++++++++++++
# def number_reverse(num):
#     reverse_num = 0
#     while num > 0:
#         digit = num % 10
#         reverse_num = reverse_num * 10 + digit
#         num //= 10
#     print(reverse_num)


# number_reverse("1234")


# # +++++++++++++++++++++++++++++++++++++++++++++
# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)


# print(factorial(5))

## ++++++++++++++++++++++++++++++++++++++++++
# import ast

# def call():
#     with open("analyzer.txt", "r") as f:
#         # line = f.read()
#         line = f.read().strip()
#         numbers = ast.literal_eval(line)

#     print(numbers, type(numbers))

# numbers = [int(n.strip()) for n in line.split(",")]

#     total = sum(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)
#     avg = total / len(numbers)
#     print("Total: ", total, "Max: \n", maximum, "Min: \n", minimum, "Avg: \n", avg)
# call()

## ++++++++++++++++++++++++++++++++++++++++++++
# def load_data():
#     data = "23, 67, 89, 823,151, 672, 8762, 562, 78"
#     with open("analyzer.txt", "w") as f:
#         f.write(data)

# def read_data():
#     with open("analyzer.txt", 'r') as f:
#         line = f.read()

#     numbers = [int(n.strip()) for n in line.split(",")]
#     return numbers

# def calculate(numbers):
#     total = sum(numbers)
#     avg = total / len(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)
#     return total, avg, minimum, maximum

# def sort_data(numbers):
#     return sorted(numbers)

# def filter_data(numbers, threshold):
#     return [n for n in numbers if n > threshold]

# def generate_report(numbers):
#     total, avg, minimum, maximum = calculate(numbers)
#     with open('generate.txt', 'w') as f:
#         f.write("----- Generated Report ------\n")
#         f.write(f"Numbers: {numbers}\n")
#         f.write(f"Total: {total}\n")
#         f.write(f"Average: {avg:.2f}\n")
#         f.write(f"Minimum: {minimum}\n")
#         f.write(f"Maximum: {maximum}\n")
#         f.write("Generated Report: generate.txt")

# def main():
#     while True:
#         print("\n----- Mini Data Analyzer -----")
#         print("1. Load data ")
#         print("2. Read and show Data")
#         print("3. Sort Data")
#         print("4. Filter Data >100")
#         print("5. Generate report")
#         print("6. Exit")

#         choose_option = input("Enter an option: ").strip()
#         if choose_option == "1":
#             load_data()
#             print("Data loaded to file. ")

#         elif choose_option == "2":
#             numbers = read_data()
#             total, avg, maximum, minimum = calculate(numbers)
#             print(f"Numbers: {numbers}")
#             print(f"Total: {total}, Average: {avg:.2f}, Max: {maximum}, Min: {minimum}")

#         elif choose_option == "3":
#             numbers = read_data()
#             print("Sorted Data:", sort_data(numbers))

#         elif choose_option == "4":
#             numbers = read_data()
#             print("Filtered Data (>100):", filter_data(numbers, 100))

#         elif choose_option == "5":
#             numbers = read_data()
#             generate_report(numbers)

#         elif choose_option == "6":
#             print("Exiting..")
#             break
#         else:
#             print("Inavalid option selected. ")

# if __name__ == "__main__":
#     main()


## +++++++++++++++++++++++++++++++++++++++++++++

# with open("analyzer.txt", "r") as f:
#     line = f.read().strip()

# clean_line = line.replace("[", "").replace("]", "").replace(",", " ")

# lines = clean_line.split()

# numbers = []
# for l in lines:
#     numbers.append(int(l.strip()))

# total = 0
# for n in numbers:
#     total += n

# maximum = numbers[0]
# for n in numbers:
#     if n > maximum:
#         maximum = n

# minimum = numbers[0]
# for n in numbers:
#     if n < minimum:
#         minimum = n


# avg = total / len(numbers)

# sort_num = sorted(numbers)


# num = 100
# filter_num = [n for n in numbers if n > num]

# print("---- Mini Data Analyzer ------")
# print("Total: ", total)
# print("Maximum: ", maximum)
# print("Minimum: ", minimum)
# print("Average: ", avg)
# print("Sorting: ", sort_num)
# print("Filter numbers: ", filter_num)

## +++++++++++++++++++++++++++++++++++++++++++

# def load_data():
#     data = "23, 67, 89, 823,151, 672, 8762, 562, 78"
#     with open("analyzer.txt", "w") as f:
#         f.write(data)

# def read_data():
#     with open("analyzer.txt", 'r') as f:
#         line = f.read()

#     numbers = [int(n.strip()) for n in line.split(",")]
#     return numbers

# def calculate(numbers):
#     total = sum(numbers)
#     avg = total / len(numbers)
#     maximum = max(numbers)
#     minimum = min(numbers)
#     return total, avg, minimum, maximum

# def sort_data(numbers):
#     return sorted(numbers)

# def filter_data(numbers, threshold):
#     return [n for n in numbers if n > threshold]

# def generate_report(numbers):
#     total, avg, minimum, maximum = calculate(numbers)
#     with open('generate.txt', 'w') as f:
#         f.write("----- Generated Report ------\n")
#         f.write(f"Numbers: {numbers}\n")
#         f.write(f"Total: {total}\n")
#         f.write(f"Average: {avg:.2f}\n")
#         f.write(f"Minimum: {minimum}\n")
#         f.write(f"Maximum: {maximum}\n")
#         f.write("Generated Report: generate.txt")

# def main():
#     while True:
#         print("\n----- Mini Data Analyzer -----")
#         print("1. Load data ")
#         print("2. Read and show Data")
#         print("3. Sort Data")
#         print("4. Filter Data >100")
#         print("5. Generate report")
#         print("6. Exit")

#         choose_option = input("Enter an option: ").strip()
#         if choose_option == "1":
#             load_data()
#             print("Data loaded to file. ")

#         elif choose_option == "2":
#             numbers = read_data()
#             total, avg, maximum, minimum = calculate(numbers)
#             print(f"Numbers: {numbers}")
#             print(f"Total: {total}, Average: {avg:.2f}, Max: {maximum}, Min: {minimum}")

#         elif choose_option == "3":
#             numbers = read_data()
#             print("Sorted Data:", sort_data(numbers))

#         elif choose_option == "4":
#             numbers = read_data()
#             print("Filtered Data (>100):", filter_data(numbers, 100))

#         elif choose_option == "5":
#             numbers = read_data()
#             generate_report(numbers)

#         elif choose_option == "6":
#             print("Exiting..")
#             break
#         else:
#             print("Inavalid option selected. ")

# if __name__ == "__main__":
#     main()

## ++++++++++++++++++++++++++++++++++++++++++++++++++

