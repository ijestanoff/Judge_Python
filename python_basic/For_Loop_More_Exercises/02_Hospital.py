calculation_period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for day in range(0, calculation_period, 1):
    patients = int(input())
    if (day+1) % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if patients > doctors:
        treated_patients += doctors
        untreated_patients += patients - doctors
    else:
        treated_patients += patients
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
