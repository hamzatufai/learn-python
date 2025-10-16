##🧾 Python Lists – My Practice Log (30 June 2025)
## +++++++++++++++++++++++++++++++++++++++++++++++++

# num = ["2", "6", "8", "9", "10"]
# print("string list:", num)
# num = [int(n) for n in num]

# data = [n for n in num]
# print("Integer list:", data)

# num = [int(n) for n in num]

# maximum = num[0]
# for n in num:
#     if n > maximum:
#         maximum = n
# print("Maximum:", maximum)

# minimum = num[0]
# for n in num:
#     if n < minimum:
#         minimum = n

# print("Minimum:", minimum)

# sort_num = sorted(num)
# second_highest = sort_num[-2]
# print("Second largest:", second_highest)

# reversed_num = num[::-1]
# print("Reverse num:", reversed_num)


# even_list = [int(n) for n in num if n % 2 == 0]
# print("Even list:", even_list)

## ++++++++++++++++++++++++++++++++++++++++++++++++++++++
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#     ]
# flat = [num for row in matrix for num in row ]

# Total_sum_of_matrix  = 0
# for n in flat:
#     Total_sum_of_matrix += n
# print("Total:",Total_sum_of_matrix)

# maximum = max(flat)
# print("Maximum:",maximum)

# even_filter_matrix = [n for n in flat if n %2 == 0]
# print(even_filter_matrix)


## +++++++++++++++++++++++++++++++++++++++
# nums = [5,10,15,20,25]
# doubled = list(map(lambda x: x*2, nums))
# # print(doubled)

# greater_num = list(filter(lambda x: x > 10, nums))
# print("Greater Num:", greater_num)

# from functools import reduce
# total_sum = reduce(lambda x, y: (x + y), nums)
# print("Total:",total_sum)

## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# words = ["apple", "banana", "guava","kiwi","pineapple", "mango"]
# words.sort(key=len)
# words.sort(key=lambda x: x[-1])
# print(words)


## ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# even_num_cube = [n**3 for n in numbers if n % 2 == 0]
# even_num_cube.sort(reverse=True)
# print(even_num_cube)

## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# words = ["python", "data", "science", "ai", "machine", "learning"]
# len_words = [n for n in words if len(n) > 5]
# upper_words = [n.upper() for n in len_words]
# sort_word = sorted(upper_words)
# print(len_words)
# print(upper_words)
# print(sort_word)

## +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# salaries = [25000, 40000, 18000, 50000, 30000, 60000]
# above_salaries = [n for n in salaries if n > 30000]
# annual_salaries = [n * 12 for n in above_salaries]
# print(annual_salaries)

# ++
# matrix = [[10, 25, 30], [45, 50, 5], [70, 80, 20]]
# flaten_list = [n for row in matrix for n in row]
# divisible = [div for div in flaten_list if div % 10 == 0]
# sort_assending = sorted(divisible)
# print("flat list: ", flaten_list)
# print("Divide: ", divisible)
# print("Sort Assending: ",sort_assending)


# ++
# text = ["AI", "is", "changing", "the", "future", "of", "technology"]
# longer_words = [w for w in text if len(w) > 3]
# lower_case = [l.lower() for l in longer_words]
# print(lower_case)

# ++
# nums = [4, 6, 2, 6, 7, 4, 2, 6, 9, 2, 7, 4]
# unique_num = list(set(nums))
# freq = {n: nums.count(n) for n in unique_num}
# sort_freq = dict(sorted(freq.items(), key=lambda x: x[1]))
# print(freq)
# print(sort_freq)


# ++
# students = [("Ali", [80, 75, 90]), ("Sara", [60, 65, 70]), ("Hamza", [95, 85, 100])]
# total_marks = {name:sum(marks) for name, marks in students}
# for key, val in total_marks.items():
#     print(f"{key}: get {val} marks")
# avg = {name: sum(marks)/len(marks) for name, marks in students}
# for key, val in avg.items():
#     print(f"{key}: {val:.2f}")


