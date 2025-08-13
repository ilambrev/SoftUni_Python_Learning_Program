months_count = int(input())

water_bill_monthly = 20.0
internet_bill_monthly = 15.0
total_sum_for_electricity = 0.0
total_sum_for_other_expenses = 0.0

for _ in range(months_count):
    electricity_bill_monthly = float(input())

    total_sum_for_electricity += electricity_bill_monthly

    total_sum_for_other_expenses += (electricity_bill_monthly
                                     + water_bill_monthly
                                     + internet_bill_monthly) * (1 + 0.2)

total_sum_for_water = water_bill_monthly * months_count
total_sum_for_internet = internet_bill_monthly * months_count

average_expenses_per_month = (total_sum_for_electricity
                              + total_sum_for_water
                              + total_sum_for_internet
                              + total_sum_for_other_expenses) / months_count

print(f'Electricity: {total_sum_for_electricity:.2f} lv')
print(f'Water: {total_sum_for_water:.2f} lv')
print(f'Internet: {total_sum_for_internet:.2f} lv')
print(f'Other: {total_sum_for_other_expenses:.2f} lv')
print(f'Average: {average_expenses_per_month:.2f} lv')