degree = int(input())
part_of_day = input()
outfit=""
shoes=""
if 10 <= degree <= 18:
    if part_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif part_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
if 18 < degree <= 24:
    if part_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif part_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
if degree >= 25:
    if part_of_day == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif part_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")
