actor_name = input()
point_from_academy = float(input())
judge_number = int(input())
total_points = point_from_academy
for count in range(0,judge_number,1):
    judge_name = input()
    judge_name_length = 0
    for cnt in judge_name:
        judge_name_length += 1
    points_from_judge = float(input())
    total_points += judge_name_length * points_from_judge / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
if total_points <= 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")