## ++
# students = [
#     ["Ali", [70, 80, 90]],
#     ["Hamza", [60, 75, 85]],
#     ["Sara", [88, 92, 79]],
#     ["Ayesha", [50, 65, 70]],
#     ["Bilal", [95, 90, 100]],
# ]

# total_marks = {name: sum(marks) for name, marks in students}
# avg_marks = {name: round(sum(marks) / len(marks), 2) for name, marks in students}

# topper = max(avg_marks, key=avg_marks.get)

# lowest = min(avg_marks, key=avg_marks.get)

# above_80 = [name for name, avg in avg_marks.items() if avg > 80]

# print("Total Marks:",total_marks)
# print("Average Marks:",avg_marks)
# print("Topper:",topper)
# print("Lowest:",lowest)
# print("Marks > 80:", above_80)

## +++
# input_list = [4, 5, 4, 2, 2, 3, 5]
# input_list = list(set(input_list))

# +++
# nested = [1, [2, [3, 4], 5], 6]
# def flatten(nested):
#     flat_list = []
#     for item in nested:
#         if isinstance(item, list):
#             flat_list.extend(flatten(item))
#         else:
#             flat_list.append(item)
#     return flat_list


# single_list = flatten(nested)
# print(single_list)

## +++
# input_list = ["a", "b", "a", "c", "b", "a"]
# result = []
# for item in input_list:
#     if not any(pair[0] == item for pair in result):
#         result.append([item, input_list.count(item)])
# print(result)

## +++
# matrix = [[1, 2, 3], [4, 5, 6]]
# transpose = []
# for i in range(len(matrix[0])):
#     row = []
#     for j in range(len(matrix)):
#         row.append(matrix[j][i])
#     transpose.append(row)

# print(transpose)

## +++
# nums = [1, 2, 3, 4, 5]
# k = 2

# k = k % len(nums)
# rotated = nums[-k:] + nums[:-k]
# print(rotated)

## +++
# sales = ["100", "250", "N/A", "300", "450", "N/A", "500"]
# # print("Orginal:", sales)
# sales[2] = 10
# sales[-2] = 10

# str_into_int = [int(n) for n in sales]
# total_sale = sum(str_into_int)
# avg_sale = round(total_sale / len(str_into_int), 2)
# print("String into int:", str_into_int)
# print("Total sale:",total_sale)
# print("Average sale:",avg_sale)

# students = [
#     ["Ali", [45, 56, 67]],
#     ["Hamza", [78, 81, 69]],
#     ["Sara", [90, 95, 92]],
#     ["John", [50, 42, 38]],
# ]
# students_total_marks = {name:sum(marks) for name, marks in students}
# student_avg = {name:round(sum(marks)/len(marks),2) for name, marks in students}
# below_50 = {name: avg for name, avg in student_avg.items() if avg < 50}
# topper = {name:avg for name, avg in student_avg.items() if avg > 80}
# print("Topper Student:",topper)
# print("Student Average:",student_avg)
# print("Lowest Average:",below_50)


# reviews = [
#     "The food was good and tasty",
#     "Good service but food was cold",
#     "Tasty food and friendly staff",
#     "Service was slow but food was good",
# ]


# words = []

# for review in reviews:
#     for word in review.lower().split():
#         words.append(word)

# print(words)

# frequency = []
# for word in words:
#     found = False

#     for pair in frequency:
#         if pair[0] == word:
#             pair[1] += 1
#             found = True
#             break

#     if not found:
#         frequency.append([word, 1])

# print(frequency)


# for i in range(len(frequency)):
#     for j in range(i + 1, len(frequency)):
#         if frequency[i][1] < frequency[j][1]:
#             frequency[i], frequency[j] = frequency[j], frequency[i]

# top3 = frequency[:3]
# print(top3)
