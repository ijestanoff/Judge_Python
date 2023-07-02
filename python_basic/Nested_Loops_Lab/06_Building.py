total_floors = int(input())
rooms_per_floor = int(input())
symbol = ""
label_string = ""
for floor in range(total_floors, 0, -1):
    if floor == total_floors:
        symbol = "L"
    elif floor % 2 == 0:
        symbol = "O"
    else:
        symbol = "A"
    for room in range(rooms_per_floor):
        label_string += symbol + str(floor) + str(room) + " "
    print(label_string)
    label_string = ""
