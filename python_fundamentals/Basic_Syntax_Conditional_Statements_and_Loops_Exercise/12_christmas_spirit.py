quantity_of_decorations = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
budget = 0
spirit_points = 0
for current_day in range (1,days_left+1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        budget += ornament_set * quantity_of_decorations
        spirit_points += 5
    if current_day % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_of_decorations
        spirit_points += 13
    if current_day % 5 == 0:
        budget += tree_lights * quantity_of_decorations
        spirit_points += 17
        if current_day % 3 == 0:
            spirit_points += 30
    if current_day % 10 == 0:
        spirit_points -= 20
        budget += tree_skirt + tree_lights + tree_garland
if days_left % 10 == 0:
    spirit_points -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {spirit_points}")
