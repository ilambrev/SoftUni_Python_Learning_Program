period_in_days = int(input())

doctors_count = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, period_in_days + 1):
    patients_for_current_day = int(input())

    if day % 3 == 0 and untreated_patients > treated_patients:
        doctors_count += 1

    if doctors_count >= patients_for_current_day:
        treated_patients += patients_for_current_day
    else:
        treated_patients += doctors_count
        untreated_patients += patients_for_current_day - doctors_count

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')