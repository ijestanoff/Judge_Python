# •	Ако числото е до 100 включително, бонус точките са 5;
# •	Ако числото е по-голямо от 100, бонус точките са 20% от числото;
# •	Ако числото е по-голямо от 1000, бонус точките са 10% от числото.
#
# •	Допълнителни бонус точки (начисляват се отделно от предходните):
# o	За четно число  + 1 т.
# o	За число, което завършва на 5  + 2 т.

whole_number = int(input())
if whole_number <= 100:
    bonus_points = 5
elif whole_number <= 1000:
    bonus_points = whole_number * 0.20
else:
    bonus_points = whole_number * 0.10

if whole_number % 2 == 0:
    bonus_points += 1
if whole_number % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(whole_number + bonus_points)