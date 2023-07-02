#  цвете	            Роза	Далия	Лале	Нарцис	Гладиола
#  Цена на брой в лева	5	    3.80	2.80	3	    2.50
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
flowers = input()
pcs_flowers = int(input())
budget = int(input())
price = 0
if flowers == "Roses":
    price = 5
    if pcs_flowers > 80:
        price *= 0.9
elif flowers == "Dahlias":
    price = 3.8
    if pcs_flowers > 90:
        price *= 0.85
elif flowers == "Tulips":
    price = 2.8
    if pcs_flowers > 80:
        price *= 0.85
elif flowers == "Narcissus":
    price = 3
    if pcs_flowers < 120:
        price *= 1.15
elif flowers == "Gladiolus":
    price = 2.5
    if pcs_flowers < 80:
        price *= 1.2
amount = pcs_flowers * price
if amount <= budget:
    print(f"Hey, you have a great garden with {pcs_flowers} {flowers} and {budget-amount:.2f} leva left.")
else:
    print(f"Not enough money, you need {amount-budget:.2f} leva more.")