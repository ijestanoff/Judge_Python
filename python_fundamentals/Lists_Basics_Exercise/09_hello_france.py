items_list = input().split("|")
budget = float(input())
start_budget = budget
new_items = []
profit = 0
for count in range(len(items_list)):
    item = items_list[count].split("->")
    item_values = float(item[1])
    item_valid = (
            item[0] == "Clothes" and item_values <= 50 and item_values <= budget
            or item[0] == "Shoes" and item_values <= 35 and item_values <= budget
            or item[0] == "Accessories" and item_values <= 20.5 and item_values <= budget
    )
    if item_valid:
        budget -= item_values
        new_items.append(item_values * 1.4)
        profit += item_values * 0.4
for count in range(len(new_items)):
    print(f"{new_items[count]:.2f}", end=" ")
print("")
print(f"Profit: {profit:.2f}")
if profit + start_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

