from math import floor

centuries = int(input())

years = centuries * 100
days = years * 365.2422
hours = floor(days) * 24
minutes = hours * 60

print(f'{centuries} centuries = {years} years = {floor(days)} days = {hours} hours = {minutes} minutes')