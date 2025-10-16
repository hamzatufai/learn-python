employees = (
    ("Leslie", "Knope", "Deputy Director", 75000, "Female", 44),
    ("Ron", "Swanson", "Director", 70000, "Male", 55),
    ("Tom", "Haverford", "Entrepreneur", 50000, "Male", 36),
    ("April", "Ludgate", "Assistant", 25000, "Female", 29),
    ("Jerry", "Gergich", "Office Manager", 50000, "Male", 61),
    ("Donna", "Meagle", "Office Manager", 60000, "Female", 46),
    ("Ann", "Perkins", "Nurse", 55000, "Female", 35),
    ("Chris", "Traeger", "City Manager", 90000, "Male", 43),
    ("Ben", "Wyatt", "State Auditor", 70000, "Male", 38),
    ("Andy", "Dwyer", "Musician", 20000, "Male", 34),
)

## List all unique occupations (hint: use set on occupation field).
unique_occupation = {occ[2] for occ in employees}
# print(unique_occupation)

## Find total number of male vs female employees (hint: count genders).

gender_count = {"male": 0, "female": 0}

genders = [gen[4] for gen in employees]
for gen in genders:
    g = gen
    if g == "Male":
        gender_count["male"] += 1

    elif g == "Female":
        gender_count["female"] += 1

# print(gender_count)

## Get all employees younger than 40 (hint: filter by age).

fltr_above_40 = {emp for emp in employees if emp[5] < 40}
# print(fltr_above_40)

## Find the average salary of all employees (hint: loop + sum).

salaries = [sal[3] for sal in employees]
# for avg_sal in salaries:
total_avg_sal = 0
for s in salaries:
    total_avg_sal += s

avg_salary = round(total_avg_sal / len(employees), 2)
# print(avg_salary)
# print(total_avg_sal)

## Create a dict mapping employee full name → salary (hint: dict comprehension).

dict_mapping = {emp[0] + " " + emp[1]: emp[3] for emp in employees}
# print(dict_mapping)


## ## List all unique occupations (hint: use set on occupation field).
unique_occupation = {occ[2] for occ in employees}
# print(unique_occupation)

## Find total number of male vs female employees (hint: count genders).

gender_count = {"male": 0, "female": 0}

genders = [gen[4] for gen in employees]
for gen in genders:
    g = gen
    if g == "Male":
        gender_count["male"] += 1

    elif g == "Female":
        gender_count["female"] += 1

# print(gender_count)

## Get all employees younger than 40 (hint: filter by age).

fltr_above_40 = {age[5] for age in employees if age[5] > 40}
# print(fltr_above_40)

## Find the average salary of all employees (hint: loop + sum).

salaries = [sal[3] for sal in employees]
# for avg_sal in salaries:
total_avg_sal = 0
for s in salaries:
    total_avg_sal += s

avg_salary = round(total_avg_sal / len(employees), 2)
# print(avg_salary)
# print(total_avg_sal)

## Create a dict mapping employee full name → salary (hint: dict comprehension).

dict_mapping = {emp[0] + " " + emp[1]: emp[3] for emp in employees}
# print(dict_mapping)

## Find top 3 highest paid employees (hint: sort by salary descending).

top_3 = sorted(employees, key=lambda emp: emp[3], reverse=True)[:3]
top_3 = [(emp[0] + " " + emp[1], emp[3]) for emp in top_3]
# print(top_3)

## Group employees by occupation and count how many per occupation
## (hint: dict with occupation as key, count as value).


occupation_count = {}
for emp in employees:

    occ = emp[2]
    if occ in occupation_count:
        occupation_count[occ] += 1

    else:
        occupation_count[occ] = 1

# print(occupation_count)

## Find the employee(s) with the maximum salary (hint: max() with key function).

emp_max_sal = max(employees, key=lambda emp: emp[3])
# print(emp_max_sal)


## Create a set of all unique last names (hint: set comprehension).

unique_last_name = set()
for emp in employees:
    name = emp[1]
    unique_last_name.add(name)

# print(unique_last_name)


## Build a dict where key = gender, value = list of salaries,
#  then calculate avg salary per gender (mini data analysis style).

gender_salary = {}

for emp in employees:

    gender = emp[4]
    salary = emp[3]

    if gender not in gender_salary:
        gender_salary[gender] = []

    gender_salary[gender].append(salary)

print(gender_salary)


total_sal_by_name = {name: sum(sal) for name, sal in gender_salary.items()}

total_avg_sal_by_name = {
    name: round(total_sal_by_name[name] / len(gender_salary[name]), 2)
    for name in gender_salary
}
print(total_avg_sal_by_name)

