haircut_mens = 15
haircut_ladies = 20
haircut_kids = 10
color_touch_up = 20
color_full_color = 30
day_target = int(input())
type_operation = ""
total_sum = 0
while True:
    command = input()
    if command == "closed":
        break
    type_operation = input()
    if command == "haircut":
        if type_operation == "mens":
            total_sum += haircut_mens
        elif type_operation == "ladies":
            total_sum += haircut_ladies
        elif type_operation == "kids":
            total_sum += haircut_kids
    elif command == "color":
        if type_operation == "touch up":
            total_sum += color_touch_up
        elif type_operation == "full color":
            total_sum += color_full_color
    if total_sum >= day_target:
        break
if total_sum >= day_target:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {day_target - total_sum}lv. more.")
print(f"Earned money: {total_sum}lv.")
