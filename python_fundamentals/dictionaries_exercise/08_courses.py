courses = {}
while True:
    command = input().split(" : ")
    if command[0] == "end":
        break
    course = command[0]
    student = command[1]
    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")
