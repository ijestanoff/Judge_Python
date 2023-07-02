# •	Първи ред – брой дни – цяло число в интервал [1…5000]
# •	Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# •	Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# •	Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# •	Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
# На конзолата трябва да се отпечата на един ред:
# •	Ако оставената храна Е достатъчна:
# o	"{килограма остатък} kilos of food left."
# 	Резултатът трябва да е закръглен към по-ниското цяло число
# •	Ако оставената храна НЕ Е достатъчна:
# o	“{килограма недостигат} more kilos of food are needed.”
# 	Резултатът трябва да е закръглен към по-високото цяло число

from math import ceil
day_count = int(input())
total_food = int(input())
dog_day_food = float(input())
cat_day_food = float(input())
turtle_day_food = float(input())
food_needed = day_count * (dog_day_food + cat_day_food + turtle_day_food/1000)
if food_needed <= total_food:
    print(f"{int(total_food - food_needed)} kilos of food left.")
else:
    print(f"{ceil(food_needed - total_food)} more kilos of food are needed.")