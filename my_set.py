# departments = {
#     "Sales": {("wahaj", "Manager"), ("Sara", "Executive")},
#     "IT": {("Hamza", "Developer"), ("Ahmed", "Support")},
#     "HR": {("Fatima", "Recruiter"), ("wahaj", "Manager")},
# }

# ## Print all employees (flatten the sets)

# all_emp = set()
# for emp_set in departments.values():
#     all_emp.update(emp_set)

# # print("All Employees: ", all_emp)


# ## Find people who work in multiple departments.
# from collections import Counter

# emp_count = Counter()
# for emp_set in departments.values():
#     for emp in emp_set:
#          emp_count[emp] += 1

# multi_dept = [emp for emp, count in emp_count.items() if count > 1]
# # print("Employee in multiple role: ", multi_dept)
# # print("Employees in multiple department: ",emp_dept)

# ## Add a new employee (“Zara”, “Intern”) to HR.
# departments["HR"].add(("Zara", "Intern"))
# # print("Add name in HR department:", departments["HR"])

# ## Remove an employee from IT
# departments["IT"].remove(("Hamza", "Developer"))
# # print("Remove Employee from IT: ", departments["IT"])

# ## Check if ("Ali", "Manager") exists in Sales
# exist = ("wahaj", "Manager") in departments["Sales"]
# status = "yes" if exist else "no"
# # print(f"Is '(wahaj)' exist in sales department? {status}")


### ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# departments = {
#     "Sales": {("Ali", "Manager"), ("Sara", "Executive"), ("Omar", "Intern")},
#     "IT": {("Hamza", "Developer"), ("Ahmed", "Support"), ("Ali", "Consultant")},
#     "HR": {("Fatima", "Recruiter"), ("Sara", "Coordinator")},
#     "Finance": {("Omar", "Analyst"), ("Zara", "Manager")},
#     "Marketing": {("Hamza", "Executive"), ("Zara", "Strategist")},
# }
# Q1. Unique employees
# unique_emp = set()
# for emp in departments.values():
#     for name in emp:

#         name = name[0]
#         unique_emp.add(name)

# print("Unique Employees:", unique_emp)

# Q2. Employees in multiple departments
# from collections import Counter

# emp_count = Counter()
# for emp_set in departments.values():
#     for emp in emp_set:
#         emp_count[emp] += 1

# multi_dept = [emp for emp, count in emp_count.items() if count > 1]
# print("Employee in multiple departments: ", multi_dept)

# Q3. Sales but not IT
# sales_name = {name for name, _ in departments["Sales"]}
# it_name = {name for name, _ in departments["IT"]}

# sales_not_it = sales_name - it_name
# print("\nSales not IT: ", sales_not_it)


# Q4. IT or Marketing (union)
# it_or_marketing = departments["IT"] | departments["Marketing"]
# print("\nIT or Marketing:", it_or_marketing)

# Q5. IT and Marketing (intersection)
# it_and_marketing = departments["IT"] & departments["Marketing"]
# print("\nIT and Marketing:", it_and_marketing)

# Q6. Finance or HR but not both (symmetric difference)
# fin = {name for name, _ in departments["Finance"]}
# hr = {name for name, _ in departments["HR"]}
# fin_hr_sym = fin ^ hr
# print("Finance or HR:", fin_hr_sym)


# Q7. HR subset of Sales?
# is_subset = departments["HR"].issubset(departments["Sales"])
# status = "yes" if is_subset else "no"
# print("HR subset sale: ", status)


# Finance and Marketing disjoint
# makr = {name for name, _ in departments["Marketing"]}
# is_disjoint = fin.isdisjoint(makr)
# status = "yes" if makr else "no"
# print("Finance and Marketing disjoint? ", status)

# Q9. Employees not in HR
# all_employee = set()
# for emp_set in departments.values():
#     for emp in emp_set:
#         all_employee.add(emp)

# not_in_hr = all_employee - departments["HR"]
# print("\nEmployee not in HR: ", not_in_hr)

## ++++++++++++++++++++++++++++++++++++++++++++++
employees = [
    {"name": "Ali", "skills": {"Python", "SQL", "Excel", "PowerBI"}, "dept": "IT"},
    {"name": "Sara", "skills": {"Excel", "PowerBI", "SQL"}, "dept": "Finance"},
    {"name": "Hamza", "skills": {"Python", "Java", "C++"}, "dept": "IT"},
    {"name": "Ahmed", "skills": {"Recruitment", "Excel", "PowerBI"}, "dept": "HR"},
    {"name": "Zara", "skills": {"Marketing", "PowerBI"}, "dept": "Marketing"},
]

projects = {
    "Data Migration": {"Python", "SQL"},
    "Reporting Dashboard": {"Excel", "PowerBI"},
    "Recruitment System": {"Recruitment", "Excel"},
    "App Development": {"Java", "C++"},
    "Data Analyst": {"Python", "SQL", "PowerBI", "Excel"},
    "AI": {"Deep Learning", "ML learning", "Python", "SQL"},
}

## Find unique skills in company
unique_skill = set()
for emp_set in employees:

    skill = emp_set["skills"]
    unique_skill.update(skill)

# print("Unique skill in comapny: \n",unique_skill)

## Find employees who can work on each project

for project, req_skill in projects.items():
    capable = []

    for emp in employees:

        if req_skill.issubset(emp["skills"]):
            capable.append(emp["name"])

    # print(f"{project}: {capable}")


data = {}
for emp_set in employees:

    dept = emp_set["dept"]
    employee = emp_set["name"]
    data[dept] = employee

# print(f"Departemnt & Employee:\n {data}")


## Find skills missing in company for projects

all_skills = set()
for emp in employees:

    all_skills |= emp["skills"]
for project, req_skill in projects.items():
    missing = req_skill - all_skills

    # print(f"{project} missing skills: {missing if missing else "None"}")



## Find employee(s) with maximum skills

max_skill = max(len(emp['skills']) for emp in employees)
top_emp = [emp['name'] for emp in employees if len(emp['skills']) == max_skill]

print(f"Employee with maximum skill: {top_emp}")
print(f"They have {max_skill} skills.")

