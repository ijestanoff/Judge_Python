def grade_calculator(my_grade):
    if 2 <= my_grade <= 2.99:
        print("Fail")
    elif my_grade <= 3.49:
        print("Poor")
    elif my_grade <= 4.49:
        print("Good")
    elif my_grade <= 5.49:
        print("Very Good")
    else:
        print("Excellent")


grade = float(input())
grade_calculator(grade)
