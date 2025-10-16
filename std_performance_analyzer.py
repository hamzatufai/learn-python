students = [
    {"name": "Ali", "math": 85, "science": 78, "attendance": 90},
    {"name": "Sara", "math": 95, "science": 88, "attendance": 92},
    {"name": "Ahmed", "math": 45, "science": 55, "attendance": 70},
    {"name": "Fatima", "math": 76, "science": 80, "attendance": 88},
    {"name": "Zain", "math": 60, "science": 65, "attendance": 80}
]

def avg_for_each_sub():
    sub_math= 0
    sub_sci =0

    for data in students:
        math = data["math"]
        sci = data["science"]
        sub_math += math
        sub_sci += sci


        avg_math = round(sub_math / len(students), 2)
        avg_sci = round(sub_sci / len(students), 2)

    total = math + sci
    percentage = (total / 200) * 100

    if percentage >= 90: grade = "A+"
    elif percentage >= 80: grade = "A"
    elif percentage >= 70: grade = "B"
    elif percentage >= 60: grade = "C"
    elif percentage >= 50: grade = "D"
    else: grade = "F"


    class_topper = max(students, key=lambda s: s["math"] + s["science"])

    supply = 0
    if math < 50:
        supply += 1
    
    if sci < 50:
        supply +=1 

    
    print("="*20, " Report ", "="*20)
    print(f"Total Obtaine Marks for maths: {math}")
    print(f"Total Obtaine Marks for science: {sci}")
    print(f"Average marks for maths: {avg_math}")
    print(f"Average marks for science: {avg_sci}")
    print(f"Total Percentage: {percentage}")
    print(f"Grade: {grade}")
    print(f"Supply: {supply}")
    print(f"Class Topper: {class_topper}")
    print("=" * 40)



    
avg_for_each_sub()







