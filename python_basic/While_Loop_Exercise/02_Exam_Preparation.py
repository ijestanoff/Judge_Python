bad_rating_number = int(input())
total_rating = 0
number_rating = 0
current_bad_rating = 0
last_name =""
while True:
    exam_name = input()
    if exam_name == "Enough":
        print(f"Average score: {total_rating / number_rating:.2f}")
        print(f"Number of problems: {number_rating}")
        print(f"Last problem: {last_name}")
        break
    else:
        last_name = exam_name
        exam_rating = int(input())
        total_rating += exam_rating
        number_rating += 1
        if exam_rating <= 4:
            current_bad_rating += 1
            if current_bad_rating == bad_rating_number:
                print(f"You need a break, {current_bad_rating} poor grades.")
                break



