number_days = int(input())
total_food = float(input())
total_dog = 0
total_cat = 0
biscuit = 0
for number in range(1, number_days + 1):
    dog_food = int(input())
    total_dog += dog_food
    cat_food = int(input())
    total_cat += cat_food
    if number % 3 == 0:
        biscuit += (dog_food + cat_food) / 10
all_eaten = total_dog + total_cat
print(f"Total eaten biscuits: {biscuit:.0f}gr.")
print(f"{all_eaten / total_food * 100:.2f}% of the food has been eaten.")
print(f"{total_dog / all_eaten * 100:.2f}% eaten from the dog.")
print(f"{total_cat / all_eaten * 100:.2f}% eaten from the cat.")


