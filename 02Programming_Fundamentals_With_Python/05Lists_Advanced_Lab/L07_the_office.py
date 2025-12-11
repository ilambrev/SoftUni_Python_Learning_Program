employees_happiness = [int(eh) for eh in input().split()]
factor = int(input())

employees_happiness_factor = [eh * factor for eh in employees_happiness]
average_happiness = sum(employees_happiness_factor) / len(employees_happiness_factor)

happy_employess = len([eh for eh in employees_happiness_factor if eh >= average_happiness])

if happy_employess >= len(employees_happiness_factor) / 2:
    print(f"Score: {happy_employess}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_employess}/{len(employees_happiness)}. Employees are not happy!")