# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
budget = int(input())
season = input()
number_of_fishermen = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if number_of_fishermen <= 6:
    price *= 0.9
elif 7 <= number_of_fishermen <= 11:
    price *= 0.85
elif number_of_fishermen >= 12:
    price *= 0.75
if number_of_fishermen % 2 == 0 and not season == "Autumn":
    price *= 0.95
if price <= budget:
    print(f"Yes! You have {budget-price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price-budget:.2f} leva.")
