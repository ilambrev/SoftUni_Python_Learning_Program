time_in_hours_to_complete_one_project = 3
name_of_the_architect = input()
number_of_projects = int(input())
total_hours_needed = number_of_projects * time_in_hours_to_complete_one_project

print(f'The architect {name_of_the_architect} will need '
      f'{total_hours_needed} hours to complete {number_of_projects} project/s.')