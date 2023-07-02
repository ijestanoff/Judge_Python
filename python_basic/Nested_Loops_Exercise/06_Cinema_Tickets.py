student_count = 0
kid_count = 0
standard_count = 0
total_tickets = 0
command = ""
while True:
    if command == "Finish":
        break
    film_name = input()
    if film_name == "Finish":
        break
    free_space = int(input())
    watch_count = 0
    while True:
        command = input()
        if command == "End" or command == "Finish":
            print(f"{film_name} - {watch_count / free_space * 100:.2f}% full.")
            break
        if command == "student":
            student_count += 1
        elif command == "kid":
            kid_count += 1
        elif command == "standard":
            standard_count += 1
        total_tickets += 1
        watch_count += 1
        if watch_count == free_space:
            print(f"{film_name} - {watch_count / free_space * 100:.2f}% full.")
            break
print(f"Total tickets: {total_tickets}")
print(f"{student_count / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_count / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_count / total_tickets * 100:.2f}% kids tickets.")