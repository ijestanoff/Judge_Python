time_list = input().split()
middle = len(time_list) // 2
time_car_left = 0
time_car_right = 0
for count in range(middle):
    if time_list[count] == "0":
        time_car_left *= 0.8
    else:
        time_car_left += int(time_list[count])
for count in range(len(time_list) - 1, middle, -1):
    if time_list[count] == "0":
        time_car_right *= 0.8
    else:
        time_car_right += int(time_list[count])
if time_car_left < time_car_right:
    print(f"The winner is left with total time: {time_car_left:.1f}")
else:
    print(f"The winner is right with total time: {time_car_right:.1f}")

