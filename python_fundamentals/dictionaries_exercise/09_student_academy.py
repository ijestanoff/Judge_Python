academy = {}
number = int(input())
for count in range(number):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

for student in academy:
    average = sum(academy[student]) / len(academy[student])
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")
