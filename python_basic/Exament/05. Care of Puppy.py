food_kg = int(input()) * 1000
food_left = 0
total_eaten = 0
while True:
    command = input()
    if command == "Adopted":
        break
    food_eaten = int(command)
    total_eaten += food_eaten
food_left = food_kg - total_eaten
if total_eaten <= food_kg:
    print(f"Food is enough! Leftovers: {food_left} grams.")
else:
    print(f"Food is not enough. You need {-food_left} grams more.")
