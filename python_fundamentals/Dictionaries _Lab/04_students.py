students = {}
while True:
    command = input().split(":")
    if len(command) == 1:
        break
    student, student_id, course = command
    students[student] = [student_id, course]

for student in students:
    if students[student][1].startswith(command[0][0:3]):
        print(f"{student} - {students[student][0]}")

