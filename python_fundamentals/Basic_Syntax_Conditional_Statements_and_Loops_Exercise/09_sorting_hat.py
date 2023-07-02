while True:
    students_name = input()
    if students_name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if students_name == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(students_name) < 5:
        print(f"{students_name} goes to Gryffindor.")
    elif len(students_name) == 5:
        print(f"{students_name} goes to Slytherin.")
    elif len(students_name) == 6:
        print(f"{students_name} goes to Ravenclaw.")
    else:
        print(f"{students_name} goes to Hufflepuff.")
