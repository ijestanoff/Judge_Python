rooms_number = int(input())
free_chair = 0
print_game_on = True
for room in range(rooms_number):
    current_room = input().split()
    chair = len(current_room[0])
    visitor = int(current_room[1])
    if visitor > chair:
        print(f"{visitor-chair} more chairs needed in room {room + 1}")
        print_game_on = False
    else:
        free_chair += chair - visitor
if print_game_on:
    print(f"Game On, {free_chair} free chairs left")

