companies = {}
while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    company = command[0]
    employee_id = command[1]
    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company in companies:
    print(company)
    for employee_id in companies[company]:
        print(f"-- {employee_id}")
