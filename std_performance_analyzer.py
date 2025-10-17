students = [
    {"name": "Ali", "math": 85, "science": 78, "attendance": 90},
    {"name": "Sara", "math": 95, "science": 88, "attendance": 92},
    {"name": "Ahmed", "math": 45, "science": 55, "attendance": 70},
    {"name": "Fatima", "math": 76, "science": 80, "attendance": 88},
    {"name": "Zain", "math": 60, "science": 65, "attendance": 80}
]

def calc_avg(subject):
    total = 0
    for s in students:
        total += s[subject]
    return round(total / len(students), 2)

def get_topper(subject):
    return max(students, key=lambda s: s[subject])

def get_grade(percentage):
    if percentage >= 90: return "A+"
    elif percentage >= 80: return "A"
    elif percentage >= 70: return "B"
    elif percentage >= 60: return "C"
    elif percentage >= 50: return "D"
    else: return "F"

def suppl_count(math, sci):
    count = 0
    if math < 50: count += 1
    if sci < 50: count += 1
    return count

def class_topper():
    return max(students, key=lambda s: s["math"] + s["science"])

def show_report():
    for s in students:
        total = s["math"] + s["science"]
        percentage = (total / 200) * 100
        grade = get_grade(percentage)
        supply = suppl_count(s["math"], s["science"])

        print("=" * 50)
        print(f" {s['name']}")
        print(f" Math: {s['math']} |  Science: {s['science']} |  Attendance: {s['attendance']}%")
        print(f" Total: {total}/200 |  {round(percentage, 2)}% |  Grade: {grade} |  Supply: {supply}")

def show_class_summary():
    math_avg = calc_avg("math")
    sci_avg = calc_avg("science")
    att_avg = calc_avg("attendance")

    topper = class_topper()
    math_topper = get_topper("math")
    sci_topper = get_topper("science")
    att_topper = get_topper("attendance")

    print("\n" + "=" * 50)
    print(" CLASS SUMMARY")
    print(f" Average Math Marks: {math_avg}")
    print(f" Average Science Marks: {sci_avg}")
    print(f" Average Attendance: {att_avg}%")
    print("=" * 50)
    print(f" Class Topper: {topper['name']} ({topper['math'] + topper['science']}/200)")
    print(f" Math Topper: {math_topper['name']} ({math_topper['math']})")
    print(f" Science Topper: {sci_topper['name']} ({sci_topper['science']})")
    print(f" Best Attendance: {att_topper['name']} ({att_topper['attendance']}%)")
    print("=" * 50)

def main():
    print("\n📚 STUDENT REPORT CARD SYSTEM - INTERMEDIATE LEVEL\n")
    show_report()
    show_class_summary()

main()
