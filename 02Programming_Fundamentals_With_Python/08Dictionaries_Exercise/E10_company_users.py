companies = {}

input_data = input()

while not input_data == "End":
    company, employee_id = input_data.split(" -> ")

    if company not in companies:
        companies[company] = []

    if employee_id not in companies[company]:
        companies[company].append(employee_id)

    input_data = input()

new_line = "\n"

[print(f"{company}{new_line}{new_line.join(['-- ' + id for id in employes_ids])}"
       ) for company, employes_ids in companies.items()]

# Old task condition for output:
#
# When you finish reading the data, order the companies by the name in ascending order.
#
# Solution for output according to the old condition
#
# companies_sorted = {company: employes_ids for company, employes_ids in sorted(
#     companies.items(), key=lambda item: item[0])}
#
# [print(f"{company}{new_line}{new_line.join(['-- ' + id for id in employes_ids])}"
#        ) for company, employes_ids in companies_sorted.items()]