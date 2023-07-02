students_name = input()
students_class = 1
class_repeat = 0
students_rating = 0
total_rating = 0
while students_class < 13:
    students_rating = float(input())
    if students_rating >= 4:
        students_class += 1
        class_repeat = 0
        total_rating += students_rating
    else:
        if class_repeat == 1:
            print(f"{students_name} has been excluded at {students_class} grade")
            break
        class_repeat = 1
if students_class == 13:
    print(f"{students_name} graduated. Average grade: {total_rating / 12:.2f}")