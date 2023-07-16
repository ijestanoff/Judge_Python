lines_number = int(input())
TANK_CAPACITY = 255
tank_water = 0
for count in range(lines_number):
    water = int(input())
    if water <= TANK_CAPACITY - tank_water:
        tank_water += water
    else:
        print("Insufficient capacity!")
print(tank_water)


