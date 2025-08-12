inherited_money = float(input())
year_to_live = int(input())

age = 18
initial_year = 1800
expenses_for_even_year = 12000

for year in range(initial_year, year_to_live + 1):
    if year % 2 == 0:
        inherited_money -= expenses_for_even_year
    else:
        inherited_money -= expenses_for_even_year + 50 * age
    
    age += 1

if (inherited_money >= 0):
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')
else:
    print(f'He will need {-inherited_money:.2f} dollars to survive.')